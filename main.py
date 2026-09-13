from lib import calculate_area, calculate_perimeter

def main():
    """
    Головна функція програми. Демонструє роботу імпортованих 
    модулів шляхом виклику функцій та виведення результату.
    """
    try:
        w = float(input("Введіть ширину прямокутника (w): "))
        h = float(input("Введіть висоту прямокутника (h): "))
    except ValueError:
        print("Помилка: потрібно ввести число!")
        return
    
    area = calculate_area(w, h)
    perimeter = calculate_perimeter(w, h)
    
    print(f"Прямокутник зі сторонами {w} та {h}:")
    print(f"Площа: {area}")
    print(f"Периметр: {perimeter}")

if __name__ == "__main__":
    main()
