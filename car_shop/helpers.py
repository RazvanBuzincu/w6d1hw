import requests 
import requests_cache 
import json 

requests_cache.install_cache('image_cache', backend='sqlite')

def get_image(search):
    url = "https://google-search72.p.rapidapi.com/imagesearch"

    querystring = {"q": search,"gl":"us","lr":"lang_en","num":"10","start":"0"}

    headers = {
	    "X-RapidAPI-Key": "d18640d5c3msh4b7d0dbe1530c4cp1f097fjsncbb8d6552706",
	    "X-RapidAPI-Host": "google-search72.p.rapidapi.com"
}

    response = requests.get(url, headers=headers, params=querystring)

    data = response.json()

    img_url = ""

    if 'items' in data.keys():
           img_url = data['items'][0]['originalImageUrl'] 

    return img_url