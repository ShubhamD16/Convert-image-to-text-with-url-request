from flask import Flask
from flask import request
import json
import numpy as np
import cv2
from PIL import Image
import requests
from io import BytesIO
import ocr

app = Flask(__name__)

@app.route('/image_to_text/', methods = ['POST'])
def determine_escalation():
    jsondata = request.get_json()
    data = json.loads(jsondata)
    url = data['url']

    #stuff happens here that involves data to obtain a result

    response = requests.get(url)
    img = Image.open(BytesIO(response.content))

    img = np.array(img)
    # img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (3, 3), 0)
    thresh = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]

    # Morph open to remove noise and invert image
    # kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
    # opening = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel, iterations=1)
    # invert = 255 - opening

    # Perform text extraction

    text = ocr.convert_to_text(gray)

    print(text)



    result = {'text': text}

    #result = {'escalate': data['url']}
    return json.dumps(result)


if __name__ == '__main__':
    app.run(debug=True)