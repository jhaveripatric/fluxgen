"""
Main Flask application for FluxGen Document Generation System
"""
from flask import Flask, render_template, jsonify
import logging
import os
from pathlib import Path

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from config import config, Config
from routes.data_routes import data_bp
from routes.document_routes import doc_bp
from database import DatabaseManager

def create_app(config_name='development'):
    """Application factory pattern"""
    base_dir = Path(__file__).parent.resolve()
    # Explicit template/static paths so the app works no matter the CWD
    app = Flask(
        __name__,
        template_folder=str(base_dir / "templates"),
        static_folder=str(base_dir / "static"),
    )
    
    # Load configuration
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)
    
    # Set up logging
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )
    
    # Register blueprints
    app.register_blueprint(data_bp)
    app.register_blueprint(doc_bp)
    
    # Main routes
    @app.route('/')
    def index():
        """Main dashboard page"""
        return render_template('index.html')
    
    @app.route('/editor')
    def editor():
        """Data editor page"""
        return render_template('editor.html')
    
    @app.route('/documents')
    def documents():
        """Documents generation page"""
        return render_template('documents.html')
    
    @app.route('/api/health')
    def health_check():
        """Health check endpoint"""
        try:
            # Test database connection
            db = DatabaseManager(Config.DATABASE_PATH)
            company_info = db.get_company_info()
            
            return jsonify({
                'status': 'healthy',
                'database': 'connected',
                'company': company_info['legal_name'] if company_info else 'Not found'
            })
        except Exception as e:
            return jsonify({
                'status': 'unhealthy',
                'error': str(e)
            }), 500
    
    @app.errorhandler(404)
    def not_found(error):
        """Handle 404 errors"""
        return jsonify({'error': 'Not found'}), 404
    
    @app.errorhandler(500)
    def internal_error(error):
        """Handle 500 errors"""
        return jsonify({'error': 'Internal server error'}), 500
    
    return app


if __name__ == '__main__':
    app = create_app()
    app.run(debug=True, host='0.0.0.0', port=5001)
