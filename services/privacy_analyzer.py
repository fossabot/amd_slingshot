from services.llm_service import get_llm
from utils.prompts import ANALYSIS_PROMPT


def analyze_privacy(context, user_query):

    llm = get_llm()

    prompt = ANALYSIS_PROMPT.format(
        context=context,
        query=user_query
    )

    response = llm.invoke(prompt)

    return response.content