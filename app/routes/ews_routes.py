from fastapi import APIRouter
from app.database.supabase_client import supabase

router = APIRouter()

@router.get("/ews/{cin}")
def get_ews(cin: str):

    response = supabase.table("early_warning_signals").select("*").eq("cin", cin).execute()

    if not response.data:
        return {
            "status": "error",
            "message": "EWS data not found"
        }

    return {
        "status": "success",
        "data": response.data
    }