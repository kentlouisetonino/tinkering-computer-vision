# Throughout this, we're going to be creating classifiers that attempt to solve
# the following problems: Is this a picture of a Car or of a Truck? Our datasets
# is about 10,000 pictures of various automobiles, around have cars and half trucks.

import os, warnings
import matplotlib.pyplot as pyplot
from matplotlib import gridspec
import numpy
import tensorflow as tf
import keras
from keras.applications import image_dataset_from_directory

# STEP 1: LOAD THE DATA.

# Reproducability.
def setSeed(seed=31415):
  numpy.random.seed(seed)
  tf.random.set_seed(seed)
  os.environ['PYTHONHASHSEED'] = str(seed)
  os.environ['TF_DETERMINISTIC_OPS'] = '1'

setSeed(31415)

# Set matplotlib defaults.
pyplot.rc('figure', autolayout = True)
pyplot.rc('axes', labelweight='bold', labelsize='large')
pyplot.rc('image', cmap='magma')

# Clean up output cells.
warnings.filterwarnings('ignore')

# Load training and validation sets.
dsTrain = image_dataset_from_directory(
  './data/train',
  labels='inferred',
  label_mode='binary',
  image_size=[128, 128],
  interpolation='nearest',
  batch_size=64,
  shuffle=True,
)

dsValid = image_dataset_from_directory(
  './data/valid',
    labels='inferred',
    label_mode='binary',
    image_size=[128, 128],
    interpolation='nearest',
    batch_size=64,
    shuffle=False,
)

# Data pipeline.
def convertToFloat(image, label):
  image = tf.image.convert_image_dtype(image, dtype=tf.float32)
  return image, label

AUTOTUNE = tf.data.experimental.AUTOTUNE

dsTrain = (
  dsTrain.map(convertToFloat).cache().prefetch(buffer_size=AUTOTUNE)
)

dsValid = (
  dsValid.map(convertToFloat).cache().prefetch(buffer_size=AUTOTUNE)
)



# STEP 2: DEFINE PRETRAINEDD BASE
pretrainedBase = keras.models.load_model(
  './vgg16',
)

pretrainedBase.trainable = False



# STEP 3: ATTACH HEAD
model = keras.Sequential([
  pretrainedBase,
  keras.layers.Flatten(),
  keras.layers.Dense(6, activation='relu'),
  keras.layers.Dense(1, activation='sigmoid'),
])
