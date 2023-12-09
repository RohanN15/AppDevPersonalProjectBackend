import requests
class Cat:
    def __init__(self, n):
        self.n = n
    
    def get_cat_breed(self):
        result = requests.get('https://catfact.ninja/breeds')
        data = result.json()["data"]
        print(data[self.n]['breed'])


cat = Cat(3)
cat.get_cat_breed()