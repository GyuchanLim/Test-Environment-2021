import requests #allows imports

response = requests.get("https://randomfox.ca/floof/")
print(response.status_code)
print(response.json()) #Returns the dictionary.
fox = response.json()
print(fox['image'])