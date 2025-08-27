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