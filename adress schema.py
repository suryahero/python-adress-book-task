from typing import Optional
from pydantic import BaseModel, constr


class AddressBase(BaseModel):
    id: Optional[int]
    created_at: Optional[str]
    shipping_address: str
    user_id: Optional[int]

    class Config:
        orm_mode = True

class AddressUpdate(BaseModel):
    shipping_address: Optional[str]

    class Config:
        orm_mode = True