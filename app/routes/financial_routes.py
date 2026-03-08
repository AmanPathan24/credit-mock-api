from fastapi import APIRouter
from app.database.supabase_client import supabase

router = APIRouter()

@router.get("/financials/{cin}")
def get_financials(cin: str):

    response = supabase.table("financial_statements").select("*").eq("cin", cin).execute()

    if not response.data:
        return {
            "status": "error",
            "message": "Financial data not found"
        }

    return {
        "status": "success",
        "data": response.data
    }