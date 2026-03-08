from fastapi import APIRouter
from app.database.supabase_client import supabase

router = APIRouter()

@router.get("/risk-summary/{cin}")
def get_risk_summary(cin: str):

    ratios = supabase.table("financial_ratios").select("*").eq("cin", cin).execute()
    fraud = supabase.table("fraud_indicators").select("*").eq("cin", cin).execute()
    ews = supabase.table("early_warning_signals").select("*").eq("cin", cin).execute()

    if not ratios.data:
        return {
            "status": "error",
            "message": "Company data not found"
        }

    r = ratios.data[0]
    f = fraud.data[0]
    e = ews.data[0]

    risk_score = 50

    if r["debt_to_equity"] > 2:
        risk_score += 10

    if f["accounting_fraud"]:
        risk_score += 20

    if f["transaction_anomalies"]:
        risk_score += 10

    if e["negative_cash_flow"]:
        risk_score += 10

    if e["revenue_decline"]:
        risk_score += 5

    return {
        "status": "success",
        "data": {
            "cin": cin,
            "risk_score": risk_score,
            "fraud_flags": f,
            "early_warning_signals": e
        }
    }