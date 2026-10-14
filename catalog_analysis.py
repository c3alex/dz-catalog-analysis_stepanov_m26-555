import math

# Исходные данные каталога
movies = [
    {"title": "The Dune Chronicles", "year": 2021, "genres": {"sci-fi", "drama"},
     "rating": 8.6, "duration_min": 155, "actors": ["T. Chalamet", "R. Ferguson", "O. Isaac"]},
    {"title": "Kitchen Stories", "year": 2019, "genres": {"comedy", "drama"},
     "rating": 7.1, "duration_min": 98, "actors": ["A. Novak", "M. Ferguson"]},
    {"title": "silent hours", "year": 2016, "genres": {"thriller", "drama"},
     "rating": 6.4, "duration_min": 112, "actors": ["J. Bloom", "K. Lee"]},
    {"title": "Comet Racers", "year": 2023, "genres": {"sci-fi", "action"},
     "rating": 5.9, "duration_min": 101, "actors": ["O. Isaac", "P. Diaz"]},
    {"title": "The Last Bakery", "year": 2014, "genres": {"comedy"},
     "rating": 7.8, "duration_min": 89, "actors": ["A. Novak", "T. Chalamet"]},
    {"title": "midnight in oslo", "year": 2020, "genres": {"thriller", "mystery"},
     "rating": 8.9, "duration_min": 124, "actors": ["K. Lee", "R. Ferguson"]},
    {"title": "Garden of Static", "year": 2022, "genres": {"drama"},
     "rating": 4.8, "duration_min": 137, "actors": ["P. Diaz", "J. Bloom"]},
    {"title": "The Quiet Algorithm", "year": 2024, "genres": {"sci-fi", "drama"},
     "rating": 9.2, "duration_min": 118, "actors": ["M. Ferguson", "O. Isaac"]},
    {"title": "Two Left Shoes", "year": 2011, "genres": {"comedy"},
     "rating": 6.0, "duration_min": 95, "actors": ["A. Novak", "K. Lee"]},
    {"title": "Red Harbor", "year": 2018, "genres": {"action", "thriller"},
     "rating": 7.3, "duration_min": 129, "actors": ["P. Diaz", "T. Chalamet"]},
]

def average_rating(movies):
    """
    Возвращает среднюю оценку всех фильмов, округлённую до одного знака.
    Если список пуст — возвращаем 0.0.
    """
    if not movies:
        return 0.0
    total = sum(m.get("rating", 0) for m in movies)
    return round(total / len(movies), 1)

def catalog_age_stats(movies, current_year=2026):
    """
    Возвращает кортеж: (самый старый фильм в годах,
                         самый новый фильм в годах,
                         средний возраст, округлённый в большую сторону).
    Для среднего используем ``math.ceil``.
    Пустой список → (0, 0, 0).
    """
    if not movies:
        return (0, 0, 0)
    ages = [current_year - m.get("year", current_year) for m in movies]
    oldest = max(ages)          # максимальный возраст
    newest = min(ages)          # минимальный возраст
    average = math.ceil(sum(ages) / len(ages))
    return (oldest, newest, average)

def duration_in_hours(minutes):
    """
    Переводит количество минут в строку вида «2ч 35м».
    Используем целочисленное деление // для часов
    и остаток % для оставшихся минут.
    """
    hours = minutes // 60
    mins = minutes % 60
    return f"{hours}ч {mins}м"


def rating_tier(rating):
    """Возвращает категорию фильма по его оценке.
    
    • "шедевр" – rating ≥ 9
    • "хорошо"  – 7 ≤ rating < 9
    • "средне" – 5 ≤ rating < 7
    • "слабо"   – rating < 5
    
    Реализовано через if/elif, внутри используется тернарный оператор.
    """
    if rating >= 9:
        return "шедевр"
    elif rating >= 7:
        # Тернарный оператор в качестве примера; здесь он просто возвращает строку "хорошо"
        return "хорошо" if rating < 8.5 else "хорошо"
    elif rating >= 5:
        return "средне"
    else:
        return "слабо"


def decade_label(year):
    """Возвращает метку в зависимости от года выпуска фильма.
    
    • "новые"    – после 2020 года (year > 2020)
    • "недавние" – 2015‑2020 включительно
    • "старые"   – до 2015 года (year < 2015)
    
    Реализовано через оператор match с условиями ``case _ if ...``.
    """
    match year:
        case _ if year > 2020:
            return "новые"
        case _ if 2015 <= year <= 2020:
            return "недавние"
        case _:
            return "старые"
