
import json
import requests

conv = {'url': 'https://www.technocrazed.com/wp-content/uploads/2015/12/quote-wallpaper_11.jpg'}
s = json.dumps(conv)
res = requests.post("http://127.0.0.1:5000/image_to_text/", json=s).json()
print(res['text'])
