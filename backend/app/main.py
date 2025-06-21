from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware # <-- ADD THIS LINE
from pydantic import BaseModel
from typing import List
from .services.titan_service import generate_clarity_alert
# This import is corrected based on the new service name and aliasing instruction
from .services.bedrock_service import get_authenticity_analysis as get_authenticity_score

class ClarityRequest(BaseModel):
    reviews: List[str]

class AuthenticityRequest(BaseModel):
    review_text: str

app = FastAPI()

# --- START ADDITIONS: CORS Configuration ---
origins = [
    "http://localhost:3000",  # Allow your Next.js frontend local development URL
    # When you deploy your frontend, you'll add its deployed URL here as well, e.g.:
    # "https://your-deployed-frontend-url.com",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,        # List of allowed origins
    allow_credentials=True,       # Allow cookies to be sent
    allow_methods=["*"],          # Allow all HTTP methods (GET, POST, PUT, DELETE, etc.)
    allow_headers=["*"],          # Allow all headers
)
# --- END ADDITIONS: CORS Configuration ---

@app.post("/api/v1/generate_clarity_alert")
def handle_clarity_alert(request: ClarityRequest):
    alert = generate_clarity_alert(request.reviews)
    return {"clarity_alert": alert}

@app.post("/api/v1/analyze_review_authenticity")
def handle_review_authenticity(request: AuthenticityRequest):
    # The call now directly uses the Bedrock service function.
    # No SageMaker endpoint name or environment variable check is needed here.
    analysis = get_authenticity_score(review_text=request.review_text)
    return analysis