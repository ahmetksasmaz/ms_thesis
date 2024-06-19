import os
import argparse
import functools
import tensorflow as tf
import numpy as np
import time
import cv2 as cv

import lact.lib.model as model
from lact.lib.multi_datasets import normalize_image

class LACTInference:
    def __init__(self, checkpoint_path):
        self.model = model.gen_light()
        model.load_checkpoint_weights_one_by_one(self.model, checkpoint_path)
    
    def __call__(self, input):
        input = tf.convert_to_tensor(input, dtype=tf.float32)
        input /= 255.0
        normalized_input = normalize_image(input)
        normalized_input = tf.reshape(normalized_input, [-1] + list(tf.shape(normalized_input).numpy()))
        
        prediction,_ = self.model(normalized_input, training=False)
        
        casted_image = tf.cast(tf.clip_by_value(0.5 * (prediction[0] + 1.0), 0.0, 1.0), 'float32')
        casted_image = casted_image.numpy()
        casted_image *= 255.0
        casted_image = casted_image.astype(np.uint8)
        return casted_image