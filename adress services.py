from fastapi import HTTPException, status
from typing import List
from . import models


async def create_new_address(request, database, current_user) -> models.Address:
    new_address = models.Address(shipping_address=request.shipping_address, user_id=current_user.id)
    database.add(new_address)
    database.commit()
    database.refresh(new_address)
    return new_address


async def get_address_listing(database) -> List[models.Address]:
    addresses = database.query(models.Address).all()
    return addresses


async def get_address_by_id(address_id, database):
    address = database.query(models.Address).filter_by(id=address_id).first()
    if not address:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Address Not Found !"
        )
    return address


async def delete_address_by_id(address_id, database):
    database.query(models.Address).filter(
        models.Address.id == address_id).delete()
    database.commit()


async def update_address_by_id(address_id, request, database):
    address = database.query(models.Address).get(address_id)
    if not address:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="address Not Found !"
        )
    return address




