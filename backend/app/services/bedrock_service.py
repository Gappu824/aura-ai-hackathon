import boto3
import json
import os
import re

# Initialize Bedrock client
bedrock_runtime = boto3.client(
    service_name='bedrock-runtime',
    region_name=os.environ.get("AWS_REGION", "us-east-1") # Ensure region is correctly configured
)

def get_authenticity_analysis(review_text: str):
    """
    Analyzes the authenticity of a review using an Amazon Bedrock LLM (Claude v2.1).

    Args:
        review_text (str): The text of the review to analyze.

    Returns:
        dict: A dictionary containing the authenticity analysis,
              including 'authenticity_score' (float) and 'reasoning' (string),
              or an 'error' message if processing fails.
    """
    # --- START MODIFICATION ---
    # Explicitly set to Claude v2.1 Model ID
    model_id = 'anthropic.claude-v2:1' # Changed model ID to anthropic.claude-v2:1
    # --- END MODIFICATION ---

    # The prompt's core instruction emphasizes understanding nuances and specific patterns.
    # Claude models prefer the Human/Assistant dialogue format.

    # Base content of the prompt (without Human/Assistant wrappers yet)
    base_prompt_content = f"""
You are an expert review authenticity analyzer, highly skilled in detecting subtle nuances in language. Your primary objective is to accurately determine the authenticity of product reviews by applying criteria consistent with distinguishing genuine user experiences from deceptive content. You will leverage a deep understanding of human review patterns and common manipulation tactics.

**Characteristics of Authentic Reviews:**
* **Specificity & Detail:** Contains concrete examples, features, usage scenarios, or specific problems.
* **Personal Experience:** Uses phrases like "I noticed," "I used it for," "my experience," reflecting real interaction.
* **Balanced Perspective (Contradictory Sentiment):** Often includes a mix of pros and cons, or expresses mixed feelings about different aspects within the same review.
* **Natural Language & Imperfections (Low-Effort Authenticity / Grammar Quirks):** May include minor typos, grammatical quirks, or a conversational tone, or be very short if reflecting genuine "good enough" sentiment tied to value/price.
* **Specific Emotional Expression:** Anger, joy, or frustration tied to a particular feature or event.
* **Irrelevant but Real Details:** May discuss logistical elements like shipping, packaging, or delivery, even if unrelated to core product function, because these are real customer experiences.
* **Sarcasm:** Employs positive words or exaggerated praise to convey an underlying negative sentiment or criticism, requiring contextual understanding.

**Characteristics of Fake Reviews (including Sophisticated Fakes):**
* **Generality & Vagueness (Empty Raves/Inane Negativity):** Lacks specific details, uses generic praise ("good product," "works great") or vague, unsubstantiated criticism.
* **Overly Hyperbolic or Emotional Language:** Excessive exclamation points, extreme adjectives without concrete support.
* **Repetition & Content Recycling:** Phrases or ideas repeated excessively; content might be recycled from other reviews.
* **Promotional Language (Astroturfing):** Sounds like marketing copy, uses excessive jargon, or promotes external links/other products.
* **"A+ in Composition":** Consistently perfect grammar and syntax, sometimes unnatural for a casual review, especially when paired with generic content (AI tell).
* **Lack of Realistic Incidents:** Struggles to invent specific, vivid anecdotes that make a review feel truly authentic.
* **Reviewer Profile Anomalies:** (While you can't check profiles, this informs the textual patterns to look for.)

**Your Analysis Process for the given Review:**
1.  **Thorough Reading:** Carefully read and understand the review.
2.  **Pattern Recognition:** Identify specific words, phrases, and structural patterns that align with either authentic or fake characteristics.
3.  **Contextual Interpretation:** For ambiguous cases (like sarcasm or irrelevant details), interpret the true intent based on the full context.
4.  **Reasoning Formulation:** Detail your step-by-step thought process, explaining *why* you classify it as authentic or fake, citing specific textual evidence from the review.
5.  **Score Assignment:** Assign an "authenticity_score" (float from 0.0 to 1.0) based on your analysis:
    * **0.0-0.2:** Highly likely fake (e.g., clear spam, blatant promotion, extremely generic positive/negative, AI tells).
    * **0.2-0.5:** Likely fake or very low-effort, suspicious authentic (e.g., overly vague, some AI tells, unsubstantiated claims).
    * **0.5-0.7:** Ambiguous / Neutral / Low-effort authentic (e.g., "It's fine," short but not suspicious, or reviews primarily about logistics with vague product comment).
    * **0.7-0.9:** Likely authentic (e.g., some specific details, natural tone, minor flaws, or genuine mixed sentiment).
    * **0.9-1.0:** Highly likely authentic (e.g., highly detailed, balanced, clear personal experience, nuanced human expression like sarcasm).
6.  **Strict JSON Output:** Provide your final findings as a JSON object.

Here are diverse, challenging examples (balanced for authentic/fake and covering edge cases) for precise analysis:

Review: "Good product. Happy with the purchase. Works as advertised. No issues."
Reasoning: This review is characterized by extreme brevity and generic, non-descriptive praise ("Good product," "Happy with the purchase," "No issues"). It completely lacks any specific details about features, personal experience, or unique observations. This pattern is strongly indicative of a low-effort fake or incentivized review that doesn't reflect genuine interaction or deep engagement with the product, falling under "Generality and Vagueness."
Analysis: {{ "authenticity_score": 0.15, "reasoning": "Generic praise, extremely short, and completely lacks specific details about product features or user experience, strongly indicative of inauthenticity." }}

Review: "The 'Quantum Flow 3000' water filter drastically improved my tap water taste. I noticed a difference in my morning coffee. Installation took about 15 minutes, largely thanks to the clear diagram on page 7 of the manual. Filter replacement seems straightforward too. Highly recommend for city dwellers."
Reasoning: This review demonstrates high authenticity through its remarkable specificity and detail. It names the product, identifies a specific benefit ("improved tap water taste," "difference in my morning coffee"), provides a precise installation time, references a specific page in the manual, and targets a specific user demographic. This depth of verifiable detail reflects genuine personal experience and interaction.
Analysis: {{ "authenticity_score": 0.98, "reasoning": "Highly specific details about usage, installation, and noticeable improvements, referencing a specific manual page, indicating a highly genuine, experienced user." }}

Review: "Oh wow, this 'super-duper' noise-cancelling headset is just *amazing*! I can still hear my dog barking two rooms over and the traffic outside. Truly, the silence is deafening. Five stars for the effort, I suppose."
Reasoning: This is a classic example of sarcasm. Despite using seemingly positive words ("amazing," "super-duper," "Five stars"), the review's context reveals a clearly negative experience. The user explicitly states they can still hear noise and that "silence is deafening," which is ironic. This requires interpreting the implied meaning over literal word choice, indicating genuine but frustrated human expression.
Analysis: {{ "authenticity_score": 0.88, "reasoning": "Authentic review using sarcasm; positive words convey a negative experience supported by specific observations of poor noise cancellation." }}

Review: "This is the optimal solution for managing complex data ecosystems. Its advanced API integration facilitates seamless data ingestion, ensuring robust interoperability across diverse enterprise architectures. A truly scalable infrastructure enhancement for any tech-forward organization. Visit buyproductnow.xyz for more!"
Reasoning: This review exhibits several hallmarks of a sophisticated fake. It uses excessive, formal technical jargon ("optimal solution," "complex data ecosystems," "robust interoperability," "diverse enterprise architectures") that sounds like marketing copy rather than a genuine user's organic feedback. The inclusion of an explicit external promotional URL ("buyproductnow.xyz") is a definitive red flag for spam. It's an "A+ in Composition" but lacks realistic human touch.
Analysis: {{ "authenticity_score": 0.02, "reasoning": "Overuse of corporate jargon, highly promotional tone, and includes an external link, indicating a highly inauthentic or spam review designed to mimic authenticity." }}

Review: "I bought this new coffee maker and it's okay. Nothing special, but it brews coffee. The packaging was a bit flimsy, but the delivery was super fast. My old one broke last month."
Reasoning: This review combines several authentic characteristics. It starts with low-effort authenticity ("it's okay," "Nothing special") but then includes genuine irrelevant details about packaging and delivery speed, which are common real-world user observations. It also provides a brief personal context ("My old one broke last month"). While not highly detailed about the product itself, it exhibits patterns of genuine, albeit casual, human feedback.
Analysis: {{ "authenticity_score": 0.65, "reasoning": "Authentic, low-effort review with irrelevant details about packaging/delivery and minimal product specifics, typical of casual user feedback." }}

Review: "I love this phone's battery life; it lasts forever. But I have to charge it three times a day. The camera is great, but photos often come out blurry in good light. Overall, it's a confusing product."
Reasoning: This review displays clear contradictory sentiment. It praises the battery life ("lasts forever") while immediately contradicting it ("charge it three times a day"). Similarly, it praises the camera ("great") then notes a significant flaw ("blurry in good light"). This mix of specific pros and cons within the same review is highly indicative of a genuine user's mixed experience.
Analysis: {{ "authenticity_score": 0.90, "reasoning": "Authentic review exhibiting contradictory sentiment, providing specific pros and cons within the same feedback, reflecting a nuanced user experience." }}

Review: "Amazing product. Everyone should buy this. The best purchase. I love it so much. A+++++"
Reasoning: This review consists of repetitive, generic praise and excessive positive sentiment without any supporting details or specific experiences. Phrases like "Amazing product," "Everyone should buy this," "The best purchase," and "A+++++" are hallmarks of low-effort, mass-generated, or incentivized fake reviews. It lacks any personal touch or specific observations.
Analysis: {{ "authenticity_score": 0.08, "reasoning": "Repetitive, generic, and hyperbolic praise lacking specific details, strongly indicative of a fake or incentivized review." }}

Review: "The new software update is totally useless! My app crashes constantly now, especially when I try to save. This is unacceptable! Developers, fix this immediately!"
Reasoning: This review, despite its strong negative emotion, is highly authentic. It clearly identifies a specific problem ("app crashes constantly"), provides a trigger ("especially when I try to save"), and makes a direct call to action to the developers. This level of specific, actionable feedback, even when frustrated, is a hallmark of a genuine user reporting an issue.
Analysis: {{ "authenticity_score": 0.94, "reasoning": "Highly specific negative review detailing a particular software bug and its impact, indicating genuine user frustration and experience." }}

Review: "It's fine. Whatever."
Reasoning: This review is extremely short and dismissive, offering no specific information or descriptive content. While its brevity makes it low-effort, it doesn't contain the typical hyperbolic or promotional language of fakes. It leans towards authentic because very short, indifferent reviews can be genuine, but the lack of detail makes its authenticity somewhat ambiguous.
Analysis: {{ "authenticity_score": 0.45, "reasoning": "Extremely short and vague, offers no descriptive content or specific sentiment, indicating low-effort authenticity with ambiguity." }}

Review: "{review_text}"
Please analyze the authenticity of the above review.
Provide your reasoning step-by-step in your thought process before giving the final analysis.
Your final output MUST be ONLY a single JSON object with two keys:
- "authenticity_score": a float between 0.0 (completely fake) and 1.0 (completely authentic).
- "reasoning": a string explaining your analysis.

Output JSON:
"""

    # --- START MODIFICATION ---
    # Claude-specific body parameters
    body = json.dumps({
        "prompt": f"\n\nHuman: {base_prompt_content}\n\nAssistant:", # Wrapped for Claude
        "max_tokens_to_sample": 700, # Max tokens for Claude response
        "temperature": 0.1,   # Keep low for consistency
        "top_p": 0.9,
        "stop_sequences": ["\n\nHuman:", "Output JSON:"], # Important stop sequences for Claude
    })
    # --- END MODIFICATION ---

    try:
        response = bedrock_runtime.invoke_model(
            body=body,
            modelId=model_id,
            accept='application/json',
            contentType='application/json'
        )

        response_body = json.loads(response.get('body').read())

        # --- START MODIFICATION ---
        # Claude-specific output extraction
        generated_text = response_body.get('completion', '').strip() # Claude's response is in 'completion'
        # --- END MODIFICATION ---

        # Robust JSON extraction logic remains the same
        json_match = re.search(r'```json\s*(\{.*\})\s*```', generated_text, re.DOTALL)

        if json_match:
            json_string = json_match.group(1)
        else:
            json_match = re.search(r'(\{.*?\})', generated_text, re.DOTALL)
            if json_match:
                json_string = json_match.group(0)
            else:
                raise ValueError(f"No valid JSON object found in model output. Raw output: {generated_text}")

        try:
            analysis_result = json.loads(json_string)

            if not isinstance(analysis_result, dict) or \
               "authenticity_score" not in analysis_result or \
               "reasoning" not in analysis_result:
                raise ValueError("Bedrock response is not a valid analysis format.")

            score = float(analysis_result["authenticity_score"])
            if not (0.0 <= score <= 1.0):
                print(f"WARNING: Authenticity score {score} out of expected range [0.0, 1.0]. Clamping.")
                score = max(0.0, min(1.0, score))

            analysis_result["authenticity_score"] = score

            return analysis_result

        except json.JSONDecodeError as e:
            print(f"ERROR: Failed to parse extracted JSON string: {e}")
            print(f"DEBUG: Problematic JSON string for parsing: '{json_string}'")
            return {"error": "Model returned malformed JSON.", "raw_output": generated_text, "parsing_error": str(e)}
        except ValueError as e:
            print(f"ERROR: Model output format validation failed: {e}")
            print(f"DEBUG: Raw output that failed validation: '{generated_text}'")
            return {"error": str(e), "raw_output": generated_text}

    except Exception as e:
        print(f"ERROR: An error occurred during Bedrock invocation: {e}")
        return {"error": f"Internal server error during analysis: {str(e)}"}