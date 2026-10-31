catalog = [
    {"title": "Мастер и Маргарита", "author": "Булгаков",
     "year": 1967, "genre": "роман", "on_loan": True},
    {"title": "Евгений Онегин", "author": "Пушкин",
     "year": 1833, "genre": "роман", "on_loan": False},
    {"title": "Стихотворения", "author": "Есенин",
     "year": 1926, "genre": "поэзия", "on_loan": False},
    {"title": "Вишнёвый сад", "author": "Чехов",
     "year": 1904, "genre": "пьеса", "on_loan": True},
    {"title": "Руслан и Людмила", "author": "Пушкин",
     "year": 1820, "genre": "поэма", "on_loan": False},
    {"title": "Три сестры", "author": "Чехов",
     "year": 1901, "genre": "пьеса", "on_loan": False},
]


def find_by_author(c, a):
    return [b["title"] for b in c if b["author"] == a]


def available_titles(c):
    return [b["title"] for b in c if not b["on_loan"]]


def books_grouped_by_genre(c):
    d = {}
    for b in c:
        if b["genre"] not in d:
            d[b["genre"]] = []
        if not b["on_loan"]:
            d[b["genre"]].append(b["title"])
    return d


print(find_by_author(catalog, "Пушкин"))
print(available_titles(catalog))
print(books_grouped_by_genre(catalog))
