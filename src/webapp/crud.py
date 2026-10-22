
from sqlalchemy import select
from sqlalchemy.orm import Session

from webapp.models import Item
from webapp.schemas import ItemCreate, ItemUpdate


def create_item(db: Session, data: ItemCreate) -> Item:
    item = Item(id=data.id, description=data.description)
    db.add(item)
    db.commit()
    db.refresh(item)
    return item

def get_items(db: Session) -> list[Item]:
    return list(
        db.scalars(select(Item).order_by(Item.id)).all()
    )

def get_item(db: Session, item_id: int) -> Item | None:
    return db.get(Item, item_id)

def update_item(db:Session, item_id:int, data:ItemUpdate):
    item = db.scalars(select(Item).filter(Item.id == item_id)).first()
    
    if item is None:
        return None
    item.description = data.description
    db.commit()
    db.refresh(item)

    return item

def delete_item(db: Session, item_id: int):
    item = db.get(Item, item_id)

    if item is None:
        return None

    db.delete(item)
    db.commit()
    return item