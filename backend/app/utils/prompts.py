# Detailed prompts for the Clarity Engine
CLARITY_PROMPT_TEMPLATE = """
Analyze the following customer reviews for a product. Your task is to identify the single most common and significant point of confusion or mismatched expectation that could lead to a customer return.
Focus exclusively on concrete product attributes like:
- Sizing (e.g., "runs small", "runs large", "inconsistent sizing")
- Color (e.g., "color is not as vibrant", "color is different from photos")
- Material (e.g., "fabric feels cheap", "material is thinner than expected")
- Assembly (e.g., "difficult to assemble", "instructions are unclear")

If a clear, recurring theme is present in at least 20% of the reviews, synthesize it into a concise, one-sentence "Clarity Alert" of 15 words or less. The alert should be direct, helpful, and start with "Customers suggest..." or "Be aware:".

If there is no single, dominant theme of confusion, you MUST respond with "NO_ALERT". Do not invent a theme.

Reviews:
---
{reviews_text}
---

Clarity Alert:
"""

# Detailed prompts for the Authenticity Engine
AUTHENTICITY_PROMPT_TEMPLATE = """
You are an expert fraud detection AI. Analyze the user-provided product review for signals of authenticity versus deception.

Evaluate the review based on these criteria:
- **Linguistic Style:** Is the language overly generic, full of clichés, or does it resemble known "template" reviews? Does it have excessive emotional hyperbole without substance?
- **Detail Specificity:** Does the review provide credible, specific details about the product's use, its features, or the user's experience? Or is it vague?
- **Sentiment Consistency:** Does the sentiment align logically with the content?

Here are examples of how to analyze reviews.

---
**Good Example:**
Review to Analyze: "I've been using this for about two weeks now. It was easy to assemble, taking me about 15 minutes with the included tool. The material feels sturdy and has held up well to daily use. Specifically, I love the side pocket feature, which is perfect for my remote control."
JSON Response:
{{
  "authenticity_score": 0.9,
  "key_positive_signals": ["Includes specific details about assembly and material", "Mentions a specific feature (side pocket) and its use"],
  "potential_concerns": []
}}
---
**Bad Example:**
Review to Analyze: "Wow. This product is amazing. I love it very much. Best purchase ever. Highly recommend to everyone. Five stars."
JSON Response:
{{
  "authenticity_score": 0.2,
  "key_positive_signals": [],
  "potential_concerns": ["Uses generic, template-like language", "Lacks any specific product details", "Contains excessive emotional hyperbole"]
}}
---

Now, analyze the following review and provide your JSON response.

Review to Analyze:
---
{review_text}
---

JSON Response:
"""