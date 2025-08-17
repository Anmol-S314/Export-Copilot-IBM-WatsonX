from typing import Dict, List, Optional
from pydantic import BaseModel, Field, AliasChoices

class CompanyProfileReport(BaseModel):
    company_name: str = Field(description="The official name of the company.")
    core_products: List[str] = Field(description="A list of the company's main products or product categories.")
    mission_statement: str = Field(description="A brief mission statement or company vision found in the documents.")
    key_strengths: List[str] = Field(description="Key strengths or competitive advantages of the company.")
    auto_generated_summary: str = Field(description="A concise, auto-generated summary of the company profile for use in other prompts.")

class HSCodeResult(BaseModel):
    hs_code: str
    confidence: float
    reasoning: str
    alternative_codes: List[str]
    customs_duty: Optional[float] = None
    documentation_required: List[str]

class DocumentValidationReport(BaseModel):
    overall_status: str
    document_scores: Dict[str, float]
    inconsistencies: List[str]
    missing_requirements: List[str]
    recommended_actions: List[str]

class FreightRecommendation(BaseModel):
    recommended_carrier: str
    service_type: str
    estimated_cost_usd: float
    transit_days: int
    booking_timing: str
    risk_factors: List[str]

class MarketOpportunityReport(BaseModel):
    market_summary: str
    key_competitors: List[str]
    consumer_trends: List[str]
    recommended_entry_strategies: List[str]
    regulatory_considerations: List[str] = Field(validation_alias=AliasChoices('regulatory_considerations', 'regulatory_consultations'))
    risk_assessment: str

class ComplianceRiskReport(BaseModel):
    immediate_actions: List[str]
    medium_term_updates: List[str]
    strategic_compliance_plan: str
    risk_mitigation: str
