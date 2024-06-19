
import cv2 as cv

class CLAHEApplier:
    def __init__(self):
        self.clahe = cv.createCLAHE(clipLimit=5)
    
    def __call__(self, input):
        ycrcb_input = cv.cvtColor(input, cv.COLOR_BGR2YCrCb)
        y, cr, cb = cv.split(ycrcb_input)
        
        y = self.clahe.apply(y)
        
        ycrcb_output = cv.merge([y,cr,cb])
        
        bgr_output = cv.cvtColor(ycrcb_output, cv.COLOR_YCrCb2BGR)
        
        return bgr_output