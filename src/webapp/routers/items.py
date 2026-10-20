
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from webapp.database import get_db
from webapp.schemas import ItemCreate, ItemResponse
from webapp import crud

router = APIRouter(prefix="/items", tags=["items"])

@router.post("", response_model=ItemResponse, status_code=201)
def create_item(
    data: ItemCreate,
    db: Session = Depends(get_db),
):
    try:
        return crud.create_item(db, data)
    except IntegrityError:
        db.rollback()
        raise HTTPException(
            status_code=409,
            detail="El ID ya existe",
        )
