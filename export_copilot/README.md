Export Co-Pilot 🚀
Transforming global trade for small businesses with an AI-powered team of export specialists.

Export Co-Pilot is a demo-ready application built on IBM watsonx that leverages a multi-agent AI framework to automate and de-risk the entire export workflow. It's designed to give small and medium-sized enterprises (SMEs) the intelligence and capabilities of a large corporate trade department, without the overhead.


(Click to watch the 3-minute demo)
https://youtu.be/vCPWml5_HM8

The Problem
Exporting is a high-stakes, manual process filled with risks:

Complex Paperwork: A single error in documentation can trap shipments in customs for weeks.

Confusing Regulations: Navigating customs codes (HS Codes) and international compliance is a specialized skill.

Market Uncertainty: Businesses often enter new markets with incomplete data, leading to costly guesswork.

Constant Change: Trade policies and regulations are constantly shifting, making it nearly impossible for SMEs to stay compliant.

The Solution: An Agentic AI Framework
Export Co-Pilot solves this by deploying a team of specialized AI agents that work together to manage the export process. Instead of one AI, we have a team of experts, each powered by IBM watsonx.

Our Team of AI Agents:
Document Validator Agent: The meticulous compliance officer. It validates documents for consistency and completeness.

Company Profile Agent: The business analyst. It synthesizes documents into a profile to provide context for other agents.

Trade Classification Agent: The customs expert. It instantly determines the correct HS code, customs duty, and required documentation.

Freight Rate Analyzer Agent: The logistics specialist. It analyzes live market data to find the most efficient and cost-effective shipping options.

Market Intelligence Agent: The market entry strategist. It generates a full report on competitors, consumer trends, and entry strategies for a target country.

Compliance Risk Monitor Agent: The proactive risk manager. It constantly scans for global regulatory changes and provides actionable alerts to ensure compliance.

Technology Stack
AI Engine: IBM watsonx (ibm/granite-3-3-8b-instruct model)

Framework: LangChain for agent orchestration

Application UI: Gradio

Core Language: Python

Tooling: DuckDuckGo for live web searches, Tesseract for OCR

Setup & Installation
Prerequisites:

Python 3.9+

Tesseract OCR Engine.

On Debian/Ubuntu: sudo apt-get install tesseract-ocr poppler-utils

On macOS: brew install tesseract

On Windows: Download from the official Tesseract repository.

Installation Steps:

Clone the repository:

git clone <your-repo-url>
cd export-copilot

Create a virtual environment (recommended):

python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

Install dependencies:

pip install -r requirements.txt

Set up your environment variables:

Create a file named .env in the root of the project.

Add your IBM watsonx credentials to this file:

WATSONX_API_KEY="your_api_key"
WATSONX_PROJECT_ID="your_project_id"

How to Run
Execute the main application file from the root directory:

python app.py

The application will launch in a pre-populated demo mode. Open the provided URL in your browser to interact with the Export Co-Pilot.