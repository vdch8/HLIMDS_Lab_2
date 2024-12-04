import tflite_runtime.interpreter as tflite
from PIL import Image
import numpy as np

# Загрузка модели
interpreter = tflite.Interpreter(model_path="mobilenet_v1_1.0_224_quant.tflite")
interpreter.allocate_tensors()

# Получение информации о тензорах ввода и вывода
input_details = interpreter.get_input_details()
output_details = interpreter.get_output_details()

# Загрузка меток классов
with open('labels_mobilenet_quant_v1_224.txt', 'r') as f:
    labels = [line.strip() for line in f.readlines()]

# Подготовка изображения
img = Image.open('your_image.jpg').resize((224, 224))
input_data = np.expand_dims(img, axis=0)

# Преобразование типа данных, если это необходимо
if input_details[0]['dtype'] == np.uint8:
    input_data = np.uint8(input_data)
else:
    input_data = (np.float32(input_data) - 127.5) / 127.5

# Выполнение инференса
interpreter.set_tensor(input_details[0]['index'], input_data)
interpreter.invoke()

# Получение результатов
output_data = interpreter.get_tensor(output_details[0]['index'])
predictions = np.squeeze(output_data)

# Находим топ-5 предсказаний
top_k = predictions.argsort()[-5:][::-1]

# Выводим результаты
for i in top_k:
    print(f'{labels[i]}: {predictions[i]}')
