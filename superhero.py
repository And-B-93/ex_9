#Нужно определить кто самый умный(intelligence) из трех супергероев- Hulk, Captain America, Thanos.
import requests
import json
def Superhero_list():
    intelligence_dict = {}
    response_hulk = requests.get('https://www.superheroapi.com/api.php/2619421814940190/search/Hulk')
    response_cap = requests.get('https://www.superheroapi.com/api.php/2619421814940190/search/Captain America')
    response_KIA = requests.get('https://www.superheroapi.com/api.php/2619421814940190/search/Thanos')
    intelligence_dict[response_hulk.json()['results'][0]['name']] = response_hulk.json()['results'][0]['powerstats']['intelligence']
    intelligence_dict[response_cap.json()['results'][0]['name']] = response_cap.json()['results'][0]['powerstats']['intelligence']
    intelligence_dict[response_KIA.json()['results'][0]['name']] = response_KIA.json()['results'][0]['powerstats']['intelligence']
    lis = [(key, value) for key, value in intelligence_dict.items()]
    return max(lis)[0]
print(Superhero_list())