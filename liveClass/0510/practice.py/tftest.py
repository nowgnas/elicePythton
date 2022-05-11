import tensorflow as tf
from tensorflow import keras
print(tf.__version__, keras.__version__)

print(tf.config.list_physical_devices('GPU'))
