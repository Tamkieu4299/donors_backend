from sqlalchemy import Column, Integer, String,Float
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy.orm import relationship

from ._base_model import BaseModel


class Site(BaseModel):
    __tablename__ = "sites"
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String, nullable=False)
    longtitude = Column(Integer, default=0, nullable=False)
    latitude =  Column(Float, default=0, nullable=False)
    city = Column(String, nullable=True)
    street = Column(String, nullable=True)
    
    donations = relationship("Donation", back_populates="site", cascade="all, delete-orphan")

    @hybrid_property
    def amount_of_donors(self):
        return len(self.donations)

    @hybrid_property
    def amount_of_approved_donors(self):
        return len([donation for donation in self.donations if donation.has_approved])
    
    @hybrid_property
    def amount_of_blood(self):
        return sum(donation.volume_of_blood for donation in self.donations if donation.has_approved)
    
    class Config:
        orm_mode = True
