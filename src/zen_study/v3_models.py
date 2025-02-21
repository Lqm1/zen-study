from __future__ import annotations

from typing import List, Optional

from pydantic import BaseModel


class Progress(BaseModel):
    total_count: int
    passed_count: int


class ComprehensionItem(BaseModel):
    total_count: int
    good_count: int
    bad_count: int


class Course(BaseModel):
    id: int
    type: str
    title: str
    selection_status: str
    selected: bool
    thumbnail_url: str
    on_calculation: bool
    progress: Progress
    comprehension: Optional[ComprehensionItem]


class Service(BaseModel):
    total_course_count: int
    courses: List[Course]
    name: str
    periodic_exam_title: Optional[str]
