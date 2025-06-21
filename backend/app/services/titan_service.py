import boto3
import json
from app.utils.prompts import CLARITY_PROMPT_TEMPLATE, AUTHENTICITY_PROMPT_TEMPLATE

# Initialize the Bedrock client
bedrock_runtime = boto3.client(service_name='bedrock-runtime', region_name='us-east-1')

def generate_clarity_alert(reviews: list) -> str:
    reviews_text = "\n".join(reviews)
    prompt = CLARITY_PROMPT_TEMPLATE.format(reviews_text=reviews_text)
    body = json.dumps({
        "inputText": prompt,
        "textGenerationConfig": {"maxTokenCount": 50, "temperature": 0}
    })
    response = bedrock_runtime.invoke_model(
        body=body, modelId='amazon.titan-text-express-v1',
        accept='application/json', contentType='application/json'
    )
    response_body = json.loads(response.get('body').read())
    alert = response_body.get('results')[0].get('outputText').strip()
    return alert if alert != "NO_ALERT" else None

def analyze_review_authenticity(review_text: str) -> dict:
    prompt = AUTHENTICITY_PROMPT_TEMPLATE.format(review_text=review_text)
    body = json.dumps({
        "inputText": prompt,
        "textGenerationConfig": {"maxTokenCount": 200, "temperature": 0.1}
    })
    response = bedrock_runtime.invoke_model(
        body=body, modelId='amazon.titan-text-express-v1',
        accept='application/json', contentType='application/json'
    )
    response_body = json.loads(response.get('body').read())
    try:
        analysis_json = response_body.get('results')[0].get('outputText').strip()
        return json.loads(analysis_json)
    except (json.JSONDecodeError, IndexError, TypeError):
        return {"error": "Failed to parse AI model response."}