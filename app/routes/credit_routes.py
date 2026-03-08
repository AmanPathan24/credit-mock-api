from fastapi import APIRouter
from app.database.supabase_client import supabase
from app.services.database_service import generate_full_company_profile
from fastapi import Query

router = APIRouter()

@router.post("/generate-company-profile")
def generate_company_profile():

    profile = generate_full_company_profile()

    return {
        "status": "success",
        "message": "Company credit profile generated",
        "data": profile
    }

@router.post("/generate-bulk-companies")
def generate_bulk_companies(n: int = Query(10, description="Number of companies to generate")):

    generated = []

    for _ in range(n):

        profile = generate_full_company_profile()

        generated.append(profile["company"]["cin"])

    return {
        "status": "success",
        "message": f"{n} companies generated",
        "generated_cins": generated
    }

@router.get("/credit-profile/{cin}")
def get_credit_profile(cin: str):

    company = supabase.table("companies").select("*").eq("cin", cin).execute()
    financials = supabase.table("financial_statements").select("*").eq("cin", cin).execute()
    ratios = supabase.table("financial_ratios").select("*").eq("cin", cin).execute()
    gst = supabase.table("gst_filings").select("*").eq("cin", cin).execute()
    bank = supabase.table("bank_summary").select("*").eq("cin", cin).execute()
    fraud = supabase.table("fraud_indicators").select("*").eq("cin", cin).execute()
    ews = supabase.table("early_warning_signals").select("*").eq("cin", cin).execute()

    if not company.data:
        return {
            "status": "error",
            "message": "Company not found"
        }

    return {
        "status": "success",
        "data": {
            "company": company.data[0],
            "financial_statements": financials.data,
            "financial_ratios": ratios.data,
            "gst_filings": gst.data,
            "bank_summary": bank.data,
            "fraud_indicators": fraud.data,
            "early_warning_signals": ews.data
        }
    }