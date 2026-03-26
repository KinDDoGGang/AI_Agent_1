import httpx

from app.core.config import get_settings


def send_to_slack(text: str) -> dict:
    settings = get_settings()

    if not settings.slack_webhook_url:
        return {"sent": False, "reason": "slack_webhook_url is empty"}

    response = httpx.post(
        settings.slack_webhook_url,
        json={"text": text},
        timeout=10.0,
    )
    response.raise_for_status()

    return {"sent": True, "status_code": response.status_code}