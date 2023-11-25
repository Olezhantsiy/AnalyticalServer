from flask import Flask, request, jsonify
import tensorflow as tf
import numpy as np

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Привет, это простой сервер на Flask!'

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Загрузка модели
        model = tf.keras.models.load_model('C:\Users\Олежа\PycharmProjects\pythonServer\tensorflow_trained120.h5')

        # Пример входных данных
        input_data = np.array([[1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0]])

        # Предсказание
        prediction = model.predict(input_data)

        # Вывод результата
        print("Результат предсказания:", prediction)


        return jsonify(prediction)

    except Exception as e:
        return jsonify({'error': str(e)})


if __name__ == '__main__':
    app.run(host="0.0.0.0",port=8000,debug=True)
