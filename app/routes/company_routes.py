from fastapi import APIRouter
from app.database.supabase_client import supabase

router = APIRouter()

@router.get("/company/{cin}")
def get_company(cin: str):

    response = supabase.table("companies").select("*").eq("cin", cin).execute()

    if not response.data:
        return {
            "status": "error",
            "message": "Company not found"
        }

    return {
        "status": "success",
        "data": response.data[0]
    }