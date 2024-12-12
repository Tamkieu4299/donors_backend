from pydantic import BaseModel
from datetime import date
from schemas.user import UserResponseSchema
from schemas.site import SiteResponse

class DonationSchema(BaseModel):
    user_id: int
    site_id: int
    class Config:
        orm_mode = True

class DonationResponse(BaseModel):
    id: int
    user: UserResponseSchema
    site: SiteResponse
    created_at: date

    class Config:
        orm_mode = True