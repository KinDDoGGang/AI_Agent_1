from fastapi import APIRouter, HTTPException

from app.agents.workers.datadog_worker import build_analysis_prompt
from app.integrations.slack_client import send_to_slack
from app.providers.openai.responses import analyze_alert
from app.schemas.webhooks import DatadogWebhookPayload

router = APIRouter(prefix="/webhooks", tags=["webhooks"])


@router.post("/datadog")
def datadog_webhook(payload: DatadogWebhookPayload) -> dict:
    try:
        prompt = build_analysis_prompt(payload)
        analysis = analyze_alert(prompt)

        slack_message = (
            "[Datadog 장애 자동 분석]\n\n"
            f"제목: {payload.title or '-'}\n"
            f"알림유형: {payload.alert_type or '-'}\n"
            f"모니터ID: {payload.monitor_id or '-'}\n\n"
            f"{analysis}"
        )

        slack_result = send_to_slack(slack_message)

        return {
            "ok": True,
            "analysis": analysis,
            "slack": slack_result,
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))