from openai import OpenAI
from config.settings import OPENAI_API_KEY

# initialize client
client = OpenAI(api_key=OPENAI_API_KEY)


def ask_llm(prompt):

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "system",
                "content": "You are a cybersecurity and AI privacy compliance auditor."
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.2
    )

    return response.choices[0].message.content