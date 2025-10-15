from typing import Dict, Any
from ..types import (
    AgeRating, 
    SortType, 
    ContentType, 
    Seasons, 
    PublishStatusesType, 
    ProductionStatusesType
)
from ..models import ReleaseCollection, Release


async def validate_filters(params: Release) -> Dict[str, Any]:
    """
    Валидация параметров фильтров в формате f["название_переменной"]
    
    :param filters: Словарь с параметрами фильтров
    """
    filters = {
        "genres": params.genres,
        "types": params.types,
        "seasons": params.seasons,
        "from_year": params.from_year,
        "to_year": params.to_year,
        "search": params.search,
        "sorting": params.sorting,
        "age_ratings": params.age_ratings,
        "publish_statuses": params.publish_statuses,
        "production_statuses": params.production_statuses
    }
    validated_filters = {}
    
    # Валидация genres
    if "genres" in filters and filters["genres"] is not None:
        if not isinstance(filters["genres"], str):
            raise ValueError("genres должен быть строкой")
        validated_filters["f[genres]"] = filters["genres"]
    
    # Валидация types (список ContentType)
    if "types" in filters and filters["types"] is not None:
        if not isinstance(filters["types"], list) or not all(isinstance(t, ContentType) for t in filters["types"]):
            raise ValueError("types должен быть списком ContentType")
        validated_filters["f[types]"] = [t.value for t in filters["types"]]
    
    # Валидация seasons (список Seasons)
    if "seasons" in filters and filters["seasons"] is not None:
        if not isinstance(filters["seasons"], list) or not all(isinstance(s, Seasons) for s in filters["seasons"]):
            raise ValueError("seasons должен быть списком Seasons")
        validated_filters["f[seasons]"] = [s.value for s in filters["seasons"]]
    
    # Валидация from_year
    if "from_year" in filters and filters["from_year"] is not None:
        if not isinstance(filters["from_year"], int) or filters["from_year"] < 1900:
            raise ValueError("from_year должен быть целым числом не менее 1900")
        validated_filters["f[from_year]"] = filters["from_year"]
    
    # Валидация to_year
    if "to_year" in filters and filters["to_year"] is not None:
        if not isinstance(filters["to_year"], int) or filters["to_year"] < 1900:
            raise ValueError("to_year должен быть целым числом не менее 1900")
        validated_filters["f[to_year]"] = filters["to_year"]
    
    # Валидация search
    if "search" in filters and filters["search"] is not None:
        if not isinstance(filters["search"], str):
            raise ValueError("search должен быть строкой")
        validated_filters["f[search]"] = filters["search"]
    
    # Валидация sorting
    if "sorting" in filters and filters["sorting"] is not None:
        if not isinstance(filters["sorting"], SortType):
            raise ValueError("sorting должен быть экземпляром SortType")
        validated_filters["f[sorting]"] = filters["sorting"].value
    
    # Валидация age_ratings (список AgeRating)
    if "age_ratings" in filters and filters["age_ratings"] is not None:
        if not isinstance(filters["age_ratings"], list) or not all(isinstance(a, AgeRating) for a in filters["age_ratings"]):
            raise ValueError("age_ratings должен быть списком AgeRating")
        validated_filters["f[age_ratings]"] = [a.value for a in filters["age_ratings"]]
    
    # Валидация publish_statuses (список PublishStatusesType)
    if "publish_statuses" in filters and filters["publish_statuses"] is not None:
        if not isinstance(filters["publish_statuses"], list) or not all(isinstance(p, PublishStatusesType) for p in filters["publish_statuses"]):
            raise ValueError("publish_statuses должен быть списком PublishStatusesType")
        validated_filters["f[publish_statuses]"] = [p.value for p in filters["publish_statuses"]]
    
    # Валидация production_statuses (список ProductionStatusesType)
    if "production_statuses" in filters and filters["production_statuses"] is not None:
        if not isinstance(filters["production_statuses"], list) or not all(isinstance(p, ProductionStatusesType) for p in filters["production_statuses"]):
            raise ValueError("production_statuses должен быть списком ProductionStatusesType")
        validated_filters["f[production_statuses]"] = [p.value for p in filters["production_statuses"]]
    
    return validated_filters

async def create_filters_from_release(release: Release) -> Dict[str, Any]:
    """
    Создает фильтры в формате API из объекта Release
    
    :param release: Объект Release с параметрами фильтрации
    """
    filters = {}
    
    # genres
    if release.genres is not None:
        filters["genres"] = release.genres
    
    # types
    if release.types is not None:
        filters["types"] = [t.value for t in release.types]
    
    # seasons
    if release.seasons is not None:
        filters["seasons"] = [s.value for s in release.seasons]
    
    # years (объединяем from_year и to_year)
    if release.from_year is not None or release.to_year is not None:
        years = {}
        if release.from_year is not None:
            years["from_year"] = release.from_year
        if release.to_year is not None:
            years["to_year"] = release.to_year
        filters["years"] = years
    
    # search
    if release.search is not None:
        filters["search"] = release.search
    
    # sorting
    if release.sorting is not None and release.sorting:
        filters["sorting"] = release.sorting.value
    
    # age_ratings
    if release.age_ratings is not None:
        filters["age_ratings"] = [a.value for a in release.age_ratings]
    
    # publish_statuses
    if release.publish_statuses is not None:
        filters["publish_statuses"] = [p.value for p in release.publish_statuses]
    
    # production_statuses
    if release.production_statuses is not None:
        filters["production_statuses"] = [p.value for p in release.production_statuses]
    
    return {"f": filters}

async def validate_collection(params: ReleaseCollection) -> Dict[str, Any]:
    """
    Валидация параметров фильтров для ReleaseCollection в формате f["название_переменной"]
    
    :param params: Объект ReleaseCollection с параметрами фильтрации
    """
    filters = {
        "genres": params.genres,
        "types": params.types,
        "years": params.years,
        "search": params.search,
        "age_ratings": params.age_ratings
    }
    validated_filters = {}
    
    # Валидация genres
    if "genres" in filters and filters["genres"] is not None:
        if not isinstance(filters["genres"], str):
            raise ValueError("genres должен быть строкой")
        validated_filters["f[genres]"] = filters["genres"]
    
    # Валидация types (список ContentType)
    if "types" in filters and filters["types"] is not None:
        if not isinstance(filters["types"], list) or not all(isinstance(t, ContentType) for t in filters["types"]):
            raise ValueError("types должен быть списком ContentType")
        validated_filters["f[types]"] = [t.value for t in filters["types"]]
    
    # Валидация years
    if "years" in filters and filters["years"] is not None:
        if not isinstance(filters["years"], str):
            raise ValueError("years должен быть строкой")
        validated_filters["f[years]"] = filters["years"]
    
    # Валидация search
    if "search" in filters and filters["search"] is not None:
        if not isinstance(filters["search"], str):
            raise ValueError("search должен быть строкой")
        validated_filters["f[search]"] = filters["search"]
    
    # Валидация age_ratings (список AgeRating)
    if "age_ratings" in filters and filters["age_ratings"] is not None:
        if not isinstance(filters["age_ratings"], list) or not all(isinstance(a, AgeRating) for a in filters["age_ratings"]):
            raise ValueError("age_ratings должен быть списком AgeRating")
        validated_filters["f[age_ratings]"] = [a.value for a in filters["age_ratings"]]
    
    return validated_filters


async def validated_json_collection(release: ReleaseCollection) -> Dict[str, Any]:
    """
    Создает фильтры в формате API из объекта ReleaseCollection
    
    :param release: Объект ReleaseCollection с параметрами фильтрации
    """
    filters = {}
    
    # genres
    if release.genres is not None:
        filters["genres"] = release.genres
    
    # types
    if release.types is not None:
        filters["types"] = [t.value for t in release.types]
    
    # years
    if release.years is not None:
        filters["years"] = release.years
    
    # search
    if release.search is not None:
        filters["search"] = release.search
    
    # age_ratings
    if release.age_ratings is not None:
        filters["age_ratings"] = [a.value for a in release.age_ratings]
    
    return {"f": filters}