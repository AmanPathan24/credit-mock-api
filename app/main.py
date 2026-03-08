from fastapi import FastAPI
from app.routes import company_routes
from app.routes import bank_routes
from app.routes import ews_routes
from app.routes import finance_ratios_routes
from app.routes import financial_routes
from app.routes import fraud_routes
from app.routes import gst_routes
from app.routes import credit_routes
from app.routes import risk_routes

app = FastAPI(
    title="Corporate Credit Mock API",
    description="Mock financial data platform for AI-based credit appraisal",
    version="1.0"
)

app.include_router(company_routes.router)
app.include_router(bank_routes.router)
app.include_router(ews_routes.router)
app.include_router(finance_ratios_routes.router)
app.include_router(financial_routes.router)
app.include_router(fraud_routes.router)
app.include_router(gst_routes.router)
app.include_router(credit_routes.router)
app.include_router(risk_routes.router)

