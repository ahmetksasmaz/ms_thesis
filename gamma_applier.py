
import cv2 as cv
import numpy as np

class GammaApplier:
    def __init__(self, max_iter):
        self.max_iter = max_iter
    def __call__(self, input):
        ycrcb_input = cv.cvtColor(input, cv.COLOR_BGR2YCrCb)
        y, cr, cb = cv.split(ycrcb_input)
        
        y = np.float32(y)
        y /= 255.0
        
        orig_y = y
        min_gamma = 0.01
        max_gamma = 4.0
        avg_brightness = cv.mean(y)
        avg_brightness_diff = avg_brightness[0] - 0.5
        
        if avg_brightness_diff > 0:
            max_gamma = 1.0
        else:
            min_gamma = 1.0
        iter = 0
        while abs(avg_brightness_diff) > 0.01 and iter < self.max_iter:
            y = pow(orig_y, 1/((min_gamma + max_gamma)/2))
            
            avg_brightness = cv.mean(y)
            avg_brightness_diff = avg_brightness[0] - 0.5
            if avg_brightness_diff > 0:
                max_gamma = (min_gamma + max_gamma) / 2
            else:
                min_gamma = (min_gamma + max_gamma) / 2
            iter += 1
        
        y *= 255.0
        y = np.uint8(y)
        
        ycrcb_output = cv.merge([y,cr,cb])
        
        bgr_output = cv.cvtColor(ycrcb_output, cv.COLOR_YCrCb2BGR)
        
        return bgr_output