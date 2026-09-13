# Лабораторна робота №1

## UML Діаграма компонентів

Нижче наведена діаграма, яка показує внутрішню структуру Python-скрипту, його методи та зв’язки між ними:

```mermaid
flowchart TD
    %% Актори та зовнішня взаємодія
    User((Користувач))
    
    subgraph Скрипт main.py
        direction TB
        Main[Функція main]
        Input[Ввід даних з консолі]
        Validation{Перевірка: w > 0, h > 0}
        Output[Вивід результатів на екран]
    end

    subgraph Модуль lib.py
        direction TB
        Area[calculate_area w, h]
        Perim[calculate_perimeter w, h]
    end

    %% Логічні зв'язки та потік виконання
    User -->|Вводить ширину та висоту| Input
    Input --> Validation
    Validation -->|Невалідні дані| Input
    Validation -->|Дані коректні| Main
    
    Main -->|Виклик функції| Area
    Main -->|Виклик функції| Perim
    
    Area -->|Повертає площу| Main
    Perim -->|Повертає периметр| Main
    
    Main --> Output
    Output --> User
```
