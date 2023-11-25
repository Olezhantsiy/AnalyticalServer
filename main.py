from flask import Flask, request, jsonify
import numpy as np
import tensorflow as tf
import ast
import os; os.environ['TF_ENABLE_ONE DNN_OPTS'] = '0'
app = Flask(__name__)

# Load the model outside of the route to avoid loading it on every request
model = tf.keras.models.load_model('tensorflow_trained10.h5')

print(model)
# Show the model architecture

model.summary()



@app.route("/", methods=['GET'])
def homepage():
    return 'FFFFFFFFFFFFFFFFFFF'

@app.route('/predict', methods=['POST'])
def predict():

    try:
        data = request.form.to_dict()['data']

        right_data = ast.literal_eval(data)
        print(right_data)

        # Extract and convert the input data to numpy array
        # input_data = np.array([right_data])
        print("IOD")
        # Perform prediction
        # predictions = model.predict(right_data)
        # print(predictions)

        new_data = np.array([right_data])
        prediction = model.predict(new_data)
        print(prediction[0][0])
        # Example response


        result = str(prediction[0][0])
        str(result)
        result = result.replace('.',',')
        print(result)
        return result

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=80, debug=True)