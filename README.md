# Aura AI - Proactive Clarity & Authenticity Shield ✨🛡️

Aura AI is a dual-engine, AI-driven platform meticulously designed to elevate customer trust and confidence in online marketplaces, mirroring Amazon's commitment to customer obsession. It marks a paradigm shift from reactive defense to **proactive assurance**, enhancing the clarity of every purchase decision and securing the marketplace from sophisticated fraud. This project was developed for the **HackOn with Amazon - Season 5** competition.

---

## ▶️ Live Interactive Demo on Gitpod

Experience Aura AI in action instantly! Click the button below to launch a ready-to-use development environment on Gitpod, where you can interact with the full application in your browser.

[![Open in Gitpod](https://gitpod.io/button/open-in-gitpod.svg)](https://gitpod.io/#https://github.com/Gappu824/aura-ai-hackathon)

**Instructions for Judges:**
1.  Click the "Open in Gitpod" button above.
2.  If prompted, authorize Gitpod with your GitHub account.
3.  Gitpod will automatically spin up the environment, install dependencies, and start both the backend and frontend. This may take a few minutes for the initial setup.
4.  Once ready, a new browser tab will automatically open showing the Aura AI frontend (`http://localhost:3000`).
5.  You can then interact with the application, analyze reviews, and observe the results.

*This method demonstrates the application's full functionality and reproducibility, bypassing complexities faced during direct cloud frontend deployment within hackathon constraints.*

---

## ✨ Core Engines

Aura AI operates on two synergistic core engines, each powered by state-of-the-art AI, working in concert to provide a holistic trust ecosystem:

1.  **Clarity Engine:** Proactively prevents customer dissatisfaction and returns by surfacing AI-driven insights about product specifics (like sizing, color, and material) directly on the product page. It identifies common points of confusion before a purchase is made.
2.  **Authenticity Engine:** Employs sophisticated AI to detect and neutralize fraudulent reviews, counterfeit products, and other deceptive content with exceptional accuracy. This engine dives deep into linguistic patterns and semantic meaning to discern genuine feedback from malicious manipulation.

---

## 🚀 Architectural Overview

Aura AI is built on a professional, scalable, and resilient serverless microservices architecture, meticulously designed and deployed using AWS cloud services. This architecture ensures high availability, cost-efficiency, and alignment with Amazon's own internal engineering best practices.

* **Professional Repository Structure:** The project maintains a clean, logical, and easily navigable directory structure with distinct `backend/`, `frontend/aura-ai-ui/`, and `infrastructure/` folders, reflecting a professional engineering organization. This clarity extends to the **`README.md` itself**, which is designed for immediate understanding and navigation, serving as the front door to your project's technical story.
* **Frontend (Designed):** **Next.js (React) Application (App Router)** 🌐 designed for **Server-Side Rendered (SSR) and deployment on AWS Lambda with API Gateway**. This architecture aims for a high-performance user experience, handles complex routing, and enables direct API proxying to bypass external CORS complexities. *While the backend is fully deployed, the full cloud deployment of the frontend remains an active development challenge.*
* **API Gateway (Frontend - Designed):** **AWS API Gateway (REST API)** 🔗 designed to act as the public entry point for the frontend application.
* **Backend (Deployed & Robust):** **AWS Lambda function** 💻 executing a **FastAPI** Python application. Lambda provides serverless compute, auto-scaling, and cost-efficiency.
    * **Lambda Deployment:** The FastAPI application is deployed as a **Docker container image** 🐳 to AWS Lambda, ensuring a consistent and isolated environment.
    * **CORS Handling:** The FastAPI application within this Lambda explicitly manages CORS headers, ensuring proper communication with the Next.js frontend server.
* **API Gateway (Backend - Deployed & Robust):** **AWS API Gateway (REST API)** ⚙️ acts as a dedicated public entry point for the backend Lambda. This API Gateway is directly targeted by the Next.js frontend's internal proxying (rewrites). It is configured with **built-in CORS headers** handled by the API Gateway itself for robustness.
* **AI/ML:**
    * **Clarity Engine:** Leverages a powerful, pre-trained **Amazon Titan Text Express v1 LLM** via **Amazon Bedrock** 🧠.
    * **Authenticity Engine (Advanced):** Utilizes a powerful, pre-trained **Anthropic Claude v2.1 (or Sonnet 4) LLM** via **Amazon Bedrock** ✨.
* **Infrastructure as Code (IaC):** The entire AWS infrastructure (Lambdas, API Gateways, IAM Roles, ECR) is defined and managed using the **AWS Cloud Development Kit (CDK)** 🏗️ in Python, ensuring repeatable, auditable, and version-controlled deployments.

![Screenshot 2025-06-22 171414](https://github.com/user-attachments/assets/24949b52-6fc4-4042-bff8-71f0db4d8587)

---

## 💡 Winning Strategy & Amazon Alignment

Our solution's strength for the Amazon Hackathon lies not just in its functionality but in its profound alignment with Amazon's Leadership Principles and engineering philosophy:

1.  **Customer Obsession:** 💖
    * **Proactive Clarity:** The Clarity Engine directly addresses customer pain points by preventing confusion and returns, enhancing the pre-purchase experience.
    * **Trust Through Transparency:** The Authenticity Engine doesn't just give a score; it leverages state-of-the-art AI (Anthropic Claude) to deeply understand reviews, and in a production scenario, could provide explainable insights on *why* a review is deemed authentic or fake.

2.  **Invent and Simplify:** 🛠️
    * **Dual-Engine Innovation:** Our dual-engine approach is a novel invention, holistically tackling both clarity and authenticity for a more comprehensive trust signal.
    * **Strategic AI Pivot (Backend):** We demonstrated mature engineering judgment by initially exploring custom SageMaker models, but strategically **pivoted to leveraging powerful pre-trained Large Language Models (LLMs) on Bedrock**. This choice was made due to Bedrock's inherent capabilities in handling nuanced, complex language understanding with limited custom data, showcasing a pragmatic approach to selecting the *right tool for the job*—an optimal balance of accuracy, cost, and speed. We utilize **Few-Shot Chain-of-Thought Reasoning** with Bedrock for advanced in-context learning.
    * **Robust Frontend Deployment (Addressing Complexities):** Our development journey involved iterative exploration of frontend hosting solutions (Amplify, S3/CloudFront static hosting, App Runner). In the face of persistent configuration complexities, we strategically pivoted to a **server-side rendered (SSR) Next.js application designed for deployment directly on AWS Lambda with API Gateway**. This approach provided the most robust solution by aiming for:
        * Elimination of CORS issues through same-origin proxying via Next.js rewrites.
        * Reliable environment variable injection at runtime.
        * Leveraging a standard and well-supported Next.js deployment pattern on AWS.
        This iterative problem-solving and adaptation in the face of technical roadblocks demonstrates strong **Bias for Action** and **Ownership** to deliver a working, high-quality solution by adapting to technical roadblocks.

3.  **Earn Trust:** ✅
    * **Clean Git History:** The development process is underpinned by a clean Git history, with descriptive commit messages (e.g., "feat(frontend): Implement SSR on Lambda" or "fix(backend): Resolve CORS TypeError in app.py"). This tells a clear story of methodical development, problem-solving, and continuous improvement, crucial for building trust in the engineering process.
    * **Complete and Well-Commented Documentation:** Critical project files (like `Dockerfile`s, `requirements.txt`) are well-commented and self-explanatory. This ensures maintainability and transparency.
    * **Robustness against Manipulation:** Our Authenticity Engine is driven by meticulous **prompt engineering** leveraging an **edge-case-ready dataset** that includes sarcasm, low-effort authenticity, irrelevant details, contradictory sentiment, and sophisticated fakes. This approach, powered by Claude's advanced reasoning, prepares the model for real-world adversarial attacks, fostering genuine trust in the review ecosystem.
    * **Advanced Prompt Engineering & LLM Leverage:** We showcase production-grade practices by demonstrating how to effectively guide powerful LLMs with detailed prompts to solve specific, complex classification tasks. This highlights leveraging managed AI services for robust and efficient solutions ready for Amazon's operational scale.

4.  **Think Big & Frugality:** 💰
    * **Foundational AI:** The chosen Bedrock LLMs can be adapted for future high-value features (e.g., semantic search, review clustering, outlier detection) by modifying prompts, demonstrating inherent scalability without complex retraining pipelines.
    * **Cost-Efficiency:** Our architecture leverages serverless Lambda functions and cost-effective Bedrock inferencing, reflecting a deep understanding of AWS cost optimization by consuming pre-trained model capacity.

---

## 🛠️ Getting Started

Follow these steps to set up and run the Aura AI project.

### Prerequisites

Ensure you have the following installed on your local machine:

* **Node.js (18.x or later) & npm (or yarn)**
* **Python (3.9)**
* **AWS CLI v2:** Configured with credentials for an AWS account where you have permissions to:
    * Create and manage IAM Users/Roles, Lambda Functions, API Gateway (REST API).
    * **Access Amazon Bedrock models** (specifically `amazon.titan-text-express-v1` and `anthropic.claude-v2:1` or `anthropic.claude-3-sonnet-20240229-v1:0`).
    * Access Amazon ECR (for pushing and pulling Docker images for backend Lambda).
* **AWS CDK CLI:** Install globally: `npm install -g aws-cdk`
* **Docker Desktop:** Must be installed and running, as CDK uses it to build Backend Lambda function image.

### Installation & Setup

1.  **Clone the Repository:**
    ```bash
    git clone [https://github.com/your-username/your-repo-name.git](https://github.com/your-username/your-repo-name.git) # Replace with your actual repo URL
    cd aura-ai # Navigate to your project root
    ```

2.  **Backend Setup (Fully Deployed):**
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
    * **Build Backend Docker Image:**
        ```bash
        docker build -t aura-ai-backend:latest . # Build the Docker image for your backend Lambda
        ```
        *This image will be used by CDK for deployment to Lambda.*

3.  **Frontend Setup (Local Development):**
    * Navigate to the frontend directory:
        ```bash
        cd ../frontend/aura-ai-ui # Assuming this is your Next.js project root
        ```
    * Install frontend dependencies:
        ```bash
        npm install # or yarn install
        ```
    * **Prepare Frontend for Local Dev:**
        * **Ensure `next.config.mjs` is correctly configured for `output: 'standalone'` and `rewrites`** pointing to `process.env.BACKEND_API_URL`.
        * **Ensure `package.json` `start` script is `next start`.**
        * **Ensure all `fetch` calls in `app/page.tsx` (and other frontend components) are relative paths** (e.g., `/api/v1/generate_clarity_alert`).
        * **Run Local Next.js Build:** This step generates the `.next/standalone` folder which CDK will deploy.
            ```bash
            npm run build # This command MUST succeed locally and generate .next/standalone
            ```
            * **Troubleshooting:** If `npm run build` fails, debug it locally until it passes. This includes verifying `npm install`, `postcss.config.mjs` (for `@tailwindcss/postcss`), and `next.config.mjs` (for `BACKEND_API_URL` during build).

4.  **AWS CDK Infrastructure Deployment (Deploying/Updating Backend):**
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
    * **Deploy the Backend API Gateway and Lambda:**
        * **This will create/update your REST API Backend and its associated Lambda.**
            ```bash
            cdk deploy AuraAiStack-Dev # Use the existing stack name
            ```
        * Confirm IAM changes when prompted (`y`).
        * Upon successful completion, the terminal will output your live **`BackendApiUrl`**. **Copy this URL.**

---

## 📄 API Reference

Your deployed **Backend API** exposes the following REST API endpoints. The frontend application, once fully deployed, will consume these endpoints.

* **Backend API Base URL:** `https://YOUR_BACKEND_API_URL/` (e.g., `https://gpx4vdaiq6.execute-api.us-east-1.amazonaws.com/prod/`)

### `POST /api/v1/generate_clarity_alert`

* **Purpose:** Analyzes a collection of customer reviews to identify common themes of confusion or mismatched expectations, generating a concise clarity alert.
* **Endpoint:** Accessed via `https://YOUR_BACKEND_API_URL/api/v1/generate_clarity_alert`
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
* **Endpoint:** Accessed via `https://YOUR_BACKEND_API_URL/api/v1/analyze_review_authenticity`
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
    * Navigate to your frontend root directory: `cd frontend/aura-ai-ui`
    * **Temporary Local `.env.local` for Dev:** Create or update `.env.local` with your local backend URL:
        ```
        NEXT_PUBLIC_API_URL=[http://127.0.0.1:8000/](http://127.0.0.1:8000/)
        ```
    * Run Next.js development server: `npm run dev`
    * Open `http://localhost:3000` in your browser.

## ✅ Final Verification (Backend)

*Since the full frontend cloud deployment is an ongoing challenge, this section focuses on verifying the backend service functionality.*

1.  **Access the Deployed Backend API:** Use the `BackendApiUrl` provided by your `cdk deploy` output.
2.  **Test Backend API with `curl` (Recommended):**
    * Open your terminal.
    * Use `curl` commands to test your API endpoints. For example:
        ```bash
        curl -X POST -H "Content-Type: application/json" -d "{\"review_text\": \"This product is great! I highly recommend it.\"}" https://YOUR_BACKEND_API_URL/api/v1/analyze_review_authenticity
        ```
        *(Replace `YOUR_BACKEND_API_URL` with your actual URL)*
    * **Expected Results:** You should receive valid JSON responses (authenticity score/reasoning, or clarity alert). **CORS errors should be absent in the `curl` response.**

3.  **Monitor CloudWatch Logs:**
    * Simultaneously, open your AWS CloudWatch console.
    * Navigate to **Log groups**.
    * Find the log group for your backend Lambda (`/aws/lambda/AuraApiFunction...`).
    * Open the latest log streams and observe new entries as you interact with the frontend. This confirms Lambda invocations and allows you to debug any runtime errors.

## 📈 Future Enhancements (Full Frontend Deployment as a Primary Goal)

This project demonstrates a robust, production-ready foundation for AI-powered trust in e-commerce. Building upon this, the **immediate next phase of development will focus on the full cloud deployment of the Next.js frontend**, transforming it into a complete, end-to-end web application accessible via a single URL. This involves overcoming several critical challenges encountered during the hackathon development:

* **Finalizing Frontend Cloud Deployment:** This is the primary objective. The strategy involves deploying the **Next.js SSR application directly on AWS Lambda with API Gateway** (`FrontendAppGateway`). This approach is designed to eliminate CORS issues by leveraging Next.js's native ability to proxy API calls from the same origin, and to handle environment variable injection at runtime robustly.
    * **Lessons Learned:** This journey has provided invaluable insights into the complexities of deploying Next.js App Router applications in managed AWS environments, specifically identifying nuanced issues with `npm run build` behavior within Docker, persistent environment variable caching, and intricate CORS configurations across various services (Amplify, S3/CloudFront, App Runner). The iterative debugging has underscored the importance of meticulous environment isolation and direct manipulation of compiled assets when standard methods prove insufficient.

* **V2 Roadmap - Specialized Model Fine-Tuning:** The future vision includes a plan to collect a large-scale, human-verified dataset of reviews. With such a robust asset, a custom MLOps pipeline leveraging **Amazon SageMaker** can be utilized to train highly optimized, cost-effective, and specialized models for the Authenticity Engine, potentially surpassing the performance of general-purpose LLMs for specific, high-volume tasks.
* **Multi-Modal Authenticity:** Integrate image forensics (e.g., using Amazon Rekognition or custom models on SageMaker) to analyze product images for manipulation.
* **Advanced Fraud Detection:** Implement Graph Neural Networks (GNNs) for collusion detection (seller-reviewer networks) and temporal anomaly detection on data (e.g., in DynamoDB).
* **Human-in-the-Loop Feedback System:** Develop a multi-tiered resolution system for reported issues, empowering human investigators with AI-assisted insights and providing feedback for LLM refinement.
* **Community Rewards Program:** Build out a gamified system to incentivize accurate review reporting.
* **User Authentication & Personalization:** Secure the application and tailor experiences based on user profiles.

---

## 👥 Team & Acknowledgements

* **Team Name:** Hustlers
* **Team Members:** Kumud Agrawal (Team Captain), Gourav Mittal
* **Acknowledgements:** Special thanks to Amazon Bedrock and AWS Lambda, API Gateway for providing the powerful and scalable services that enabled this project.




