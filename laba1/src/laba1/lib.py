def calculate_area(width: float, height: float) -> float:
    """
    Обчислює площу прямокутника за заданою шириною та висотою.
    
    Args:
        width (float): Ширина прямокутника.
        height (float): Висота прямокутника.
        
    Returns:
        float: Площа прямокутника.
    """
    return width * height

def calculate_perimeter(width: float, height: float) -> float:
    """
    Обчислює периметр прямокутника.
    
    Args:
        width (float): Ширина прямокутника.
        height (float): Висота прямокутника.
        
    Returns:
        float: Периметр прямокутника.
    """
    return 2 * (width + height)
