import requests

# url = requests.get("https://www.google.com/")
# with open("google_data.txt", "w") as file:
#     file.write(url.text)

# with open("google_data.html", "w") as file:
#     file.write(url.text)

# url = requests.get("https://images.pexels.com/photos/674010/pexels-photo-674010.jpeg?_gl=1*1a4iiry*_ga*MTkxNzA5MTU3NS4xNzQ5MDY5MDc0*_ga_8JE65Q40S6*czE3NTUzNjE4MTQkbzExJGcxJHQxNzU1MzYxODE2JGo1OCRsMCRoMA..")
# with open("peacock.png", "wb") as file:
#     file.write(url.content)

url = requests.get("https://httpbin.org/get")
print(url.text)

payload = {"name": "John", "age": 30}
url = requests.post("https://httpbin.org/post", data=payload)
print(url.text)