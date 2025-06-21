# Aura AI - Proactive Clarity & Authenticity Shield ✨🛡️

Aura AI is a dual-engine, AI-driven platform meticulously designed to elevate customer trust and confidence in online marketplaces, mirroring Amazon's commitment to customer obsession. It marks a paradigm shift from reactive defense to **proactive assurance**, enhancing the clarity of every purchase decision and securing the marketplace from sophisticated fraud. This project was developed for the **HackOn with Amazon - Season 5** competition.

---

## 🚀 Architectural Overview

Aura AI is built on a professional, scalable, and resilient serverless microservices architecture, meticulously designed and deployed using AWS cloud services. This architecture ensures high availability, cost-efficiency, and alignment with Amazon's own internal engineering best practices.

* **Frontend:** **Next.js (React) Application (App Router)** 🌐 for a high-performance, server-rendered user experience, ensuring fast loading times and optimal SEO.
* **API Gateway:** **AWS HTTP API (API Gateway v2)** 🔗 acts as the single, public entry point for all frontend requests, providing centralized request handling, routing, and robust CORS management.
* **Backend:** **AWS Lambda function** 💻 executing a **FastAPI** Python application. Lambda provides serverless compute, auto-scaling, and cost-efficiency.
    * **Lambda Deployment:** The FastAPI application is deployed as a **Docker container image** 🐳 to AWS Lambda, ensuring a consistent and isolated environment with all necessary Python dependencies (like `boto3`, `mangum`) bundled inside.
* **AI/ML:**
    * **Clarity Engine:** Leverages a powerful, pre-trained **Amazon Titan Text Express v1 LLM** via **Amazon Bedrock** 🧠. This provides rapid prototyping and effective summarization of common confusions.
    * **Authenticity Engine (Advanced):** Utilizes a powerful, pre-trained **Anthropic Claude v2.1 (or Sonnet 4) LLM** via **Amazon Bedrock** ✨. This provides superior accuracy for nuanced review authenticity classification, particularly for challenging edge cases, by leveraging sophisticated prompt engineering and in-context learning.
* **Infrastructure as Code (IaC):** The entire AWS infrastructure (Lambda, API Gateway, IAM Roles, ECR) is defined and managed using the **AWS Cloud Development Kit (CDK)** 🏗️ in Python, ensuring repeatable, auditable, and version-controlled deployments.

<!-- Optional: You might place a simple architecture diagram here, e.g., an SVG or a link to a diagram. -->

---

## 💡 Winning Strategy & Amazon Alignment

Our solution's strength for the Amazon Hackathon lies not just in its functionality but in its profound alignment with Amazon's Leadership Principles and engineering philosophy:

1.  **Customer Obsession:** 💖
    * **Proactive Clarity:** The Clarity Engine directly addresses customer pain points by preventing confusion and returns, enhancing the pre-purchase experience.
    * **Trust Through Transparency:** The Authenticity Engine doesn't just give a score; it leverages state-of-the-art AI (Anthropic Claude) to deeply understand reviews, and in a production scenario, could provide explainable insights on *why* a review is deemed authentic or fake.

2.  **Invent and Simplify:** 🛠️
    * **Dual-Engine Innovation:** Our dual-engine approach is a novel invention, holistically tackling both clarity and authenticity for a more comprehensive trust signal.
    * **Strategic AI Pivot:** We demonstrated mature engineering judgment by initially exploring custom SageMaker models, but strategically **pivoted to leveraging powerful pre-trained Large Language Models (LLMs) on Bedrock**. This choice was made due to Bedrock's inherent capabilities in handling nuanced, complex language understanding with limited custom data, showcasing a pragmatic approach to selecting the *right tool for the job*—an optimal balance of accuracy, cost, and speed. We utilize **Few-Shot Chain-of-Thought Reasoning** with Bedrock for advanced in-context learning.

3.  **Earn Trust:** ✅
    * **Robustness against Manipulation:** Our Authenticity Engine is driven by meticulous **prompt engineering** leveraging an **edge-case-ready dataset** that includes sarcasm, low-effort authenticity, irrelevant details, contradictory sentiment, and sophisticated fakes. This approach, powered by Claude's advanced reasoning, prepares the model for real-world adversarial attacks, fostering genuine trust in the review ecosystem.
    * **Advanced Prompt Engineering & LLM Leverage:** We showcase production-grade practices by demonstrating how to effectively guide powerful LLMs with detailed prompts to solve specific, complex classification tasks. This highlights leveraging managed AI services for robust and efficient solutions ready for Amazon's operational scale.

4.  **Think Big & Frugality:** 💰
    * **Foundational AI:** The chosen Bedrock LLMs can be adapted for future high-value features (e.g., semantic search, review clustering, outlier detection) by modifying prompts, demonstrating inherent scalability without complex retraining pipelines.
    * **Cost-Efficiency:** Our architecture leverages serverless Lambda and cost-effective Bedrock inferencing, reflecting a deep understanding of AWS cost optimization by consuming pre-trained model capacity.

---

## 🛠️ Getting Started

Follow these steps to set up and run the Aura AI project.

### Prerequisites

Ensure you have the following installed on your local machine:

* **Node.js (18.x or later) & npm (or yarn)**
* **Python (3.9)**
* **AWS CLI v2:** Configured with credentials for an AWS account where you have permissions to:
    * Create and manage IAM Users/Roles, S3 Buckets, Lambda Functions, API Gateway (HTTP API).
    * **Access Amazon Bedrock models** (specifically `amazon.titan-text-express-v1` and `anthropic.claude-v2:1` or `anthropic.claude-3-sonnet-20240229-v1:0`).
    * Access Amazon ECR (for pushing and pulling Docker images).
* **AWS CDK CLI:** Install globally: `npm install -g aws-cdk`
* **Docker Desktop:** Must be installed and running, as CDK uses it to build Lambda function images.

### Installation & Setup

1.  **Clone the Repository:**
    ```bash
    git clone [https://github.com/your-username/your-repo-name.git](https://github.com/your-username/your-repo-name.git) # Replace with your actual repo URL
    cd aura-ai # Navigate to your project root
    ```

2.  **Backend Setup:**
    * Navigate to the backend directory:
        ```bash
        cd backend
        ```
    * Create and activate a Python virtual environment:
        ```bash
        python -m venv venv
        .\venv\Scripts\activate   # For Windows PowerShell
        # Or: source venv/bin/activate  # For macOS/Linux Bash/Zsh
        ```
    * Install backend dependencies:
        ```bash
        pip install -r requirements.txt
        ```

3.  **Frontend Setup:**
    * Navigate to the frontend directory (assuming your Next.js project is directly in `frontend/`):
        ```bash
        cd ../frontend
        ```
    * Install frontend dependencies:
        ```bash
        npm install # or yarn install
        ```

4.  **AWS CDK Infrastructure Deployment (Backend Cloud Resources):**
    * Navigate to the infrastructure directory:
        ```bash
        cd ../infrastructure
        ```
    * Install CDK dependencies:
        ```bash
        npm install
        ```
    * Bootstrap your AWS environment (one-time per account/region):
        ```bash
        cdk bootstrap aws://YOUR_AWS_ACCOUNT_ID/YOUR_AWS_REGION # e.g., aws://123456789012/us-east-1
        ```
        * **Important:** Replace `YOUR_AWS_ACCOUNT_ID` and `YOUR_AWS_REGION`.
    * **Deploy the Backend API and Lambda:**
        * Run the deployment command (no SageMaker endpoint context needed anymore):
            ```bash
            cdk deploy
            ```
        * Confirm IAM changes when prompted (`y`).
        * Upon successful completion, the terminal will output your live **API Gateway URL (ApiUrl)**. **Copy this URL.**

5.  **Frontend Deployment (AWS Amplify Console Recommended):**
    * **Push your frontend code to a Git repository** (if not already).
    * **Navigate to AWS Amplify Console** in the AWS Management Console.
    * **Connect New App:** Choose your Git provider, select your repository and the appropriate branch (e.g., `main`).
    * **Configure Build Settings:** Amplify should auto-detect Next.js.
        * **Set Environment Variable:** In the "Environment variables" section, add:
            * **Key:** `NEXT_PUBLIC_API_URL`
            * **Value:** Paste the **API Gateway URL** you copied from the `cdk deploy` output.
    * **Save and Deploy.** Monitor the build and deployment process in Amplify.
    * Once successful, Amplify will provide the live URL for your frontend application.

---

## 📄 API Reference

Your deployed application exposes the following REST API endpoints:

### `POST /api/v1/generate_clarity_alert`

* **Purpose:** Analyzes a collection of customer reviews to identify common themes of confusion or mismatched expectations, generating a concise clarity alert.
* **Request Body (`application/json`):**
    ```json
    {
      "reviews": [
        "The shirt runs really small, definitely order a size up.",
        "Warning: size is way off! I'd recommend sizing up at least one size.",
        "Love the color! Fabric is a bit thin. Sizing is a real issue, too tight.",
        "Not sure what others are talking about, perfect fit and great quality.",
        "Had to send it back, it was too tight. Order a size up."
      ]
    }
    ```
* **Response Body (Success - `200 OK` - `application/json`):**
    ```json
    {
      "clarity_alert": "Customers suggest ordering a size up for the best fit."
    }
    ```
* **Response Body (No Alert - `200 OK` - `application/json`):**
    ```json
    {
      "clarity_alert": null
    }
    ```
* **Response Body (Error - `500 Internal Server Error` - `application/json`):**
    ```json
    {
      "detail": "Error message details from the backend."
    }
    ```

### `POST /api/v1/analyze_review_authenticity`

* **Purpose:** Analyzes a single customer review for authenticity signals using an advanced AI model (Anthropic Claude), providing a score and detailed reasoning.
* **Request Body (`application/json`):**
    ```json
    {
      "review_text": "This product is truly incredible. Amazing quality and value. Best purchase ever."
    }
    ```
* **Response Body (Success - `200 OK` - `application/json`):**
    ```json
    {
      "authenticity_score": 0.15,
      "reasoning": "Generic praise, extremely short, and completely lacks specific details about product features or user experience, strongly indicative of inauthenticity."
    }
    ```
* **Response Body (Error - `500 Internal Server Error` - `application/json`):**
    ```json
    {
      "detail": "Error message details from the backend."
    }
    ```

## 💻 How to Run Locally

For local development and testing:

1.  **Start Backend (FastAPI):**
    * Navigate to `backend/app` directory: `cd backend/app`
    * Activate virtual environment: `.\venv\Scripts\activate` (Windows) or `source venv/bin/activate` (Linux/macOS)
    * Run Uvicorn server: `uvicorn main:app --reload`
    * The API will be available at `http://127.0.0.1:8000`.

2.  **Start Frontend (Next.js):**
    * Navigate to your frontend root directory: `cd frontend` (or `cd .` if already in project root).
    * Ensure your `NEXT_PUBLIC_API_URL` in `.env.local` is set to `http://127.0.0.1:8000`.
    * Run Next.js development server: `npm run dev`
    * Open `http://localhost:3000` in your browser.

## ✅ Final Verification (Post-Deployment)

Once both your backend (Lambda/API Gateway) and frontend (Next.js on Amplify) are deployed:

1.  **Access the Deployed Frontend:** Open the live URL provided by AWS Amplify Console in your browser.

2.  **Full Functional Test:**
    * **User Input Section:** Test with a variety of reviews (generic positive, sarcastic, detailed negative, etc.) in the input box. Verify the authenticity score, reasoning, and clarity alerts.
    * **Pre-defined Examples:** Test the "Analyze Authenticity" buttons for the mock reviews.
    * **Expected Results:** The Authenticity Engine (powered by your **Anthropic Claude LLM**) should provide high-confidence, accurate scores and reasoning for all the edge cases we've meticulously covered. The Clarity Engine (Bedrock) should also function correctly.

3.  **Monitor CloudWatch Logs:**
    * Simultaneously, open your AWS CloudWatch console.
    * Navigate to **Log groups**.
    * Find the log group for your Lambda function (`/aws/lambda/AuraAiStack-Dev-AuraApiFunction...`).
    * Open the latest log stream and observe new entries as you interact with the frontend. This confirms Lambda invocations and allows you to debug any runtime errors.

## 📈 Future Enhancements

* **Robust Data Collection & MLOps Pipelines:** Implement automated pipelines for continuous collection, labeling, and re-training/re-prompting of LLMs to combat model drift and adapt to new deceptive patterns.

* **V2 Roadmap - Specialized Model Fine-Tuning:** The future vision includes a plan to collect a large-scale, human-verified dataset of reviews. With such a robust asset, a custom MLOps pipeline leveraging **Amazon SageMaker** can be utilized to train highly optimized, cost-effective, and specialized models for the Authenticity Engine, potentially surpassing the performance of general-purpose LLMs for specific, high-volume tasks.

* **Multi-Modal Authenticity:** Integrate image forensics (e.g., using Amazon Rekognition or custom models on SageMaker) to analyze product images for manipulation.

* **Advanced Fraud Detection:** Implement Graph Neural Networks (GNNs) for collusion detection (seller-reviewer networks) and temporal anomaly detection on data (e.g., in DynamoDB).

* **Human-in-the-Loop Feedback System:** Develop a multi-tiered resolution system for reported issues, empowering human investigators with AI-assisted insights and providing feedback for LLM refinement.

* **Community Rewards Program:** Build out a gamified system to incentivize accurate review reporting.

* **User Authentication & Personalization:** Secure the application and tailor experiences based on user profiles.

## 👥 Team & Acknowledgements

* **Team Name:**  Hustlers
* **Team Members:**  Kumud Agrawal(Team Captain), Gourav Mittal
* **Acknowledgements:** Special thanks to Amazon Bedrock and AWS Lambda, API Gateway, and Amplify Console for providing the powerful and scalable services that enabled this project.
