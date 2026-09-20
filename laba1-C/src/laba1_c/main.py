import lib

def main():
    print("--- Проста програма ---")
    x = 10.5
    y = 2.0
    
    sum_result = lib.add(x, y)
    mult_result = lib.multiply(x, y)
    
    print(f"Сума {x} та {y} дорівнює {sum_result}")
    print(f"Добуток {x} та {y} дорівнює {mult_result}")
    print("--- Кінець ---")

if __name__ == "__main__":
    main()
