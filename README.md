Flask TensorFlow Prediction API

Это Flask-приложение служит простым API для выполнения предсказаний с использованием предварительно обученной модели TensorFlow. Модель загружается при запуске приложения, и предсказания могут быть сделаны путем отправки POST-запросов к конечной точке /predict.
Предварительные требования

    Python 3.x
    Flask
    NumPy
    TensorFlow

Установка

git clone https://github.com/Olezhantsiy/AnalyticalServer.git
cd your-repository

Установите зависимости:

    pip install -r requirements.txt

    Загрузите предварительно обученную модель TensorFlow (tensorflow_trained10.h5) и поместите ее в корневой каталог.

Использование:

Запустите приложение Flask:

python app.py

Приложение запустится по адресу http://0.0.0.0:80/.
