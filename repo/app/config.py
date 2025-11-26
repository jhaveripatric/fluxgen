"""
Configuration settings for FluxGen Document Generation System
"""
import os
from pathlib import Path

class Config:
    """Base configuration"""
    
    # Flask settings
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'fluxgen-secret-key-2025'
    
    # Database settings
    # Project root (two levels up from this file: repo/app -> repo -> FluxGen)
    BASE_DIR = Path(__file__).resolve().parents[2]
    DATABASE_PATH = BASE_DIR / 'data' / 'fluxgen.db'
    
    # Output directory for generated PDFs
    OUTPUT_DIR = Path(__file__).parent / 'outputs'
    
    # FluxGen brand colors
    BRAND_COLORS = {
        'navy': '#1F3A4A',
        'orange': '#C87533',
        'gray': '#6B7280',
        'light_gray': '#F3F4F6',
        'white': '#FFFFFF',
        'black': '#000000'
    }
    
    # Document settings
    DOCUMENTS = {
        'executive_summary': 'Executive Summary',
        'business_plan': 'Business Plan',
        'financial_projections': 'Financial Projections',
        'market_analysis': 'Market Analysis',
        'technical_specs': 'Technical Specifications',
        'team_bios': 'Team Biographies',
        'site_requirements': 'Site Requirements',
        'pitch_deck': 'Pitch Deck',
        'individual_prep': 'Individual Prep Documents'
    }
    
    @classmethod
    def init_app(cls, app):
        """Initialize configuration"""
        # Ensure output directory exists
        cls.OUTPUT_DIR.mkdir(exist_ok=True)
        return cls


class DevelopmentConfig(Config):
    """Development configuration"""
    DEBUG = True


class ProductionConfig(Config):
    """Production configuration"""
    DEBUG = False


config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}
