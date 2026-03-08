from fastapi import APIRouter
from app.database.supabase_client import supabase

router = APIRouter()

@router.get("/fraud-indicators/{cin}")
def get_fraud_indicators(cin: str):

    response = supabase.table("fraud_indicators").select("*").eq("cin", cin).execute()

    if not response.data:
        return {
            "status": "error",
            "message": "Fraud indicators not found"
        }

    return {
        "status": "success",
        "data": response.data
    }