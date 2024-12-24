from sqlalchemy.orm import Session
from .models import Term

def create_term(db: Session, key: str, description: str):
    new_term = Term(key=key, description=description)
    db.add(new_term)
    db.commit()
    db.refresh(new_term)
    return new_term

def get_term(db: Session, key: str):
    return db.query(Term).filter(Term.key == key).first()

def update_term(db: Session, key: str, new_description: str):
    term = get_term(db, key)
    if term:
        term.description = new_description
        db.commit()
        db.refresh(term)
    return term

def delete_term(db: Session, key: str):
    term = get_term(db, key)
    if term:
        db.delete(term)
        db.commit()
        return True
    return False

def list_terms(db: Session):
    return db.query(Term).all()
