from app.main import app  # Imports the FastAPI 'app' instance
from mangum import Mangum

# Mangum is the bridge between the AWS Lambda event and our FastAPI app.
# The 'handler' is the object that AWS Lambda will invoke.
handler = Mangum(app)