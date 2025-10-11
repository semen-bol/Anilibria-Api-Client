class AnilibriaException(Exception):
    """Общий класс для валидации ошибок"""
    pass

class AnilibriaValidationException(AnilibriaException):
    """Ошибка валидации на стороне Anilibria"""
    pass