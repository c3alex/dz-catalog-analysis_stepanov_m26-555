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

def normalize_title(title: str) -> str:
    """Приводит строку к формату Title Case без использования str.title()."""
    words = title.split()
    title_cased = [word[0].upper() + word[1:] if word else '' for word in words]
    return ' '.join(title_cased)

def make_slug(title: str) -> str:
    """Создаёт слаг из нормализованного названия."""
    return title.lower().replace(' ', '-')

def format_report_line(movie: dict) -> str:
    """Формирует строку‑отчёт о фильме."""
    title = normalize_title(movie.get('title', ''))
    year = movie.get('year', '')
    rating = movie.get('rating', 0)
    duration = duration_in_hours(movie.get('duration_min', 0))
    genres = sorted(movie.get('genres', []))
    genres_str = ', '.join(genres)
    return f'"{title}" ({year}) — {rating}/10, {duration}, жанры: {genres_str}'



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

# Демонстрация работы с циклами

# 1. for с continue – выводим названия фильмов, не относящихся к жанру "comedy"
for movie in movies:
    if "comedy" in movie.get("genres", set()):
        continue
    print(movie["title"])

# 2. while с break – ищем первый фильм с рейтингом выше 9.0
index = 0
while index < len(movies):
    if movies[index].get("rating", 0) > 9.0:
        print(f"Первый шедевр: {movies[index]['title']}")
        break
    index += 1
else:
    print("Шедевров не найдено")

# 2b. while с break, но условие заведомо невозможно – демонстрируем ветку else
index = 0
while index < len(movies):
    if movies[index].get("rating", 0) > 10.0:  # такого фильма нет
        print(f"Найдено: {movies[index]["title"]}")
        break
    index += 1
else:
    print("Шедевров не найдено (вторая проверка)")

def top_n_by_rating(movies, n=3) -> list:
    """Возвращает список из `n` кортежей (title, rating) топ‑фильмов по рейтингу.
    Сортировка делается через `sorted` с `key=lambda m: m.get('rating', 0)`.
    """
    # Сортируем копию списка, не меняя оригинал
    sorted_movies = sorted(movies, key=lambda m: m.get('rating', 0), reverse=True)
    # Формируем список из первых n элементов в виде кортежей
    return [(movie.get('title', ''), movie.get('rating', 0)) for movie in sorted_movies[:n]]

def titles_sorted_by_rating(movies) -> list:
    """Возвращает список названий фильмов, отсортированных по убыванию рейтинга.
    Исходный список `movies` не изменяется.
    """
    sorted_movies = sorted(movies, key=lambda m: m.get('rating', 0), reverse=True)
    return [movie.get('title', '') for movie in sorted_movies]

def count_long_movies(movies, threshold=120):
    """Подсчитывает количество фильмов длительностью более *threshold* минут.
    Делается через простой цикл for и накопительную переменную.
    """
    count = 0
    for movie in movies:
        if movie.get("duration_min", 0) > threshold:
            count += 1
    return count


def count_by_genre(movies) -> dict:
    """Подсчитывает количество фильмов по каждому жанру.
    Используется цикл и `dict.get()` без `collections.Counter`.
    """
    genre_counts = {}
    for movie in movies:
        for genre in movie.get('genres', []):
            genre_counts[genre] = genre_counts.get(genre, 0) + 1
    return genre_counts


def actor_filmography(movies) -> dict:
    """Возвращает словарь, где ключ – имя актёра, а значение – список названий фильмов,
    в которых он/она снялся(ась).
    """
    filmography = {}
    for movie in movies:
        title = movie.get('title', '')
        for actor in movie.get('actors', []):
            current = filmography.get(actor, [])
            current.append(title)
            filmography[actor] = current
    return filmography



def all_genres(movies) -> set:
    """Возвращает множество всех уникальных жанров каталога."""
    genres = set()
    for movie in movies:
        genres.update(movie.get('genres', []))
    return genres

def common_actors(movie1: dict, movie2: dict) -> set:
    """Возвращает множество актёров, снявшихся в обоих фильмах (пересечение)."""
    actors1 = set(movie1.get('actors', []))
    actors2 = set(movie2.get('actors', []))
    return actors1 & actors2

def genres_only_in_one(movies_a, movies_b) -> set:
    """Возвращает жанры, присутствующие в `movies_a`, но отсутствующие в `movies_b` (разность)."""
    genres_a = set()
    for movie in movies_a:
        genres_a.update(movie.get('genres', []))
    genres_b = set()
    for movie in movies_b:
        genres_b.update(movie.get('genres', []))
    return genres_a - genres_b

def iter_high_rated(movies, min_rating=8.0):
    """Генератор, лениво выдающий фильмы с рейтингом >= `min_rating`.
    Пример использования:
        for movie in iter_high_rated(movies):
            print(format_report_line(movie))
    """
    for movie in movies:
        if movie.get('rating', 0) >= min_rating:
            yield movie

# Пример суммирования длительности всех фильмов с рейтингом выше 7 (генераторное выражение)
# total_minutes = sum(m['duration_min'] for m in movies if m.get('rating', 0) > 7)

def build_report(movies):
    """Выводит единый консольный отчёт по каталогу.
    Формат соответствует требованию задачи.
    """
    # 1. Общая статистика
    avg_rating = average_rating(movies)
    # catalog_age_stats возвращает (oldest, newest, average_age_ceil)
    _, _, avg_age = catalog_age_stats(movies)

    # 2. Топ‑3 фильма
    top3 = top_n_by_rating(movies, n=3)
    top3_lines = []
    for title, rating in top3:
        film = next((m for m in movies if m.get('title') == title), None)
        if film:
            top3_lines.append(f"  {format_report_line(film)}")

    # 3. Количество фильмов по жанрам – сортируем по убыванию количества
    genre_counts = count_by_genre(movies)
    sorted_genres = sorted(genre_counts.items(), key=lambda item: item[1], reverse=True)
    genre_lines = [f"  {genre} — {count}" for genre, count in sorted_genres]

    # 4. Список всех уникальных жанров – в алфавитном порядке
    all_genres_set = all_genres(movies)
    all_genres_list = sorted(all_genres_set)
    all_genres_str = ", ".join(all_genres_list)

    # Формируем и выводим отчёт
    print("ОТЧЕТ ПО КАТАЛОГУ")
    print(f"Средний рейтинг: {avg_rating}")
    print(f"Средний возраст фильмов: {avg_age} лет\n")
    print("Топ-3 фильма:")
    for line in top3_lines:
        print(line)
    print("\nФильмов по жанрам:")
    for line in genre_lines:
        print(line)
    print("\nВсе жанры каталога: " + all_genres_str)

