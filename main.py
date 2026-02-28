import cv2
import numpy as np
import logging as l
l.basicConfig(level=l.INFO, format="[%asctime)s] %(levelname)s: %(message)s")

class Image:
    def __init__(self, path):
        self.p = path
        self.brightness = None
        self.laplacian = None
        self.contrast = None

    def check_brightness(self):
        image = cv2.imread(self.p, cv2.IMREAD_GRAYSCALE)
        self.brightness = np.mean(image)  # Среднее значение яркости всех пикселей
        self.brightness = round(self.brightness, 2)
        return self.brightness

    def check_sharpness(self):
        image = cv2.imread(self.p, cv2.IMREAD_GRAYSCALE)
        self.laplacian = cv2.Laplacian(image, cv2.CV_64F).var()  # Считаем "резкость" с помощью Лапласа
        self.laplacian = round(self.laplacian, 2)
        return self.laplacian

    def check_contrast(self):
        image = cv2.imread(self.p, cv2.IMREAD_GRAYSCALE)
        min_pixel = np.min(image)  # Находим самый темный пиксель
        max_pixel = np.max(image)  # Находим самый светлый пиксель
        self.contrast = max_pixel - min_pixel  # Контраст = разница между светлым и темным
        self.contrast = round(self.contrast, 2)
        return round(self.contrast,2) 


class AI:
    def __init__(self):
        pass

    def evaluate_image(self, image_class):
        points = 0
        b = image_class.check_brightness()
        s = image_class.check_sharpness()
        c = image_class.check_contrast()
        # 0.1 - плохо,1 - хорошо 
        if b < 100:
           points += 0.1
        elif 100 <= b <= 180: # проверка яркости 
             points += 1
        else:
            points += 0.1
        if s < 100: # 
           points += 0.1
        elif 100 <= s <= 300: # проверка резкости 
            points += 1
        else:
            points += 0.1
        if c < 50: # проверка контраста 
            points += 0.1
        elif 50 <= c <= 150: # проверка контраста 
            points += 1
        else:
            points += 0.1
        return round(points, 2) # возращаем балл в четном виде 
    
    