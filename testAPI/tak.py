import requests

res = requests.get(
    "https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos",
    params={'sol' : 1000, 'api_key' : 'DEMO_KEY'}
)

res_json = res.json()
for photo in res_json["photos"]:
    if photo["camera"]["name"] == "NAVCAM":
        print(photo["camera"]["name"] + " : " + photo["img_src"]) 
