
from sqlalchemy import select
from sqlalchemy.orm import Session

from webapp.models import Item
from webapp.schemas import ItemCreate


def create_item(db: Session, data: ItemCreate) -> Item:
    item = Item(id=data.id, query=data.description)
    db.add(item)
    db.commit()
    db.refresh(item)
    return item
