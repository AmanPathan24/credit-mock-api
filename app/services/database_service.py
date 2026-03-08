from app.database.supabase_client import supabase
from app.services.fake_data_generator import *

def insert_company(company):

    response = supabase.table("companies").insert(company).execute()

    return response.data


def insert_financials(financials):

    response = supabase.table("financial_statements").insert(financials).execute()

    return response.data


def insert_ratios(ratios):

    response = supabase.table("financial_ratios").insert(ratios).execute()

    return response.data


def insert_gst(gst):

    response = supabase.table("gst_filings").insert(gst).execute()

    return response.data


def insert_bank_summary(bank):

    response = supabase.table("bank_summary").insert(bank).execute()

    return response.data


def insert_fraud(fraud):

    response = supabase.table("fraud_indicators").insert(fraud).execute()

    return response.data


def insert_ews(ews):

    response = supabase.table("early_warning_signals").insert(ews).execute()

    return response.data

def generate_full_company_profile():

    company = generate_company()

    insert_company(company)

    financials = generate_financials(company["cin"])
    insert_financials(financials)

    ratios = generate_ratios(financials)
    insert_ratios(ratios)

    gst = generate_gst(company["cin"], financials["revenue"])
    insert_gst(gst)

    bank = generate_bank_summary(company["cin"], financials["revenue"])
    insert_bank_summary(bank)

    fraud = generate_fraud_signals(company["cin"])
    insert_fraud(fraud)

    ews = generate_ews(company["cin"])
    insert_ews(ews)

    return {
        "company": company,
        "financials": financials,
        "ratios": ratios,
        "gst": gst,
        "bank_summary": bank,
        "fraud_indicators": fraud,
        "early_warning_signals": ews
    }