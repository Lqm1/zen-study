from __future__ import annotations

from typing import List, Optional

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


class Progress(BaseModel):
    total_count: int
    passed_count: int
    total_chapters: int
    passed_chapters: int
    total_materials: int
    passed_materials: int
    on_calculation: bool


class SubjectCategory(BaseModel):
    title: str


class Progress1(BaseModel):
    total_count: int
    passed_count: int
    on_calculation: bool
    status: str


class Chapter(BaseModel):
    id: int
    title: str
    progress: Progress1
    thumbnail_url: Optional[str] = None
    outline: str
    resource_type: str
    label: Optional[str] = None


class MaterialCourse(BaseModel):
    id: int
    type: str
    title: str
    selected: bool
    progress: Progress
    thumbnail_url: str
    outline: str
    subject_category: SubjectCategory
    chapters: List[Chapter]