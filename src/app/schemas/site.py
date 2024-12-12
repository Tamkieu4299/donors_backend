from pydantic import BaseModel
from typing import Optional

class SiteAdd(BaseModel):
    name: str
    map_marker: str = None
    city: str = None
    street: str = None
    longtitude: float = 0
    latitude: float = 0

    class Config:
        orm_mode = True

class SiteUpdate(BaseModel):
    name: Optional[str]
    map_marker: Optional[str]
    city: Optional[str]
    street: Optional[str]
    longtitude: Optional[float]
    latitude: Optional[float]

class SiteFilter(BaseModel):
    name: Optional[str]
    map_marker: Optional[str]
    city: Optional[str]
    street: Optional[str]
    longtitude: Optional[float] = 0
    latitude: Optional[float] = 0
    amount_of_donors: Optional[int] = 0
    amount_of_approved_donors: Optional[int]
    amount_of_blood: Optional[int] = 0

    class Config:
        orm_mode = True

class SiteResponse(BaseModel):
    id: int
    name: str
    map_marker: str = None
    city: str = None
    street: str = None
    longtitude: float = 0
    latitude: float = 0
    amount_of_donors: int = 0
    amount_of_approved_donors: int = 0
    amount_of_blood: int = 0

    class Config:
        orm_mode = True
