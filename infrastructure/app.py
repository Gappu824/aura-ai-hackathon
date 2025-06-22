#!/usr/bin/env python3
import os

import aws_cdk
from aws_cdk import (
    App,
    Stack,
    CfnOutput,
    Duration,
)
# Corrected APIGW V1 (REST API Gateway) import
from aws_cdk import aws_apigateway as apigw
from aws_cdk.aws_lambda import (
    DockerImageCode,
    DockerImageFunction,
    Function, # Used for the frontend lambda
    Code,     # Used for the frontend lambda
    Runtime,  # Used for the frontend lambda
)
from aws_cdk import aws_iam as iam

class AuraAiStack(Stack): # Keep your existing stack definition
    def __init__(self, scope: App, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # --- 1. Backend Lambda & REST API Gateway Definition ---
        # This part defines your FastAPI backend Lambda and its REST API Gateway.
        backend_lambda = DockerImageFunction(
            self, "AuraApiFunction", # Logical ID for backend Lambda
            code=DockerImageCode.from_image_asset(directory="../backend"),
            timeout=Duration.seconds(60), # Generous timeout for LLM inference
            memory_size=2048 # Generous memory for LLM inference
        )

        # Grant Bedrock permissions to the Backend Lambda's execution role
        backend_lambda.add_to_role_policy(iam.PolicyStatement(
            actions=["bedrock:InvokeModel"],
            resources=["*"]
        ))

        # This is the REST API Gateway for your backend Lambda.
        # It has default CORS preflight options enabled (allowing all origins/methods).
        backend_rest_api = apigw.LambdaRestApi(
            self, "AuraBackendRestApi", # Logical ID for backend REST API Gateway
            handler=backend_lambda,
            proxy=True, # Proxy all requests to the Lambda
            default_cors_preflight_options=apigw.CorsOptions( # Built-in CORS
                allow_origins=apigw.Cors.ALL_ORIGINS,
                allow_methods=apigw.Cors.ALL_METHODS,
                allow_headers=apigw.Cors.DEFAULT_HEADERS,
                max_age=Duration.days(1),
            )
        )
        CfnOutput(self, "BackendApiUrl", value=backend_rest_api.url)
        # --- END Backend Definition ---


        # --- 2. Frontend Next.js SSR on Lambda (Frontend Application) ---
        # This section defines the Lambda and API Gateway for your Next.js frontend.

        # 1. Next.js Frontend Lambda Function
        # This lambda will run the Next.js server.
        # Code comes from the locally built .next/standalone directory.
        frontend_nextjs_lambda = Function(
            self, "AuraFrontendNextJsFunction", # Logical ID for frontend Lambda
            runtime=Runtime.NODEJS_18_X, # Use Node.js runtime for Next.js
            handler="server.js", # Standard handler for Next.js standalone output
            # CRITICAL: Path to the locally built .next/standalone folder
            code=Code.from_asset("../frontend/aura-ai-ui/.next/standalone"),
            memory_size=1024, # Adjust based on your Next.js app's needs
            timeout=Duration.seconds(30), # Standard for web app serving
            # Pass the actual Backend API URL to the Next.js server via environment variable
            environment={
                "BACKEND_API_URL": backend_rest_api.url # Pass backend API URL to Next.js server
            }
        )

        # 2. API Gateway for Frontend (main application URL)
        # This will be your primary application URL that users access.
        # This is also a REST API Gateway for consistent behavior.
        frontend_app_gateway = apigw.LambdaRestApi(
            self, "AuraFrontendAppGateway", # Logical ID for frontend API Gateway
            handler=frontend_nextjs_lambda,
            proxy=True, # Proxy all requests to the frontend Next.js Lambda
            # CORS is not needed here, as the browser requests are handled by this same origin.
            # All traffic originates from frontend_app_gateway domain.
        )

        CfnOutput(self, "FrontendAppUrl", value=frontend_app_gateway.url)
        # --- END NEW: Frontend Next.js SSR on Lambda ---

app = App()
AuraAiStack(app, "AuraAiStack-Dev", # Keep this stack name
    env=aws_cdk.Environment(account=os.getenv('CDK_DEFAULT_ACCOUNT'), region=os.getenv('CDK_DEFAULT_REGION')),
)
app.synth()