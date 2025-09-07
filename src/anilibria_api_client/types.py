from enum import Enum


class CollectionType(Enum):
    """Типы коллекций"""
    PLANNED = "PLANNED"
    WATCHED = "WATCHED"
    WATCHING = "WATCHING"
    POSTPONED = "POSTPONED"
    ABANDONED = "ABANDONED"
    

class ContentType(Enum):
    """Типы контента"""
    TV = "TV"
    ONA = "ONA"
    WEB = "WEB"
    OVA = "OVA"
    OAD = "OAD"
    MOVIE = "MOVIE"
    DORAMA = "DORAMA"
    SPECIAL = "SPECIAL"

class AgeRating(Enum):
    """Возрастные рейтинги"""
    R0_PLUS = "R0_PLUS"
    R6_PLUS = "R6_PLUS"
    R12_PLUS = "R12_PLUS"
    R16_PLUS = "R16_PLUS"
    R18_PLUS = "R18_PLUS"

class Seasons(Enum):
    """Сезоны"""
    WINTER = "winter"
    SPRING = "spring"
    SUMMER = "summer"
    AUTUMN = "autumn"

class SortType(Enum):
    """Тип сортировки"""
    FRESH_AT_DESC = "FRESH_AT_DESC"
    FRESH_AT_ASC = "FRESH_AT_ASC"
    RATING_DESC = "RATING_DESC"
    RATING_ASC = "RATING_ASC"
    YEAR_DESC = "YEAR_DESC"
    YEAR_ASC = "YEAR_ASC"

class PublishStatusesType(Enum):
    """Статус аниме (онгоинг)"""
    IS_ONGOING = "IS_ONGOING"
    IS_NOT_ONGOING = "IS_NOT_ONGOING"

class ProductionStatusesType(Enum):
    """Статус аниме (в озвучке)"""
    IS_IN_PRODUCTION = "IS_IN_PRODUCTION"
    IS_NOT_IN_PRODUCTION = "IS_NOT_IN_PRODUCTION"