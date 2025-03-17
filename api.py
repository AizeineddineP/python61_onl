import requests

API_KEY = "dda5c41f"
MOVIE_TITLE = "Inception"

url = f"http://www.omdbapi.com/?apikey={API_KEY}&t={MOVIE_TITLE}"
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    if "Error" in data:
        print("Ошибка:", data["Error"])
    else:
        print(f"Название: {data['Title']}")
        print(f"Год выпуска: {data['Year']}")
        print(f"Жанр: {data['Genre']}")
        print(f"Рейтинг IMDb: {data['imdbRating']}")
else:
    print("Ошибка при получении данных!")
if "Action" in data["Genre"]:
    print(f"Фильм '{data['Title']}' относится к жанру Action!")
else:
    print(f"Фильм '{data['Title']}' не является Action.")

import requests

API_KEY = "dda5c41f"
SEARCH_TERM = "Batman"

url = f"http://www.omdbapi.com/?apikey={API_KEY}&s={SEARCH_TERM}&type=movie"
response = requests.get(url)

if response.status_code == 200:
    data = response.json()

    if "Search" in data:
        movies = data["Search"]  # Список найденных фильмов

        print("Найденные фильмы:")
        for movie in movies:
            print(f"{movie['Title']} ({movie['Year']}) - IMDb ID: {movie['imdbID']}")
    else:
        print("Фильмы не найдены.")
else:
    print("Ошибка при получении данных!")






