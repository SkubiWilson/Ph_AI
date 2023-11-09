import cv2
import pytesseract

# Шлях до виконуваного файлу Tesseract OCR
pytesseract.pytesseract.tesseract_cmd = 'tesseract\\tesseract.exe'

# Завантажуємо зображення Лише png
img = cv2.imread('Screenshot_1.png')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# Конфігурація для розпізнавання українського тексту
config = r'--oem 3 --psm 6 -l ukr'

# Розпізнавання тексту
text = pytesseract.image_to_string(img, config=config)

# Виведення розпізнаного тексту в консоль
print(text)
