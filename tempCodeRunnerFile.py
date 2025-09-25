import requests
base_url="https://pokeapi.co/api/v2/"
def pokinfo(name):
    url=f"{base_url}/pokemon/{name}"
    details=requests.get(url)
    if details.status_code==200:
        details1= details.json()
        return details1
pokiname=input("Enter the pokemon name:")
detail2=pokinfo(pokiname)
if detail2:
    print(f"NAME: {detail2["name"]}")
    print(f"ID: {detail2["id"]}")
    print(f"WEIGHT: {detail2["weight"]}")