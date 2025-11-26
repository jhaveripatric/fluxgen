"""
Data CRUD routes for FluxGen application
"""
from flask import Blueprint, request, jsonify, current_app
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from database import DatabaseManager
from config import Config
import logging

data_bp = Blueprint('data', __name__, url_prefix='/api/data')
logger = logging.getLogger(__name__)

def get_db():
    """Get database manager instance"""
    return DatabaseManager(Config.DATABASE_PATH)

@data_bp.route('/company', methods=['GET'])
def get_company():
    """Get company information"""
    try:
        db = get_db()
        company_info = db.get_company_info()
        if not company_info:
            return jsonify({'error': 'Company information not found'}), 404
        return jsonify(company_info)
    except Exception as e:
        logger.error(f"Error getting company info: {str(e)}")
        return jsonify({'error': 'Failed to retrieve company information'}), 500

@data_bp.route('/company', methods=['PUT'])
def update_company():
    """Update company information"""
    try:
        data = request.get_json()
        if not data:
            return jsonify({'error': 'No data provided'}), 400
        
        db = get_db()
        success = db.update_company_info(data)
        if success:
            return jsonify({'message': 'Company information updated successfully'})
        else:
            return jsonify({'error': 'Failed to update company information'}), 500
    except Exception as e:
        logger.error(f"Error updating company info: {str(e)}")
        return jsonify({'error': 'Failed to update company information'}), 500

@data_bp.route('/team', methods=['GET'])
def get_team_members():
    """Get all team members"""
    try:
        db = get_db()
        team_members = db.get_team_members()
        return jsonify(team_members)
    except Exception as e:
        logger.error(f"Error getting team members: {str(e)}")
        return jsonify({'error': 'Failed to retrieve team members'}), 500

@data_bp.route('/team', methods=['POST'])
def add_team_member():
    """Add new team member"""
    try:
        data = request.get_json()
        if not data or not data.get('name') or not data.get('role'):
            return jsonify({'error': 'Name and role are required'}), 400
        
        db = get_db()
        member_id = db.add_team_member(data)
        return jsonify({'message': 'Team member added successfully', 'id': member_id}), 201
    except Exception as e:
        logger.error(f"Error adding team member: {str(e)}")
        return jsonify({'error': 'Failed to add team member'}), 500

@data_bp.route('/team/<int:member_id>', methods=['PUT'])
def update_team_member(member_id):
    """Update team member"""
    try:
        data = request.get_json()
        if not data:
            return jsonify({'error': 'No data provided'}), 400
        
        db = get_db()
        success = db.update_team_member(member_id, data)
        if success:
            return jsonify({'message': 'Team member updated successfully'})
        else:
            return jsonify({'error': 'Team member not found'}), 404
    except Exception as e:
        logger.error(f"Error updating team member: {str(e)}")
        return jsonify({'error': 'Failed to update team member'}), 500

@data_bp.route('/team/<int:member_id>', methods=['DELETE'])
def delete_team_member(member_id):
    """Delete team member"""
    try:
        db = get_db()
        success = db.delete_team_member(member_id)
        if success:
            return jsonify({'message': 'Team member deleted successfully'})
        else:
            return jsonify({'error': 'Team member not found'}), 404
    except Exception as e:
        logger.error(f"Error deleting team member: {str(e)}")
        return jsonify({'error': 'Failed to delete team member'}), 500

@data_bp.route('/capex', methods=['GET'])
def get_capex():
    """Get all CAPEX items"""
    try:
        db = get_db()
        capex_items = db.get_investment_capex()
        return jsonify(capex_items)
    except Exception as e:
        logger.error(f"Error getting CAPEX items: {str(e)}")
        return jsonify({'error': 'Failed to retrieve CAPEX items'}), 500

@data_bp.route('/capex/<int:item_id>', methods=['PUT'])
def update_capex(item_id):
    """Update CAPEX item"""
    try:
        data = request.get_json()
        if not data:
            return jsonify({'error': 'No data provided'}), 400
        
        db = get_db()
        success = db.update_capex_item(item_id, data)
        if success:
            return jsonify({'message': 'CAPEX item updated successfully'})
        else:
            return jsonify({'error': 'CAPEX item not found'}), 404
    except Exception as e:
        logger.error(f"Error updating CAPEX item: {str(e)}")
        return jsonify({'error': 'Failed to update CAPEX item'}), 500

@data_bp.route('/production', methods=['GET'])
def get_production():
    """Get all production targets"""
    try:
        db = get_db()
        production_targets = db.get_production_targets()
        return jsonify(production_targets)
    except Exception as e:
        logger.error(f"Error getting production targets: {str(e)}")
        return jsonify({'error': 'Failed to retrieve production targets'}), 500

@data_bp.route('/production/<int:target_id>', methods=['PUT'])
def update_production(target_id):
    """Update production target"""
    try:
        data = request.get_json()
        if not data:
            return jsonify({'error': 'No data provided'}), 400
        
        db = get_db()
        success = db.update_production_target(target_id, data)
        if success:
            return jsonify({'message': 'Production target updated successfully'})
        else:
            return jsonify({'error': 'Production target not found'}), 404
    except Exception as e:
        logger.error(f"Error updating production target: {str(e)}")
        return jsonify({'error': 'Failed to update production target'}), 500

@data_bp.route('/alloys', methods=['GET'])
def get_alloys():
    """Get alloys catalog"""
    try:
        db = get_db()
        alloys = db.get_alloys_catalog()
        return jsonify(alloys)
    except Exception as e:
        logger.error(f"Error getting alloys: {str(e)}")
        return jsonify({'error': 'Failed to retrieve alloys catalog'}), 500

@data_bp.route('/funding', methods=['GET'])
def get_funding():
    """Get funding programs"""
    try:
        db = get_db()
        funding_programs = db.get_funding_programs()
        return jsonify(funding_programs)
    except Exception as e:
        logger.error(f"Error getting funding programs: {str(e)}")
        return jsonify({'error': 'Failed to retrieve funding programs'}), 500

@data_bp.route('/certifications', methods=['GET'])
def get_certifications():
    """Get certifications roadmap"""
    try:
        db = get_db()
        certifications = db.get_certifications_roadmap()
        return jsonify(certifications)
    except Exception as e:
        logger.error(f"Error getting certifications: {str(e)}")
        return jsonify({'error': 'Failed to retrieve certifications'}), 500

@data_bp.route('/assumptions', methods=['GET'])
def get_assumptions():
    """Get business assumptions"""
    try:
        db = get_db()
        assumptions = db.get_business_assumptions()
        return jsonify(assumptions)
    except Exception as e:
        logger.error(f"Error getting business assumptions: {str(e)}")
        return jsonify({'error': 'Failed to retrieve business assumptions'}), 500

@data_bp.route('/competitors', methods=['GET'])
def get_competitors():
    """Get competitor list"""
    try:
        db = get_db()
        competitors = db.get_competitors()
        return jsonify(competitors)
    except Exception as e:
        logger.error(f"Error getting competitors: {str(e)}")
        return jsonify({'error': 'Failed to retrieve competitors'}), 500

@data_bp.route('/competitor-pricing', methods=['GET'])
def get_competitor_pricing():
    """Get competitor pricing benchmarks"""
    try:
        db = get_db()
        pricing = db.get_competitor_pricing()
        return jsonify(pricing)
    except Exception as e:
        logger.error(f"Error getting competitor pricing: {str(e)}")
        return jsonify({'error': 'Failed to retrieve competitor pricing'}), 500

@data_bp.route('/market-analysis', methods=['GET'])
def get_market_analysis():
    """Get market analysis metrics"""
    try:
        db = get_db()
        market_data = db.get_market_analysis()
        return jsonify(market_data)
    except Exception as e:
        logger.error(f"Error getting market analysis: {str(e)}")
        return jsonify({'error': 'Failed to retrieve market analysis'}), 500

@data_bp.route('/raw-materials', methods=['GET'])
def get_raw_materials():
    """Get raw material specifications"""
    try:
        db = get_db()
        materials = db.get_raw_materials()
        return jsonify(materials)
    except Exception as e:
        logger.error(f"Error getting raw materials: {str(e)}")
        return jsonify({'error': 'Failed to retrieve raw materials'}), 500

@data_bp.route('/brand', methods=['GET'])
def get_brand():
    """Get brand assets"""
    try:
        db = get_db()
        brand_assets = db.get_brand_assets()
        return jsonify(brand_assets)
    except Exception as e:
        logger.error(f"Error getting brand assets: {str(e)}")
        return jsonify({'error': 'Failed to retrieve brand assets'}), 500

@data_bp.route('/summary', methods=['GET'])
def get_summary():
    """Get financial and operational summary"""
    try:
        db = get_db()
        summary = db.get_financial_summary()
        return jsonify(summary)
    except Exception as e:
        logger.error(f"Error getting summary: {str(e)}")
        return jsonify({'error': 'Failed to retrieve summary'}), 500
