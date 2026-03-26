from app.schemas.webhooks import DatadogWebhookPayload


def build_analysis_prompt(payload: DatadogWebhookPayload) -> str:
    tags = ", ".join(payload.tags) if payload.tags else "-"

    return f"""
다음 Datadog 알림을 분석해줘.

제목: {payload.title or "-"}
본문: {payload.text or "-"}
alert_type: {payload.alert_type or "-"}
event_type: {payload.event_type or "-"}
발생시각: {payload.date or "-"}
monitor_id: {payload.monitor_id or "-"}
event_id: {payload.id or "-"}
url: {payload.url or "-"}
tags: {tags}

운영자에게 바로 전달할 수 있게 정리해줘.
""".strip()