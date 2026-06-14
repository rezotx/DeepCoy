"""TensorFlow 1 compatibility layer for modern TensorFlow runtimes."""

import os

os.environ.setdefault("TF_USE_LEGACY_KERAS", "1")

import tensorflow as _tf

_tf.compat.v1.disable_eager_execution()

tf = _tf.compat.v1
