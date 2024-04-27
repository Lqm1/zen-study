from __future__ import annotations

from typing import List

from pydantic import BaseModel


class CsrfToken(BaseModel):
    token: str
    expire_time: int


class User(BaseModel):
    zane_user_id: int
    name: str
    icon: str
    sex: int
    authority: List[str]
    payment: bool
    payments: List
    is_chargeable: bool
    is_personal_information_needed: bool
    capabilities: List[str]


class Notice(BaseModel):
    id: int
    notice_type: str
    target_id: int
    target_type: str
    title: str
    description: str
    resource: str
    created_at: int