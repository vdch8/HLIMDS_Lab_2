## **MobileNet на Raspberry Pi 3 B+**

### **Шаг 1: Обновление системы**

Обновите список пакетов и установите обновления:

```bash
sudo apt-get update
sudo apt-get upgrade
```

### **Шаг 2: Установка Python и необходимых инструментов**

Убедитесь, что у вас установлены Python 3, pip и модуль для создания виртуальных окружений:

```bash
sudo apt-get install python3 python3-pip python3-venv
```

### **Шаг 3: Создание и активация виртуального окружения**

Создайте директорию для вашего проекта и перейдите в неё:

```bash
mkdir my_mobilenet_project
cd my_mobilenet_project
```

Создайте виртуальное окружение:

```bash
python3 -m venv venv
```

Активируйте виртуальное окружение:

```bash
source venv/bin/activate
```

### **Шаг 4: Обновление pip внутри виртуального окружения**

Обновите pip до последней версии:

```bash
pip install --upgrade pip
```

### **Шаг 5: Установка необходимых пакетов**

#### **5.1 Установка совместимой версии numpy**

Установите `numpy` версии ниже 2.0:

```bash
pip install "numpy<2"
```

#### **5.2 Установка tflite-runtime без обновления numpy**

Установите `tflite-runtime`, запретив установку зависимостей:

```bash
pip install tflite-runtime --no-deps
```

#### **5.3 Установка Pillow**

Установите пакет `Pillow` для работы с изображениями:

```bash
pip install Pillow
```

### **Шаг 6: Загрузка модели MobileNet**

Скачайте предварительно обученную модель MobileNet:

```bash
wget https://storage.googleapis.com/download.tensorflow.org/models/tflite/mobilenet_v1_1.0_224_quant_and_labels.zip
```

### **Шаг 7: Распаковка архива с моделью**

Распакуйте скачанный архив:

```bash
unzip mobilenet_v1_1.0_224_quant_and_labels.zip
```

### **Шаг 8: Подготовка изображения**

#### **8.1 Скачивание тестового изображения**

Скачайте тестовое изображение (замените URL на любое изображение по вашему выбору):

```bash
wget https://upload.wikimedia.org/wikipedia/commons/4/4d/Cat_November_2010-1a.jpg -O your_image.jpg
```

#### **8.2 Проверка изображения**

Убедитесь, что изображение скачано:

```bash
ls
```

### **Шаг 9: Создание скрипта**

Создайте файл `inference.py`:
```bash
touch inference.py
```


### **Шаг 10: Запуск скрипта**

Запустите скрипт:

```bash
python inference.py
```

### **Шаг 11: Проверка результатов**

Убедитесь, что выводятся предсказания модели для вашего изображения, для нашего примера:
```bash
tiger cat: 146  
Egyptian cat: 89  
tabby: 20  
cricket: 0  
zebra: 0
```

### **Шаг 12: Деактивация виртуального окружения**

После завершения работы:

```bash
deactivate
```

----------
