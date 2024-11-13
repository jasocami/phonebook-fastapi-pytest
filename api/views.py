from sqlmodel import select
from fastapi import status as http_status, HTTPException

from api.constants import CONTACTS, PhoneTypes
from api.models import Contact, ContactPublic, ContactCreateUpdate
from api.sql_engine import SessionDep


def get_contacts(session: SessionDep) -> list[ContactPublic]:
    return session.exec(select(Contact)).all()


def get_contact(pk: int, session: SessionDep) -> ContactPublic:
    if contact := session.get(Contact, pk):
        return contact
    raise HTTPException(status_code=http_status.HTTP_404_NOT_FOUND, detail='Not found')


def save_contact(contact: Contact, session: SessionDep) -> Contact:
    contact = Contact.model_validate(contact)
    session.add(contact)
    session.commit()
    session.refresh(contact)
    return contact


def delete_contact(pk: int, session: SessionDep) -> bool:
    if contact := session.get(Contact, pk):
        session.delete(contact)
        session.commit()
        return True
    raise HTTPException(status_code=http_status.HTTP_404_NOT_FOUND, detail='Not found')


def update_contact(pk: int, data: ContactCreateUpdate, session: SessionDep) -> ContactPublic:
    if contact := session.get(Contact, pk):
        contact_data = data.model_dump(exclude_unset=True)
        contact.sqlmodel_update(contact_data)
        session.add(contact)
        session.commit()
        session.refresh(contact)
        return contact
    raise HTTPException(status_code=http_status.HTTP_404_NOT_FOUND, detail='Not found')
