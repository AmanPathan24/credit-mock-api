from fastapi import APIRouter
from app.database.supabase_client import supabase

router = APIRouter()

@router.get("/bank-summary/{cin}")
def get_bank_summary(cin: str):

    response = supabase.table("bank_summary").select("*").eq("cin", cin).execute()

    if not response.data:
        return {
            "status": "error",
            "message": "Bank data not found"
        }

    return {
        "status": "success",
        "data": response.data
    }