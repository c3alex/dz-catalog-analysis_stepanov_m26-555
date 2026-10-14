"""Анализ каталога фильмов: версия 2 с полными docstring и аннотациями типов.

Модуль решает домашнее задание по этапам 1-9:
числа и math, условия и match, циклы, строки, списки,
словари, множества, генераторы и итоговый отчёт.
"""

import math
from collections.abc import Iterator
from typing import Any

# Псевдоним типа одного фильма каталога
Movie = dict[str, Any]

# Исходные данные каталога
movies: list[Movie] = [
    {"title": "The Dune Chronicles", "year": 2021, "genres": {"sci-fi", "drama"},
     "rating": 8.6, "duration_min": 155,
     "actors": ["T. Chalamet", "R. Ferguson", "O. Isaac"]},
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


def average_rating(movies: list[Movie]) -> float:
    """Средняя оценка всех фильмов каталога.

    Аргументы:
        movies: список словарей; в каждом словаре есть ключ "rating" (число).

    Возвращает:
        float: среднее оценок, округлённое до одного знака через round().

    Побочные эффекты: нет, каталог не изменяется.
    Ограничения: пустой список вернёт 0.0 (защита от деления на ноль).
    """
    if not movies:
        return 0.0
    total = sum(m["rating"] for m in movies)
    return round(total / len(movies), 1)


def catalog_age_stats(
    movies: list[Movie], current_year: int = 2026
) -> tuple[int, int, int]:
    """Статистика возраста фильмов каталога.

    Аргументы:
        movies: список словарей с ключом "year" (год выпуска, int).
        current_year: текущий год, от него считается возраст (по умолчанию 2026).

    Возвращает:
        tuple: (возраст самого старого, самого нового, средний возраст).
        Среднее округлено вверх до целого через math.ceil.

    Побочные эффекты: нет.
    Ограничения: пустой список вернёт (0, 0, 0);
    годы выпуска должны быть не больше current_year.
    """
    if not movies:
        return (0, 0, 0)
    ages = [current_year - m["year"] for m in movies]
    # кортеж — неизменяемая запись результата
    return (max(ages), min(ages), math.ceil(sum(ages) / len(ages)))


def duration_in_hours(minutes: int) -> str:
    """Переводит минуты в строку вида "2ч 35м".

    Аргументы:
        minutes: длительность в минутах (неотрицательное число).

    Возвращает:
        str: часы и минуты, вычисленные через // и %.

    Побочные эффекты: нет.
    Ограничения: для отрицательных значений результат не определён.
    """
    return f"{minutes // 60}ч {minutes % 60}м"


# ---------- Этап 2: условия и match ----------


def rating_tier(rating: float) -> str:
    """Категория фильма по оценке.

    Аргументы:
        rating: число от 0 до 10.

    Возвращает:
        str: "шедевр" (>=9), "хорошо" (7-8.9), "средне" (5-6.9), "слабо" (<5).

    Побочные эффекты: нет.
    Ограничения: границы диапазонов не пересекаются,
    вне диапазона 0-10 поведение не оговорено заданием.
    """
    if rating >= 9:
        return "шедевр"
    elif rating >= 7:
        return "хорошо"
    # тернарный оператор для нижней половины шкалы
    return "средне" if rating >= 5 else "слабо"


def decade_label(year: int) -> str:
    """Метка эпохи фильма через match.

    Аргументы:
        year: год выпуска фильма (int).

    Возвращает:
        str: "новые" (после 2020), "недавние" (2015-2020), "старые" (до 2015).

    Побочные эффекты: нет.
    Ограничения: диапазоны заданы через case _ if и покрывают
    весь числовой промежуток без потерь граничных значений.
    """
    match year:
        case _ if year > 2020:
            return "новые"
        case _ if 2015 <= year <= 2020:
            return "недавние"
        case _:
            return "старые"


# ---------- Этап 3: циклы ----------


def find_first_masterpiece(movies: list[Movie], threshold: float = 9.0) -> None:
    """Ищет первый фильм с рейтингом выше порога (while + break).

    Аргументы:
        movies: список словарей с ключом "rating".
        threshold: порог рейтинга (по умолчанию 9.0).

    Возвращает:
        None: результат печатается в консоль.

    Побочные эффекты: печатает название найденного фильма
    или сообщение "Шедевров не найдено" из ветки else цикла.
    Ограничения: ветка else срабатывает только если break не был вызван.
    """
    index = 0
    while index < len(movies):
        if movies[index]["rating"] > threshold:
            print(f"Первый фильм с рейтингом > {threshold}: {movies[index]['title']}")
            break
        index += 1
    else:
        # цикл закончился сам, без break — шедевра нет
        print("Шедевров не найдено")


def count_long_movies(movies: list[Movie], threshold: int = 120) -> int:
    """Считает фильмы длиннее порога через накопление в цикле.

    Аргументы:
        movies: список словарей с ключом "duration_min".
        threshold: порог длительности в минутах (по умолчанию 120).

    Возвращает:
        int: количество фильмов строго длиннее threshold.

    Побочные эффекты: нет.
    Ограничения: без sum() по списку-фильтру — только счётчик в цикле for.
    """
    count = 0
    for movie in movies:
        if movie["duration_min"] > threshold:
            count += 1
    return count


# ---------- Этап 4: строки ----------


def normalize_title(title: str) -> str:
    """Приводит строку к Title Case вручную.

    Аргументы:
        title: название фильма со словами через пробел.

    Возвращает:
        str: каждое слово с заглавной первой буквой
        (срез word[0].upper() + word[1:], без str.title()).

    Побочные эффекты: нет.
    Ограничения: исходная строка не изменяется (строки неизменяемы);
    регистр остальных букв слова сохраняется.
    """
    return " ".join(word[0].upper() + word[1:] for word in title.split())


def make_slug(title: str) -> str:
    """Делает слаг из названия: "the-quiet-algorithm".

    Аргументы:
        title: нормализованное название фильма.

    Возвращает:
        str: нижний регистр, пробелы заменены на дефис (.lower + .replace).

    Побочные эффекты: нет.
    Ограничения: посторонние символы (знаки препинания) не убираются.
    """
    return title.lower().replace(" ", "-")


def format_report_line(movie: Movie) -> str:
    """Собирает строку-отчёт об одном фильме.

    Аргументы:
        movie: словарь с ключами "title", "year", "rating",
        "duration_min" и "genres".

    Возвращает:
        str: '"The Quiet Algorithm" (2024) — 9.2/10, 1ч 58м, жанры: ...'
        Длительность переводится вызовом duration_in_hours (этап 1),
        жанры отсортированы по алфавиту, сборка через f-строку.

    Побочные эффекты: нет.
    Ограничения: ожидается корректно заполненный словарь фильма.
    """
    genres = ", ".join(sorted(movie["genres"]))
    return (
        f'"{normalize_title(movie["title"])}" ({movie["year"]}) — '
        f'{movie["rating"]}/10, {duration_in_hours(movie["duration_min"])}, '
        f"жанры: {genres}"
    )


# ---------- Этап 5: списки ----------


def titles_sorted_by_rating(movies: list[Movie]) -> list[str]:
    """Названия фильмов по убыванию рейтинга.

    Аргументы:
        movies: список словарей с ключами "title" и "rating".

    Возвращает:
        list[str]: названия, отсортированные через sorted(key=..., reverse=True).

    Побочные эффекты: нет, исходный список movies не изменяется.
    Ограничения: порядок равных по рейтингу фильмов устойчив (stable sort).
    """
    ordered = sorted(movies, key=lambda m: m["rating"], reverse=True)
    return [m["title"] for m in ordered]


def top_n_by_rating(movies: list[Movie], n: int = 3) -> list[tuple[str, float]]:
    """Топ-n фильмов по рейтингу.

    Аргументы:
        movies: список словарей с ключами "title" и "rating".
        n: размер топа (по умолчанию 3).

    Возвращает:
        list[tuple]: кортежи (title, rating), отсортированные по убыванию.

    Побочные эффекты: нет.
    Ограничения: при n больше длины каталога вернутся все фильмы.
    """
    ordered = sorted(movies, key=lambda m: m["rating"], reverse=True)
    return [(m["title"], m["rating"]) for m in ordered[:n]]


# ---------- Этап 6: словари ----------


def count_by_genre(movies: list[Movie]) -> dict[str, int]:
    """Считает фильмы по каждому жанру.

    Аргументы:
        movies: список словарей с ключом "genres" (множество строк).

    Возвращает:
        dict: {жанр: количество фильмов}, построен вручную
        через цикл и dict.get(genre, 0), без Counter.

    Побочные эффекты: нет.
    Ограничения: фильм с несколькими жанрами учитывается в каждом из них.
    """
    counts: dict[str, int] = {}
    for movie in movies:
        for genre in movie["genres"]:
            counts[genre] = counts.get(genre, 0) + 1
    return counts


def actor_filmography(movies: list[Movie]) -> dict[str, list[str]]:
    """Строит фильмографию актёров.

    Аргументы:
        movies: список словарей с ключами "actors" и "title".

    Возвращает:
        dict: {актёр: [список названий фильмов]}.

    Побочные эффекты: нет.
    Ограничения: порядок фильмов каждого актёра совпадает
    с порядком в каталоге; повторов в "actors" одного фильма быть не должно.
    """
    filmography: dict[str, list[str]] = {}
    for movie in movies:
        for actor in movie["actors"]:
            # пустой список по умолчанию через get
            filmography.setdefault(actor, []).append(movie["title"])
    return filmography


def above_average_ratings(movies: list[Movie]) -> dict[str, float]:
    """Рейтинги фильмов выше среднего по каталогу.

    Аргументы:
        movies: список словарей с ключами "title" и "rating".

    Возвращает:
        dict: {title: rating} только для фильмов с оценкой строго выше
        среднего (среднее берётся из average_rating этапа 1).
        Построен генератором словаря, без цикла с присваиванием.

    Побочные эффекты: нет.
    Ограничения: пустой каталог даст пустой словарь.
    """
    avg = average_rating(movies)
    return {m["title"]: m["rating"] for m in movies if m["rating"] > avg}


# ---------- Этап 7: множества ----------


def all_genres(movies: list[Movie]) -> set[str]:
    """Множество всех уникальных жанров каталога.

    Аргументы:
        movies: список словарей с ключом "genres".

    Возвращает:
        set: объединение множеств жанров всех фильмов (оператор |).

    Побочные эффекты: нет.
    Ограничения: порядок элементов не гарантирован.
    """
    genres: set[str] = set()
    for movie in movies:
        genres |= movie["genres"]
    return genres


def common_actors(movie1: Movie, movie2: Movie) -> set[str]:
    """Актёры, снимавшиеся в обоих фильмах.

    Аргументы:
        movie1, movie2: словари фильмов с ключом "actors".

    Возвращает:
        set: пересечение множеств актёров (оператор &).

    Побочные эффекты: нет.
    Ограничения: пустое множество означает отсутствие общих актёров.
    """
    return set(movie1["actors"]) & set(movie2["actors"])


def genres_only_in_one(movies_a: list[Movie], movies_b: list[Movie]) -> set[str]:
    """Жанры из первого списка, которых нет во втором.

    Аргументы:
        movies_a, movies_b: два списка фильмов с ключом "genres".

    Возвращает:
        set: разность множеств жанров (all_genres(movies_a) - all_genres(movies_b)).

    Побочные эффекты: нет.
    Ограничения: результат не зависит от порядка фильмов внутри списков.
    """
    return all_genres(movies_a) - all_genres(movies_b)


# ---------- Этап 8: итераторы и генераторы ----------


def iter_high_rated(
    movies: list[Movie], min_rating: float = 8.0
) -> Iterator[Movie]:
    """Лениво выдаёт фильмы с рейтингом не ниже порога.

    Аргументы:
        movies: список словарей с ключом "rating".
        min_rating: минимальный рейтинг (по умолчанию 8.0).

    Возвращает:
        Iterator[Movie]: фильмы по одному через yield, без готового списка.

    Побочные эффекты: нет (элементы вычисляются по запросу).
    Ограничения: генератор одноразовый — после исчерпания
    повторный обход требует нового вызова функции.
    """
    for movie in movies:
        if movie["rating"] >= min_rating:
            yield movie


# ---------- Этап 9: итоговый отчёт ----------


def build_report(movies: list[Movie]) -> None:
    """Печатает полный отчёт по каталогу (единая точка входа).

    Аргументы:
        movies: список словарей фильмов каталога.

    Возвращает:
        None: весь отчёт выводится в консоль — общая статистика,
        топ-3 фильма, количество фильмов по жанрам (по убыванию)
        и полный список жанров одной строкой через ", ".join(...).

    Побочные эффекты: только печать, каталог не изменяется.
    Ограничения: функция только собирает вызовы готовых функций
    этапов 1-8, самостоятельных вычислений почти не содержит.
    """
    _, _, avg_age = catalog_age_stats(movies)

    print("ОТЧЕТ ПО КАТАЛОГУ")
    print(f"Средний рейтинг: {average_rating(movies)}")
    print(f"Средний возраст фильмов: {avg_age} лет\n")

    # топ-3: ищем фильм по названию из кортежа
    print("Топ-3 фильма:")
    for title, _ in top_n_by_rating(movies, 3):
        movie = next(m for m in movies if m["title"] == title)
        print(f"  {format_report_line(movie)}")

    # жанры по убыванию количества, при равенстве — по алфавиту
    print("\nФильмов по жанрам:")
    for genre, count in sorted(
        count_by_genre(movies).items(), key=lambda item: (-item[1], item[0])
    ):
        print(f"  {genre} — {count}")

    print("\nВсе жанры каталога: " + ", ".join(sorted(all_genres(movies))))


if __name__ == "__main__":
    # Этап 3: for + continue — названия фильмов не из жанра comedy
    for movie in movies:
        if "comedy" in movie["genres"]:
            continue
        print(movie["title"])

    # while + break + else: сначала находим фильм, потом проверяем ветку else
    find_first_masterpiece(movies, 9.0)
    find_first_masterpiece(movies, 10.0)
    print("Длинных фильмов (>120 мин):", count_long_movies(movies))

    # Этап 4: примеры работы со строками
    print(normalize_title("silent hours"))
    print(make_slug("Silent Hours"))
    print(format_report_line(movies[7]))

    # Этап 5-7: списки, словари, множества
    print(top_n_by_rating(movies, 3))
    print(count_by_genre(movies))
    print(common_actors(movies[0], movies[3]))
    print(genres_only_in_one(movies[5:6], movies[:5]))
    print(above_average_ratings(movies))

    # Этап 8: генератор + генераторное выражение внутри sum()
    for movie in iter_high_rated(movies):
        print(format_report_line(movie))
    print(sum(m["duration_min"] for m in movies if m["rating"] > 7))

    # Этап 9: итоговый отчёт одним вызовом
    build_report(movies)
