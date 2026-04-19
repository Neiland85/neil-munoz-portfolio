from fastapi import APIRouter
from app.next_feature.email.models import EmailCampaign

router = APIRouter(prefix="/emails", tags=["emails"])


@router.post("/campaigns")
def create_campaign(campaign: EmailCampaign):
    return {"status": "created", "campaign_id": str(campaign.id)}
