from fastapi import APIRouter
from app.database.supabase_client import supabase

router = APIRouter()

@router.get("/gst/{cin}")
def get_gst(cin: str):

    response = supabase.table("gst_filings").select("*").eq("cin", cin).execute()

    if not response.data:
        return {
            "status": "error",
            "message": "GST data not found"
        }

    return {
        "status": "success",
        "data": response.data
    }