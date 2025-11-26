"""
Document generation routes for FluxGen application
"""
from flask import Blueprint, request, jsonify, send_file, current_app
from pathlib import Path
import os
import logging
from datetime import datetime
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from config import Config
from database import DatabaseManager

# Import document generators
from generators.executive_summary import ExecutiveSummaryGenerator
from generators.business_plan import BusinessPlanGenerator
from generators.financial_projections import FinancialProjectionsGenerator
from generators.market_analysis import MarketAnalysisGenerator
from generators.technical_specs import TechnicalSpecsGenerator
from generators.team_bios import TeamBiosGenerator
from generators.site_requirements import SiteRequirementsGenerator
from generators.pitch_deck import PitchDeckGenerator
from generators.individual_prep import IndividualPrepGenerator

doc_bp = Blueprint('documents', __name__, url_prefix='/api/documents')
logger = logging.getLogger(__name__)

def get_db():
    """Get database manager instance"""
    return DatabaseManager(Config.DATABASE_PATH)

# Document generator mapping
GENERATORS = {
    'executive_summary': ExecutiveSummaryGenerator,
    'business_plan': BusinessPlanGenerator, 
    'financial_projections': FinancialProjectionsGenerator,
    'market_analysis': MarketAnalysisGenerator,
    'technical_specs': TechnicalSpecsGenerator,
    'team_bios': TeamBiosGenerator,
    'site_requirements': SiteRequirementsGenerator,
    'pitch_deck': PitchDeckGenerator,
    'individual_prep': IndividualPrepGenerator
}

@doc_bp.route('/generate/<doc_name>', methods=['POST'])
def generate_document(doc_name):
    """Generate a single PDF document"""
    try:
        if doc_name not in GENERATORS:
            return jsonify({'error': f'Unknown document type: {doc_name}'}), 400
        
        # Special handling for individual_prep - requires member_name parameter
        if doc_name == 'individual_prep':
            data = request.get_json() or {}
            member_name = data.get('member_name')
            
            if not member_name:
                return jsonify({'error': 'member_name parameter required for individual_prep'}), 400
            
            db = get_db()
            generator = IndividualPrepGenerator(db, Config.OUTPUT_DIR)
            
            logger.info(f"Individual prep document generation started for: {member_name}")
            output_path = generator.generate_for_member(member_name)
            
            if not output_path:
                return jsonify({'error': f'Failed to generate prep document for {member_name}'}), 500
            
            filename = output_path.name
            logger.info(f"Individual prep document generated successfully: {filename}")
            
            return jsonify({
                'message': f'Prep document for {member_name} generated successfully',
                'filename': filename,
                'status': 'completed',
                'file_size': output_path.stat().st_size
            }), 200
        
        # Get database manager and initialize generator
        db = get_db()
        generator_class = GENERATORS[doc_name]
        generator = generator_class(db, Config.OUTPUT_DIR)
        
        logger.info(f"Document generation started for: {doc_name}")
        
        # Generate the document
        output_path = generator.generate()
        filename = output_path.name
        
        logger.info(f"Document generated successfully: {filename}")
        
        return jsonify({
            'message': f'{Config.DOCUMENTS[doc_name]} generated successfully',
            'filename': filename,
            'status': 'completed',
            'file_size': output_path.stat().st_size
        }), 200
        
    except Exception as e:
        logger.error(f"Error generating document {doc_name}: {str(e)}")
        return jsonify({'error': f'Failed to generate {doc_name}: {str(e)}'}), 500

@doc_bp.route('/generate-all-prep', methods=['POST'])
def generate_all_prep_documents():
    """Generate prep documents for all team members"""
    try:
        db = get_db()
        generator = IndividualPrepGenerator(db, Config.OUTPUT_DIR)
        
        logger.info("Generating prep documents for all team members")
        output_paths = generator.generate_all_members()
        
        generated_files = []
        for output_path in output_paths:
            generated_files.append({
                'filename': output_path.name,
                'status': 'completed',
                'file_size': output_path.stat().st_size
            })
        
        logger.info(f"All prep documents generated successfully: {len(generated_files)} files")
        
        return jsonify({
            'message': 'All prep documents generated successfully',
            'generated': generated_files,
            'total_generated': len(generated_files)
        }), 200
        
    except Exception as e:
        logger.error(f"Error generating all prep documents: {str(e)}")
        return jsonify({'error': f'Failed to generate prep documents: {str(e)}'}), 500

@doc_bp.route('/generate-all', methods=['POST'])
def generate_all_documents():
    """Generate all PDF documents"""
    try:
        generated_files = []
        errors = []
        
        # Get database manager
        db = get_db()
        
        # Skip individual_prep from bulk generation as it requires special handling
        generators_to_run = {k: v for k, v in GENERATORS.items() if k != 'individual_prep'}
        
        for doc_name in generators_to_run.keys():
            try:
                logger.info(f"Generating document: {doc_name}")
                
                # Initialize generator and create document
                generator_class = generators_to_run[doc_name]
                generator = generator_class(db, Config.OUTPUT_DIR)
                output_path = generator.generate()
                
                generated_files.append({
                    'document': doc_name,
                    'filename': output_path.name,
                    'status': 'completed',
                    'file_size': output_path.stat().st_size
                })
                
            except Exception as e:
                logger.error(f"Error generating {doc_name}: {str(e)}")
                errors.append({
                    'document': doc_name,
                    'error': str(e)
                })
        
        logger.info(f"Bulk document generation completed: {len(generated_files)} successful, {len(errors)} errors")
        
        return jsonify({
            'message': 'Bulk document generation completed',
            'generated': generated_files,
            'errors': errors,
            'total_generated': len(generated_files),
            'total_errors': len(errors)
        }), 200
        
    except Exception as e:
        logger.error(f"Error in bulk document generation: {str(e)}")
        return jsonify({'error': f'Failed to complete bulk document generation: {str(e)}'}), 500

@doc_bp.route('/download/<filename>', methods=['GET'])
def download_document(filename):
    """Download a generated PDF document"""
    try:
        file_path = Config.OUTPUT_DIR / filename
        
        if not file_path.exists():
            return jsonify({'error': 'File not found'}), 404
        
        return send_file(
            file_path,
            as_attachment=True,
            download_name=filename,
            mimetype='application/pdf'
        )
        
    except Exception as e:
        logger.error(f"Error downloading file {filename}: {str(e)}")
        return jsonify({'error': 'Failed to download file'}), 500

@doc_bp.route('/list', methods=['GET'])
def list_documents():
    """List all generated PDF documents"""
    try:
        output_dir = Config.OUTPUT_DIR
        files = []
        # Ensure output directory exists even if app was started clean
        output_dir.mkdir(parents=True, exist_ok=True)

        if output_dir.exists():
            for file_path in output_dir.glob('*.pdf'):
                stat = file_path.stat()
                files.append({
                    'filename': file_path.name,
                    'size': stat.st_size,
                    'created': datetime.fromtimestamp(stat.st_ctime).isoformat(),
                    'modified': datetime.fromtimestamp(stat.st_mtime).isoformat()
                })
        
        # Sort by modification time (newest first)
        files.sort(key=lambda x: x['modified'], reverse=True)
        
        return jsonify({
            'files': files,
            'total': len(files)
        })
        
    except Exception as e:
        logger.error(f"Error listing documents: {str(e)}")
        return jsonify({'error': f'Failed to list documents: {str(e)}'}), 500

@doc_bp.route('/<filename>', methods=['DELETE'])
def delete_document(filename):
    """Delete a generated PDF document"""
    try:
        file_path = Config.OUTPUT_DIR / filename
        
        if not file_path.exists():
            return jsonify({'error': 'File not found'}), 404
        
        file_path.unlink()
        logger.info(f"Document deleted: {filename}")
        
        return jsonify({'message': 'Document deleted successfully'})
        
    except Exception as e:
        logger.error(f"Error deleting file {filename}: {str(e)}")
        return jsonify({'error': 'Failed to delete file'}), 500

@doc_bp.route('/status', methods=['GET'])
def get_generation_status():
    """Get document generation status"""
    try:
        # In a real application, this would check the status of background tasks
        # For now, return a simple status
        return jsonify({
            'status': 'ready',
            'active_generations': 0,
            'queue_length': 0
        })
        
    except Exception as e:
        logger.error(f"Error getting generation status: {str(e)}")
        return jsonify({'error': 'Failed to get status'}), 500
