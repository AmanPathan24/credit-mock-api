from faker import Faker
import random
import uuid
from datetime import datetime

fake = Faker()

def generate_company():

    return {
        "cin": fake.unique.bothify(text="U#####MH####PLC######"),
        "company_name": fake.company(),
        "sector": random.choice([
            "Manufacturing",
            "Pharmaceutical",
            "Automobile",
            "Textiles",
            "Infrastructure",
            "Energy",
            "Logistics"
        ]),
        "incorporation_year": random.randint(2000, 2022),
        "registered_address": fake.address(),
        "directors": [fake.name(), fake.name()],
        "promoters": [fake.name()]
    }

def generate_financials(cin):

    revenue = random.randint(50_000_000, 5_000_000_000)

    profit_margin = random.uniform(0.05, 0.2)

    net_profit = int(revenue * profit_margin)

    assets = revenue * random.uniform(1.5, 3)

    liabilities = assets * random.uniform(0.3, 0.7)

    equity = assets - liabilities

    debt = liabilities * random.uniform(0.5, 0.9)

    cash_flow = net_profit * random.uniform(0.7, 1.2)

    ebitda = revenue * random.uniform(0.15, 0.35)

    return {
        "cin": cin,
        "year": 2024,
        "revenue": int(revenue),
        "net_profit": int(net_profit),
        "total_assets": int(assets),
        "total_liabilities": int(liabilities),
        "equity": int(equity),
        "debt": int(debt),
        "cash_flow": int(cash_flow),
        "ebitda": int(ebitda)
    }

def generate_ratios(financials):

    debt_to_equity = financials["debt"] / financials["equity"]

    current_ratio = random.uniform(1.0, 2.5)

    interest_coverage = random.uniform(1.5, 6)

    profit_margin = financials["net_profit"] / financials["revenue"]

    return_on_assets = financials["net_profit"] / financials["total_assets"]

    return_on_equity = financials["net_profit"] / financials["equity"]

    return {
        "cin": financials["cin"],
        "year": financials["year"],
        "debt_to_equity": round(debt_to_equity, 2),
        "current_ratio": round(current_ratio, 2),
        "interest_coverage": round(interest_coverage, 2),
        "profit_margin": round(profit_margin, 2),
        "return_on_assets": round(return_on_assets, 2),
        "return_on_equity": round(return_on_equity, 2)
    }

def generate_gst(cin, revenue):

    sales = revenue * random.uniform(0.9, 1.1)

    tax_paid = sales * 0.18

    input_credit = tax_paid * random.uniform(0.6, 0.9)

    compliance_score = random.randint(70, 100)

    filing_delay = random.randint(0, 10)

    return {
        "cin": cin,
        "year": 2024,
        "gstr1_sales": int(sales),
        "gstr3b_tax_paid": int(tax_paid),
        "gstr2a_input_credit": int(input_credit),
        "gst_compliance_score": compliance_score,
        "gst_filing_delay": filing_delay
    }


def generate_bank_summary(cin, revenue):

    monthly_inflow = revenue / 12

    monthly_outflow = monthly_inflow * random.uniform(0.7, 0.95)

    average_balance = monthly_inflow * random.uniform(0.05, 0.15)

    overdraft = random.choice([True, False])

    repayment = random.choice([
        "clean",
        "minor delays",
        "restructured",
        "default history"
    ])

    return {
        "cin": cin,
        "monthly_inflow": int(monthly_inflow),
        "monthly_outflow": int(monthly_outflow),
        "average_balance": int(average_balance),
        "overdraft_usage": overdraft,
        "loan_repayment_history": repayment
    }

def generate_fraud_signals(cin):

    return {
        "cin": cin,
        "accounting_fraud": random.choice([True, False]),
        "regulatory_actions": random.randint(0, 3),
        "abnormal_ratios": random.choice([True, False]),
        "governance_failure": random.choice([True, False]),
        "compliance_violations": random.randint(0, 4),
        "transaction_anomalies": random.choice([True, False])
    }

def generate_ews(cin):

    return {
        "cin": cin,
        "negative_cash_flow": random.choice([True, False]),
        "revenue_decline": random.choice([True, False]),
        "rating_downgrade": random.choice([True, False]),
        "new_lawsuits": random.randint(0, 3),
        "regulatory_investigation": random.choice([True, False])
    }