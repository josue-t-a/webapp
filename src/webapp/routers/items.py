
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from webapp.database import get_db
from webapp.schemas import ItemCreate, ItemResponse, ItemUpdate
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

@router.get("", response_model=list[ItemResponse])
def read_items(db: Session = Depends(get_db)):
    return crud.get_items(db)


@router.get("/{item_id}", response_model=ItemResponse)
def read_item(
    item_id: int,
    db: Session = Depends(get_db),
):
    item = crud.get_item(db, item_id)

    if item is None:
        raise HTTPException(
            status_code=404,
            detail="Item no encontrado",
        )

    return item

@router.put("/{item_id}", response_model=ItemResponse)
def update_item(
    item_id: int,
    data:ItemUpdate,
    db: Session = Depends(get_db),
):
    item = crud.update_item(db, item_id, data)

    if item is None:
        raise HTTPException(
            status_code=404,
            detail="Item not found"
        )
    
    return item

@router.delete("/{item_id}", response_model=ItemResponse)
def delete_item(
    item_id:int,
    db: Session = Depends(get_db),
):
    item = crud.delete_item(db, item_id)

    if item is None:
            raise HTTPException(
                status_code=404,
                detail="Item not found"
            )

    return item