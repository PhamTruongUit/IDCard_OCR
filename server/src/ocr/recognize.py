from PIL import Image

def OCR(lst_lines, detector)->list:
    lst_text = []
    for img in lst_lines:
        try:
            img = Image.fromarray(img)
            text = detector.predict(img)
        except:
            text = ''
        lst_text.append(text)
    return lst_text


    