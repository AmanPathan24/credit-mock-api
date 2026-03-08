# Corporate Credit Mock API

A comprehensive mock financial data platform built with FastAPI for AI-based credit appraisal systems. This API provides realistic financial data for companies including bank statements, GST returns, fraud detection, credit scores, and risk assessment.

## Features

- **Company Information**: Fetch company details using CIN (Corporate Identification Number)
- **Bank Summary**: Retrieve banking transaction summaries and account details
- **Financial Statements**: Access income statements, balance sheets, and cash flow data
- **GST Returns**: Get GST filing and return information
- **Credit Scoring**: Obtain credit scores and related metrics
- **Risk Assessment**: Evaluate business and financial risks
- **Fraud Detection**: Access fraud indicators and detection data
- **EWS (Early Warning Signals)**: Monitor early warning indicators
- **Financial Ratios**: Calculate and retrieve key financial ratios

## Technology Stack

- **Framework**: FastAPI 0.135.1
- **Database**: Supabase (PostgreSQL)
- **Data Generation**: Faker 40.8.0
- **Server**: Uvicorn
- **Language**: Python 3.x
- **Environment Management**: python-dotenv

## Project Structure

```
mock-api/
├── app/
│   ├── main.py                      # FastAPI application entry point
│   ├── database/
│   │   └── supabase_client.py       # Supabase connection configuration
│   ├── routes/
│   │   ├── bank_routes.py           # Bank summary endpoints
│   │   ├── company_routes.py        # Company information endpoints
│   │   ├── credit_routes.py         # Credit scoring endpoints
│   │   ├── ews_routes.py            # Early warning signals endpoints
│   │   ├── finance_ratios_routes.py # Financial ratios endpoints
│   │   ├── financial_routes.py      # Financial statements endpoints
│   │   ├── fraud_routes.py          # Fraud detection endpoints
│   │   ├── gst_routes.py            # GST returns endpoints
│   │   └── risk_routes.py           # Risk assessment endpoints
│   └── services/
│       ├── database_service.py      # Database operations
│       └── fake_data_generator.py   # Mock data generation utilities
├── requirements.txt                  # Project dependencies
├── Procfile                         # Deployment configuration
└── README.md                        # Project documentation
```

## 🔧 Setup Instructions

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- Supabase account and project

### Installation

1. **Clone the repository**

   ```bash
   git clone <repository-url>
   cd mock-api
   ```

2. **Create a virtual environment**

   ```bash
   python -m venv venv
   ```

3. **Activate the virtual environment**
   - Windows:
     ```bash
     venv\Scripts\activate
     ```
   - macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

4. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

5. **Configure environment variables**

   Create a `.env` file in the root directory:

   ```env
   SUPABASE_URL=your_supabase_project_url
   SUPABASE_KEY=your_supabase_anon_key
   ```

## Running the Application

### Development Mode

```bash
uvicorn app.main:app --reload
```

The API will be available at: `http://localhost:8000`

### Production Mode

```bash
uvicorn app.main:app --host 0.0.0.0 --port 8000
```

## API Documentation

Once the server is running, access the interactive API documentation:

- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

### Available Endpoints

#### Company Routes

- `GET /company/{cin}` - Get company details by CIN

#### Bank Routes

- `GET /bank-summary/{cin}` - Get bank summary for a company

#### Financial Routes

- Financial statements and related data

#### GST Routes

- GST returns and filing information

#### Credit Routes

- Credit scores and credit-related metrics

#### Risk Routes

- Risk assessment and risk indicators

#### Fraud Routes

- Fraud detection indicators and reports

#### EWS Routes

- Early warning signals for businesses

#### Financial Ratios Routes

- Key financial ratios and metrics

## Database

This project uses **Supabase** (PostgreSQL) as the database backend. Ensure you have created the following tables in your Supabase project:

- `companies` - Company master data
- `bank_summary` - Banking transaction summaries
- `financial_statements` - Income statements, balance sheets
- `gst_returns` - GST filing data
- `credit_scores` - Credit scoring information
- `risk_assessment` - Risk indicators
- `fraud_detection` - Fraud-related data
- `ews_indicators` - Early warning signals
- `financial_ratios` - Calculated financial ratios

## Deployment

This project is configured for deployment on platforms like Heroku, Render, or Railway using the `Procfile`:

```
web: uvicorn app.main:app --host 0.0.0.0 --port $PORT
```

## Testing

Test the API endpoints using:

- **Swagger UI**: Built-in interactive documentation
- **Postman**: Import the API collection
- **cURL**: Command-line testing
- **httpx/requests**: Python client libraries

Example cURL request:

```bash
curl -X GET "http://localhost:8000/company/U12345ABC2020PLC123456"
```

## Response Format

All API responses follow a consistent format:

**Success Response:**

```json
{
  "status": "success",
  "data": { ... }
}
```

**Error Response:**

```json
{
  "status": "error",
  "message": "Error description"
}
```
