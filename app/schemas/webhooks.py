from pydantic import BaseModel, ConfigDict, Field


class DatadogWebhookPayload(BaseModel):
    model_config = ConfigDict(extra="allow")

    title: str | None = None
    text: str | None = None
    alert_type: str | None = None
    event_type: str | None = None
    date: str | None = None
    id: int | None = None
    monitor_id: int | None = None
    url: str | None = None
    tags: list[str] = Field(default_factory=list)