from pydantic import BaseModel
from typing import List
from .types import (
    ContentType, 
    Seasons, 
    SortType, 
    AgeRating, 
    PublishStatusesType, 
    ProductionStatusesType, 
    CollectionType
)


class TimeCode(BaseModel):
    """
    Класс для работы с этими методами:

    accounts.users_me_views_timecodes_update
    """
    time: int
    is_watched: bool
    release_episode_id: str

class Release(BaseModel):
    """
    Класс для работы с этими методами:

    anime.catalog_releases_get
    
    anime.catalog_releases_post
    """
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

class ReleaseCollection(BaseModel):
    """
    Класс для работы с этими методами

    users_me_collections_releases_get

    users_me_collections_releases_post
    """
    type_of_collection: CollectionType
    page: int | None = None
    limit: int | None = None
    genres: str | None = None
    types: List[ContentType] | None = None
    years: str | None = None
    search: str | None = None
    age_ratings: List[AgeRating] | None = None
    include: str | None = None
    exclude: str | None = None