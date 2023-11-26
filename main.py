from flask import Flask, request, jsonify
import numpy as np
import tensorflow as tf
import ast
import os; os.environ['TF_ENABLE_ONE DNN_OPTS'] = '0'
app = Flask(__name__)

model = tf.keras.models.load_model('tensorflow_trained10.h5')
print(model)
model.summary()

@app.route("/", methods=['GET'])
def homepage():
    return 'Welcome to Home page!'

@app.route('/predict', methods=['POST'])
def predict():

    try:
        data = request.form.to_dict()['data']

        datamodel = np.array([ast.literal_eval(data)])
        prediction = model.predict(datamodel)
        print(prediction[0][0])
        # Example response


        result = str(prediction[0][0])
        result = result.replace('.',',')
        print(result)
        return result

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=80, debug=True)
