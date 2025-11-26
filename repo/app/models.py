"""
Data models for FluxGen application
"""
from dataclasses import dataclass, asdict
from typing import Optional, List, Dict, Any
from datetime import datetime


@dataclass
class CompanyInfo:
    """Company information model"""
    id: int
    legal_name: str
    operating_name: Optional[str] = None
    location: Optional[str] = None
    province: Optional[str] = None
    country: Optional[str] = None
    incorporation_status: Optional[str] = None
    tagline: Optional[str] = None
    vision: Optional[str] = None
    mission: Optional[str] = None
    website: Optional[str] = None
    primary_email: Optional[str] = None
    primary_phone: Optional[str] = None
    created_date: Optional[str] = None
    
    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)


@dataclass
class TeamMember:
    """Team member model"""
    id: int
    name: str
    role: str
    email: Optional[str] = None
    phone: Optional[str] = None
    address: Optional[str] = None
    status: str = 'active'
    notes: Optional[str] = None
    created_date: Optional[str] = None
    
    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)


@dataclass
class CapexItem:
    """Capital expenditure item model"""
    id: int
    category: str
    description: Optional[str] = None
    estimated_cost_cad: Optional[float] = None
    actual_cost_cad: Optional[float] = None
    phase: str = 'pilot'
    status: str = 'planned'
    notes: Optional[str] = None
    created_date: Optional[str] = None
    
    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)


@dataclass
class ProductionTarget:
    """Production target model"""
    id: int
    phase: str
    output_kg_month: Optional[int] = None
    facility_type: Optional[str] = None
    process_flow: Optional[str] = None
    sourcing_strategy: Optional[str] = None
    target_date: Optional[str] = None
    status: str = 'planned'
    created_date: Optional[str] = None
    
    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)


@dataclass
class Alloy:
    """Alloy catalog item model"""
    id: int
    alloy_symbol: str
    alloy_name: Optional[str] = None
    grade_type: Optional[str] = None
    typical_composition: Optional[str] = None
    application: Optional[str] = None
    supplier: Optional[str] = None
    unit_cost_cad: Optional[float] = None
    notes: Optional[str] = None
    created_date: Optional[str] = None
    
    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)


@dataclass
class FundingProgram:
    """Funding program model"""
    id: int
    program_name: str
    funding_type: Optional[str] = None
    max_coverage_percent: Optional[int] = None
    max_amount_cad: Optional[float] = None
    eligibility_criteria: Optional[str] = None
    application_status: str = 'identified'
    application_date: Optional[str] = None
    approval_date: Optional[str] = None
    amount_received_cad: Optional[float] = None
    notes: Optional[str] = None
    created_date: Optional[str] = None
    
    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)


@dataclass
class Certification:
    """Certification roadmap item model"""
    id: int
    phase: int
    certification_name: str
    certification_body: Optional[str] = None
    target_date: Optional[str] = None
    completion_date: Optional[str] = None
    status: str = 'planned'
    cost_estimate_cad: Optional[float] = None
    priority: str = 'medium'
    notes: Optional[str] = None
    created_date: Optional[str] = None
    
    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)


@dataclass
class BrandAsset:
    """Brand asset model"""
    id: int
    brand_name: str
    brand_type: Optional[str] = None
    tagline: Optional[str] = None
    description: Optional[str] = None
    primary_color: Optional[str] = None
    accent_color: Optional[str] = None
    text_color: Optional[str] = None
    primary_font: Optional[str] = None
    logo_description: Optional[str] = None
    notes: Optional[str] = None
    created_date: Optional[str] = None
    
    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)


class ModelFactory:
    """Factory for creating model instances from database rows"""
    
    @staticmethod
    def create_company_info(data: Dict[str, Any]) -> CompanyInfo:
        return CompanyInfo(**data)
    
    @staticmethod
    def create_team_member(data: Dict[str, Any]) -> TeamMember:
        return TeamMember(**data)
    
    @staticmethod
    def create_capex_item(data: Dict[str, Any]) -> CapexItem:
        return CapexItem(**data)
    
    @staticmethod
    def create_production_target(data: Dict[str, Any]) -> ProductionTarget:
        return ProductionTarget(**data)
    
    @staticmethod
    def create_alloy(data: Dict[str, Any]) -> Alloy:
        return Alloy(**data)
    
    @staticmethod
    def create_funding_program(data: Dict[str, Any]) -> FundingProgram:
        return FundingProgram(**data)
    
    @staticmethod
    def create_certification(data: Dict[str, Any]) -> Certification:
        return Certification(**data)
    
    @staticmethod
    def create_brand_asset(data: Dict[str, Any]) -> BrandAsset:
        return BrandAsset(**data)