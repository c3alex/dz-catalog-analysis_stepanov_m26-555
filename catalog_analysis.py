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


# ---------- Этап 1: числа и math ----------


def average_rating(movies):
    """Средняя оценка каталога, округлённая до одного знака."""
    total = sum(m["rating"] for m in movies)
    return round(total / len(movies), 1)


def catalog_age_stats(movies, current_year=2026):
    """Кортеж (самый старый, самый новый, средний возраст вверх до целого)."""
    ages = [current_year - m["year"] for m in movies]
    return (max(ages), min(ages), math.ceil(sum(ages) / len(ages)))


def duration_in_hours(minutes):
    """Минуты в строку вида "2ч 35м" через // и %."""
    return f"{minutes // 60}ч {minutes % 60}м"


# ---------- Этап 2: условия и match ----------


def rating_tier(rating):
    """Категория фильма по оценке (if/elif + тернарный оператор)."""
    if rating >= 9:
        return "шедевр"
    elif rating >= 7:
        return "хорошо"
    # тернарный оператор для нижней части шкалы
    return "средне" if rating >= 5 else "слабо"


def decade_label(year):
    """Метка эпохи через match с диапазонами."""
    match year:
        case _ if year > 2020:
            return "новые"
        case _ if year >= 2015:
            return "недавние"
        case _:
            return "старые"


# ---------- Этап 3: циклы ----------


def find_first_above(movies, threshold=9.0):
    """while + break: первый фильм с рейтингом выше порога."""
    index = 0
    while index < len(movies):
        if movies[index]["rating"] > threshold:
            print(f"Первый фильм с рейтингом > {threshold}: {movies[index]['title']}")
            break
        index += 1
    else:
        # сюда попадаем, если break не сработал
        print("Шедевров не найдено")


def count_long_movies(movies, threshold=120):
    """Считает фильмы длиннее порога через накопление в цикле."""
    count = 0
    for movie in movies:
        if movie["duration_min"] > threshold:
            count += 1
    return count


# ---------- Этап 4: строки ----------


def normalize_title(title):
    """Title Case вручную, без str.title()."""
    return " ".join(word[0].upper() + word[1:] for word in title.split())


def make_slug(title):
    """Слаг вида the-quiet-algorithm."""
    return title.lower().replace(" ", "-")


def format_report_line(movie):
    """Строка отчёта об одном фильме."""
    genres = ", ".join(sorted(movie["genres"]))
    return (
        f'"{normalize_title(movie["title"])}" ({movie["year"]}) — '
        f"{movie['rating']}/10, {duration_in_hours(movie['duration_min'])}, "
        f"жанры: {genres}"
    )


# ---------- Этап 5: списки ----------


def titles_sorted_by_rating(movies):
    """Названия фильмов по убыванию рейтинга (исходный список не меняется)."""
    ordered = sorted(movies, key=lambda m: m["rating"], reverse=True)
    return [m["title"] for m in ordered]


def top_n_by_rating(movies, n=3):
    """Топ-n фильмов как список кортежей (title, rating)."""
    ordered = sorted(movies, key=lambda m: m["rating"], reverse=True)
    return [(m["title"], m["rating"]) for m in ordered[:n]]


# ---------- Этап 6: словари ----------


def count_by_genre(movies):
    """Словарь {жанр: количество фильмов} вручную, без Counter."""
    counts = {}
    for movie in movies:
        for genre in movie["genres"]:
            counts[genre] = counts.get(genre, 0) + 1
    return counts


def actor_filmography(movies):
    """Словарь {актёр: [названия фильмов]}."""
    filmography = {}
    for movie in movies:
        for actor in movie["actors"]:
            filmography.setdefault(actor, []).append(movie["title"])
    return filmography


def above_average_ratings(movies):
    """{title: rating} только для фильмов с рейтингом выше среднего."""
    avg = average_rating(movies)
    return {m["title"]: m["rating"] for m in movies if m["rating"] > avg}


# ---------- Этап 7: множества ----------


def all_genres(movies):
    """Множество всех жанров каталога (объединение)."""
    genres = set()
    for movie in movies:
        genres |= movie["genres"]
    return genres


def common_actors(movie1, movie2):
    """Актёры, снимавшиеся в обоих фильмах (пересечение)."""
    return set(movie1["actors"]) & set(movie2["actors"])


def genres_only_in_one(movies_a, movies_b):
    """Жанры из movies_a, которых нет в movies_b (разность)."""
    return all_genres(movies_a) - all_genres(movies_b)


# ---------- Этап 8: итераторы и генераторы ----------


def iter_high_rated(movies, min_rating=8.0):
    """Ленивый генератор фильмов с рейтингом не ниже min_rating."""
    for movie in movies:
        if movie["rating"] >= min_rating:
            yield movie


# ---------- Этап 9: итоговый отчёт ----------


def build_report(movies):
    """Печатает полный отчёт по каталогу: одна точка входа."""
    _, _, avg_age = catalog_age_stats(movies)

    print("ОТЧЕТ ПО КАТАЛОГУ")
    print(f"Средний рейтинг: {average_rating(movies)}")
    print(f"Средний возраст фильмов: {avg_age} лет\n")

    print("Топ-3 фильма:")
    for title, _ in top_n_by_rating(movies, 3):
        movie = next(m for m in movies if m["title"] == title)
        print(f"  {format_report_line(movie)}")

    # жанры: сначала по убыванию количества, затем по алфавиту
    print("\nФильмов по жанрам:")
    for genre, count in sorted(
        count_by_genre(movies).items(), key=lambda item: (-item[1], item[0])
    ):
        print(f"  {genre} — {count}")

    print("\nВсе жанры каталога: " + ", ".join(sorted(all_genres(movies))))


if __name__ == "__main__":
    # Этап 3: for + continue — фильмы без жанра comedy
    for movie in movies:
        if "comedy" in movie["genres"]:
            continue
        print(movie["title"])

    # while + break: сначала порог 9.0 (найдём), потом 10.0 (не найдём)
    find_first_above(movies, 9.0)
    find_first_above(movies, 10.0)
    print("Длинных фильмов (>120 мин):", count_long_movies(movies))

    # Этап 4: примеры строк
    print(normalize_title("silent hours"))
    print(make_slug("Silent Hours"))
    print(format_report_line(movies[7]))

    # Этап 5-7: примеры
    print(top_n_by_rating(movies, 3))
    print(count_by_genre(movies))
    print(common_actors(movies[0], movies[3]))
    print(genres_only_in_one(movies[5:6], movies[:5]))
    print(above_average_ratings(movies))

    # Этап 8: генератор и генераторное выражение
    for movie in iter_high_rated(movies):
        print(format_report_line(movie))
    print(sum(m["duration_min"] for m in movies if m["rating"] > 7))

    # Этап 9: итоговый отчёт
    build_report(movies)
