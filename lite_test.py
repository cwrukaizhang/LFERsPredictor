import numpy as np
import tensorflow as tf

# Load the TFLite model and allocate tensors.

def run_model(path):
    interpreter = tf.lite.Interpreter(model_path=path)
    interpreter.allocate_tensors()
# Get input and output tensors.
    input_details = interpreter.get_input_details()
    output_details = interpreter.get_output_details()

# Test the model on random input data.
    input_shape = input_details[0]['shape']
    input_data = np.array(np.random.random_sample(input_shape), dtype=np.float32)
    interpreter.set_tensor(input_details[0]['index'], input_data)
    interpreter.invoke()
# The function `get_tensor()` returns a copy of the tensor data.
# Use `tensor()` in order to get a pointer to the tensor.
    output_data = interpreter.get_tensor(output_details[0]["index"])

    return output_data
print(run_model("B_model_lite.tflite"))