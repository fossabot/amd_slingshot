# ANALYSIS_PROMPT = """
# You are a Privacy Compliance AI Agent.

# Use the following regulatory context to answer the question.

# Context:
# {context}

# Question:
# {query}

# Provide a structured privacy analysis including:
# 1. Risk
# 2. Relevant regulation
# 3. Recommendation
# """

def get_full_prompt(context, uploaded_text, prompt):

    full_prompt = f"""
You are an AI Privacy Compliance Auditor.

Use the framework knowledge to evaluate the company's privacy practices.

Framework Knowledge:
{context}

Company Document:
{uploaded_text}

User Question:
{prompt}

Tasks:
1. Determine if the company is compliant with privacy regulations.
2. Identify potential privacy violations.
3. Detect misleading statements (example: claiming encryption but using hashing).
4. Provide recommendations to improve compliance.

Return a structured analysis.
"""

    return full_prompt