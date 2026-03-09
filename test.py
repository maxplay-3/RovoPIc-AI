import main 
# создаем класс для ии
ai = main.AI()
mode = input("Enter the language(en/ru):")
if mode == "en":
   text = "Enter the path to the photo (the image must be located in the same folder):"
else:
   text = "введите путь к фотографии(изображение должно находится в этой же папке):"
while True:
# определяем путь к картинке
    IMAGE_PATH = input(text)
# создаем экземляр класса Image в котром находятся все параметры изображения
    класс = main.Image(IMAGE_PATH)
# и наконецто определям оценку и выводим
    оценка = ai.evaluate_image(класс)
    print(оценка)
