from pydantic import BaseModel
from typing import List
from .types import *

class TimeCode(BaseModel):
    time: int
    is_watched: bool
    release_episode_id: str

class Release(BaseModel):
    page: int | None = None
    limit: int | None = None
    genres: str | None = None
    types: List[ContentType] | None = None
    seasons: List[Seasons] | None = None
    from_year: int | None = None
    to_year: int | None = None
    search: str | None = None
    sorting: SortType | None = None
    age_ratings: List[AgeRating] | None = None
    publish_statuses: List[PublishStatusesType] | None = None
    production_statuses: List[ProductionStatusesType] | None = None
    include: str | None = None
    exclude: str | None = None