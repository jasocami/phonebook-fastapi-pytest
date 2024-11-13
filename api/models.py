from typing import Annotated

from fastapi import Depends, FastAPI, HTTPException, Query
from sqlmodel import Field, Session, SQLModel, create_engine, select


class ContactBase(SQLModel):
    name: str = Field(index=True)
    phone: int | None = Field(default=None)


class Contact(ContactBase, table=True):
    id: int | None = Field(default=None, primary_key=True)


class ContactPublic(ContactBase):
    id: int


class ContactCreateUpdate(ContactBase):
    pass
