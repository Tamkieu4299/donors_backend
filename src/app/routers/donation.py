from typing import List

from constants.config import Settings
from crud.donation import CRUDDonation
from db.database import get_db
from fastapi import APIRouter, Depends, HTTPException
from models.donation import Donation
from secret import get_current_active_user
from schemas.donation import DonationSchema, DonationResponse
from sqlalchemy.orm import Session
from utils.exception import CommonInvalid
from app.utils.response import Response

settings = Settings()

router = APIRouter()

donation_crud = CRUDDonation(Donation)


@router.post("/register", response_model=DonationResponse)
async def donation(    
    payload: DonationSchema,
    db: Session = Depends(get_db),
):
    donation = await donation_crud.create(payload.dict(), db)
    if donation is None:
        raise CommonInvalid(detail=f"Fail to create donation")
    return Response(content=DonationResponse.from_orm(donation))


@router.get("/donations", response_model=List[DonationResponse])
async def get_donations(    
    db: Session = Depends(get_db),
):
    donation = donation_crud.get_all(db)
    return Response(content=[DonationResponse.from_orm(i) for i in donation])

@router.put("/approve/{donation_id}", response_model=DonationResponse)
async def approve_donation(
    donation_id: int,
    volume_of_blood: float,
    db: Session = Depends(get_db),
):
    updated_donation = donation_crud.update(donation_id, {"volume_of_blood": volume_of_blood, "has_approved": True}, db)
    if updated_donation is None:
        raise CommonInvalid(detail=f"Fail to update donation")
    return Response(content=DonationResponse.from_orm(updated_donation))
