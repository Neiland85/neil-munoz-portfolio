from pydantic import BaseModel
from typing import List, Optional
from uuid import UUID, uuid4
from datetime import datetime


class EmailBlock(BaseModel):
    type: str  # text, button, image
    content: dict


class EmailTemplate(BaseModel):
    subject: str
    blocks: List[EmailBlock]


class EmailCampaign(BaseModel):
    id: UUID = uuid4()
    festival_id: UUID
    template: EmailTemplate
    recipients: List[str]
    scheduled_at: Optional[datetime] = None
    created_at: datetime = datetime.utcnow()
