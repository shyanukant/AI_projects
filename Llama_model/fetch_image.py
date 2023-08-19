import os
import requests
PIXEL_KEY = os.environ.get('PIXEL_KEY')
def fetch_image(query):

    url = "https://pexelsdimasv1.p.rapidapi.com/v1/search"

    querystring = {"query":query, "per_page":"1"}

    headers = {
        "Authorization": PIXEL_KEY,
        "X-RapidAPI-Key": "fa936278admshef9bffe495b2f18p15229bjsnc09f54b19e14",
        "X-RapidAPI-Host": "PexelsdimasV1.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)

    if response.status_code  == 200:
        data = response.json()
        photos = data.get('photos')
    
        if photos :
            src_original_url = photos[0]['src']['original']
            return src_original_url
        else :
            print('No Image found!!')
    else:
        return f"Error : {response.status_code}. {response.text}"
