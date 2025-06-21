#!/usr/bin/env python3
import os
from aws_cdk import (
    App,
    Stack,
    aws_apigatewayv2 as apigw2,
    aws_iam as iam,
    CfnOutput,
    Duration
)
from aws_cdk.aws_apigatewayv2_integrations import HttpLambdaIntegration
from aws_cdk.aws_lambda import DockerImageCode, DockerImageFunction

class AuraAiStack(Stack):
    def __init__(self, scope: App, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # Defines the Lambda function for our FastAPI app
        backend_lambda = DockerImageFunction(
            self, "AuraApiFunction",
            code=DockerImageCode.from_image_asset(directory="../backend"),
            timeout=Duration.seconds(30),
            memory_size=512 # No longer need a large memory footprint
        )

        # --- Simplified Permissions: Only Bedrock is needed now ---
        backend_lambda.add_to_role_policy(iam.PolicyStatement(
            actions=["bedrock:InvokeModel"],
            resources=["*"]
        ))

        # Create the HTTP API Gateway
        http_api = apigw2.HttpApi(
            self, "AuraHttpApi",
            default_integration=HttpLambdaIntegration("AuraLambdaIntegration", backend_lambda)
        )

        CfnOutput(self, "ApiUrl", value=http_api.url)

app = App()
AuraAiStack(app, "AuraAiStack-Dev")
app.synth()
