import easyocr
import cv2

def convert_to_text(img):
    reader = easyocr.Reader(['en'])
    result = reader.readtext(img, detail=0)

    return result


