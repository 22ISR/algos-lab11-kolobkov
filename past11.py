import requests
import json

response = requests.get("http://www.omdbapi.com/?apikey=505480d7&s=batman")
if response.status_code == 200:
    print(response.json())  # {'name': 'michael', 'age': 40, 'count': 12345}


while True:
    command = input("Введите название фильма (или напишите 'выход' чтобы завершить работу):")
    if command.lower() == "exit":
        print("Goodbye!")
        break
    print(f"You entered: {command}")
    response = requests.get("https://api.example.com/data")
    
movies = [
    {"Title": "Inception", "Year": "2010"},
    {"Title": "The Matrix", "Year": "1999"},
]
for movie in movies:
    print(f"🎬 {movie['Title']} ({movie['Year']})")