from lact_inference import LACTInference
from clahe_applier import CLAHEApplier
from gamma_applier import GammaApplier
import cv2 as cv
import tensorflow as tf
import argparse

def psnr(y_true, y_pred):
    return tf.reduce_mean(tf.image.psnr(y_true, y_pred, max_val=255))

def ssim(y_true, y_pred):
    return tf.reduce_mean(tf.image.ssim(y_true, y_pred, max_val=255))

def main():
    parser = argparse.ArgumentParser(description='LACT & Classical Methods Experimenter')
    parser.add_argument('-d','--dataset-path', help='Dataset directory', required=True, type=str)
    parser.add_argument('-j','--dataset-json', help='Json database path for dataset', required=True, type=str)
    parser.add_argument('-c','--checkpoint-path', help='Checkpoint path of LACT /path/to/ckpt', required=True, type=str)
    parser.add_argument('-i','--input-resize-shape', help='Input resize shape w h', nargs="+", required=True, type=int)
    parser.add_argument('-o','--output-path', help='Output directory of results', required=True, type=str)
    args = vars(parser.parse_args())
    
    if len(args["input_resize_shape"]) != 2:
        print("Input resize shape should be 2 dimensional")
        exit()
    
    resize_shape = args["input_resize_shape"]
    
    lact_inference = LACTInference(args["checkpoint_path"])
    clahe_applier = CLAHEApplier()
    gamma_applier = GammaApplier(100)

    # Read dataset
    
    # Read results from json
    # Transfer json to dict
    
    # Iterate dataset
        # Get Image and Label
        # Resize Image and Label
        # If image label tuple is in results then skip
            # Lact Prediction
            # PSNR & SSIM Lact
            # Clahe
            # PSNR & SSIM Clahe
            # Gamma
            # PSNR & SSIM Gamma
            # Merge results and imwrite output
            # Add results to dict
    
    # Parse result dict and calculate overall metrics

    image = cv.imread("/home/kursad/git/datasets/SICE/Dataset_Part1/1/4.JPG")
    label = cv.imread("/home/kursad/git/datasets/SICE/Dataset_Part1/Label/1.JPG")
    image = cv.resize(image, (resize_shape[0], resize_shape[1]))
    label = cv.resize(label, (resize_shape[0], resize_shape[1]))

    lact_prediction = lact_inference(image)
    clahe_output = clahe_applier(image)
    gamma_output = gamma_applier(image)

    print("Lact : ", {"psnr": psnr(label, lact_prediction), "ssim": ssim(label, lact_prediction)})
    print("Clahe : ", {"psnr": psnr(label, clahe_output), "ssim": ssim(label, clahe_output)})
    print("Gamma : ", {"psnr": psnr(label, gamma_output), "ssim": ssim(label, gamma_output)})

if __name__ == "__main__":
    main()