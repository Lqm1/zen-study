from __future__ import annotations

from typing import Dict, List, Optional, Any

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


class Progress2(BaseModel):
    total_count: int
    passed_count: int
    status: str


class Section(BaseModel):
    resource_type: str
    id: int
    title: str
    passed: bool
    textbook_info: Optional[str] = None
    length: Optional[int] = None
    content_url: str
    material_type: str
    thumbnail_url: Optional[str]
    permissions: Dict[str, Any]
    playback_position: Optional[int] = None
    total_question: Optional[int] = None
    done: Optional[bool] = None


class MaterialChapter(BaseModel):
    id: int
    title: str
    outline: str
    thumbnail_url: Optional[str] = None
    open_section_index: int
    progress: Progress2
    sections: List[Section]
    course_type: Optional[str] = None


class SectionUse(BaseModel):
    active: bool
    reason: str
    meta: Dict[str, Any]


class PackageSelect(BaseModel):
    active: bool
    reason: str
    meta: Dict[str, Any]


class Permissions(BaseModel):
    section_use: SectionUse
    package_select: PackageSelect


class Comprehension(BaseModel):
    limit: int
    bad: int
    good: int
    perfect: int


class Checkpoint(BaseModel):
    total: int
    clear: int


class Progress3(BaseModel):
    on_calculation: bool
    comprehension: Comprehension
    checkpoint: Checkpoint


class ShortTest(BaseModel):
    total_short_test: int
    total_passed_short_test: int


class MaterialRecommendation(BaseModel):
    header: str
    class Course(BaseModel):
        id: int
        type: str
        title: str
        outline: str
        released_at: int
        permission_label: str
        permission_url: str
        permission_text: str
        permissions: Permissions
        selected: bool
        progress: Progress3
        short_test: ShortTest
        thumbnail_url: str
        subject_category: SubjectCategory
        chapters: List
    courses: List[Course]


class Service(BaseModel):
    name: str
    course_total: int
    class Course(BaseModel):
        id: int
        type: str
        title: str
        selected: bool
        progress: Progress
        thumbnail_url: str
        outline: str
    courses: List[Course]