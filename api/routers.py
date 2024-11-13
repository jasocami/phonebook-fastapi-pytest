from fastapi import APIRouter

from api.constants import PhoneTypes
from api.models import Contact, ContactPublic, ContactCreateUpdate
from api.sql_engine import SessionDep
from api.views import get_contact, get_contacts, save_contact, delete_contact, update_contact

router = APIRouter()


@router.get('/')
async def home():
    return {'message': 'Main phonebook page'}


@router.get('/contacts/')
async def contacts_list(session: SessionDep) -> list[ContactPublic]:
    return get_contacts(session)


@router.post('/contacts/', response_model=ContactPublic)
async def create_contact(contact: Contact, session: SessionDep):
    return save_contact(contact, session)


@router.get('/contacts/{contact_id}/', response_model=ContactPublic)
async def contact_item(contact_id: int, session: SessionDep):
    return get_contact(contact_id, session)


@router.delete('/contacts/{contact_id}/')
async def delete_contact_item(contact_id: int, session: SessionDep) -> dict:
    delete_contact(contact_id, session)
    return {'ok': True}


@router.patch('/contacts/{contact_id}/', response_model=ContactPublic)
async def update_contact_item(contact_id: int, contact: ContactCreateUpdate, session: SessionDep):
    contact = update_contact(contact_id, contact, session)
    return contact


@router.get('/phone-types/{ptype}/')
async def phone_types_list(ptype: PhoneTypes):
    rs = {'phone_type': ptype}
    if ptype is PhoneTypes.other:
        rs['message'] = 'What type then?'
        return rs
    if ptype is PhoneTypes.work:
        rs['message'] = "Don't call out of schedule!"
        return rs
    return rs
