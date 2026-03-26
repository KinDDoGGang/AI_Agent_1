from app.core.config import get_settings
from app.providers.openai.client import get_openai_client


def analyze_alert(prompt: str) -> str:
    settings = get_settings()
    client = get_openai_client()

    response = client.responses.create(
        model=settings.openai_model,
        instructions=(
            "너는 Datadog 장애 분석 도우미다. "
            "반드시 한국어로 답하고, 아래 형식으로 정리해라.\n"
            "1. 장애 요약\n"
            "2. 추정 원인\n"
            "3. 즉시 확인 항목\n"
            "4. 권장 조치\n"
        ),
        input=prompt,
    )

    return response.output_text.strip()