import os
import logging
from dotenv import load_dotenv
from langchain_ibm import WatsonxLLM

# --- Local Imports ---
from utils import LLMUtils
from agents import (
    HealthCheckAgent, CompanyProfileAgent, ExportDocumentValidator,
    TradeClassificationAgent, FreightRateAnalyzer, MarketIntelligenceAgent,
    ComplianceRiskMonitor
)

load_dotenv()

# --- IBM Watsonx AI Configuration ---
WATSONX_API_KEY = os.getenv("WATSONX_API_KEY")
WATSONX_PROJECT_ID = os.getenv("WATSONX_PROJECT_ID")
WATSONX_URL = "https://us-south.ml.cloud.ibm.com"

if not WATSONX_API_KEY or not WATSONX_PROJECT_ID:
    logging.error("🛑 Watsonx credentials not set. Please create a .env file.")
    WATSONX_CREDENTIALS_SET = False
else:
    WATSONX_CREDENTIALS_SET = True
    logging.info("✅ Watsonx credentials loaded successfully.")

# --- Model Configuration ---
LLM_MODEL_ID = "ibm/granite-3-3-8b-instruct"
EMBEDDING_MODEL = "all-MiniLM-L6-v2"

def setup_agents():
    """Initializes and returns all agent instances."""
    if not WATSONX_CREDENTIALS_SET:
        return None, None, None, None, None, None, None

    llm = WatsonxLLM(
        model_id=LLM_MODEL_ID, url=WATSONX_URL, project_id=WATSONX_PROJECT_ID,
        apikey=WATSONX_API_KEY, params={"decoding_method": "greedy", "max_new_tokens": 4096, "temperature": 0.0}
    )
    llm_utils = LLMUtils(llm)

    health_agent = HealthCheckAgent(llm_utils)
    agent0 = CompanyProfileAgent(llm_utils)
    agent1 = ExportDocumentValidator(llm_utils)
    agent2 = TradeClassificationAgent(llm_utils)
    agent3 = FreightRateAnalyzer(llm_utils)
    agent4 = MarketIntelligenceAgent(llm_utils)
    agent5 = ComplianceRiskMonitor(llm_utils)

    logging.info("✅ All agents initialized successfully.")
    return health_agent, agent0, agent1, agent2, agent3, agent4, agent5
