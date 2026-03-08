from fastapi import APIRouter
from app.database.supabase_client import supabase

router = APIRouter()

@router.get("/ratios/{cin}")
def get_ratios(cin: str):

    response = supabase.table("financial_ratios").select("*").eq("cin", cin).execute()

    if not response.data:
        return {
            "status": "error",
            "message": "Ratios not found"
        }

    return {
        "status": "success",
        "data": response.data
    }