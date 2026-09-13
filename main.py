from lib import calculate_area, calculate_perimeter

def main():
    """
    Головна функція програми. Демонструє роботу імпортованих 
    модулів шляхом виклику функцій та виведення результату.
    """
    while True:
        try:
            w = float(input("Введіть ширину прямокутника (w): "))
            if w <= 0:
                print("Помилка: ширина повинна бути більшою за 0!")
                continue
                
            h = float(input("Введіть висоту прямокутника (h): "))
            if h <= 0:
                print("Помилка: висота повинна бути більшою за 0!")
                continue
                
            break
            
        except ValueError:
            print("Помилка: потрібно ввести числове значення!")
    
    area = calculate_area(w, h)
    perimeter = calculate_perimeter(w, h)
    
    print(f"Прямокутник зі сторонами {w} та {h}:")
    print(f"Площа: {area}")
    print(f"Периметр: {perimeter}")

if __name__ == "__main__":
    main()
