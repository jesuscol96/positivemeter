import re, string, pickle
import tensorflow as tf
import tensorflow.keras as keras
from tensorflow.keras.layers.experimental.preprocessing import TextVectorization

max_features = 20000
embedding_dim = 128
sequence_length = 500

def custom_standardization(input_data):
    lowercase = tf.strings.lower(input_data)
    stripped_html = tf.strings.regex_replace(lowercase, "<br />", " ")
    return tf.strings.regex_replace(stripped_html, "[%s]" % re.escape(string.punctuation), "")

vectorize_layer = TextVectorization(standardize=custom_standardization,
                                    max_tokens=max_features,
                                    output_mode="int",
                                    output_sequence_length=sequence_length)
#reload object from file
file = open('assets/vec_weights.pkl', 'rb')
vec_weights = pickle.load(file)
file.close()
#
vectorize_layer.set_weights(vec_weights)
#
model = keras.models.load_model('assets/model.h5')
# A string input
inputs = tf.keras.Input(shape=(1,), dtype="string")
# Turn strings into vocab indices
indices = vectorize_layer(inputs)
# Turn vocab indices into predictions
outputs = model(indices)
# Our end to end model
end_to_end_model = tf.keras.Model(inputs, outputs)
end_to_end_model.compile(loss="binary_crossentropy", optimizer="adam", metrics=["accuracy"])

def process_text(text):
    #Prediction
    score = end_to_end_model.predict([text])

    return '{:2d}'.format(int(score[0][0]*100))
