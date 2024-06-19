from lact_inference import LACTInference
from clahe_applier import CLAHEApplier
from gamma_applier import GammaApplier
import cv2 as cv
import tensorflow as tf
import argparse
import json
import os
import numpy as np
import tqdm

gpus = tf.config.experimental.list_physical_devices('GPU')
if len(gpus) >= 1:
    tf.config.experimental.set_visible_devices(gpus[0], 'GPU')

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
    parser.add_argument('-o','--output-file', help='Output file of results', required=True, type=str)
    parser.add_argument('-p','--merged-predictions-path', help='Merged predictions directory path', required=True, type=str)
    args = vars(parser.parse_args())
    
    if len(args["input_resize_shape"]) != 2:
        print("Input resize shape should be 2 dimensional")
        exit()
    
    resize_shape = args["input_resize_shape"]
    
    lact_inference = LACTInference(args["checkpoint_path"])
    clahe_applier = CLAHEApplier()
    gamma_applier = GammaApplier(100)

    dataset_json_file = open(args["dataset_json"])
    dataset_json = json.load(dataset_json_file)
    
    results_dict = {}
    
    if os.path.isfile(args["output_file"]):
        previous_output_file = open(args["output_file"])
        for line in previous_output_file.readlines():
            # Image path, algorithm [lact | clahe | gamma], psnr, ssim
            fields = line.split("\t")
            if fields[0] not in results_dict.keys():
                results_dict[fields[0]] = {}
            results_dict[fields[0]][fields[1]] = (float(fields[2]),float(fields[3]))
        previous_output_file.close()
    
    output_file = open(args["output_file"], "a")
    
    for i in tqdm.tqdm(range(len(dataset_json["image"]))):
        image_path = dataset_json["image"][i]
        label_path = dataset_json["label"][i]
        calculate_lact = False
        calculate_clahe = False
        calculate_gamma = False
        if image_path in results_dict.keys():
            if "lact" not in results_dict[image_path]:
                calculate_lact = True
            if "clahe" not in results_dict[image_path]:
                calculate_clahe = True
            if "gamma" not in results_dict[image_path]:
                calculate_gamma = True
        else:
            results_dict[image_path] = {}
            calculate_lact = True
            calculate_clahe = True
            calculate_gamma = True
        if calculate_lact or calculate_clahe or calculate_gamma:
            image = cv.imread(args["dataset_path"]+image_path)
            label = cv.imread(args["dataset_path"]+label_path)
            image = cv.resize(image, (resize_shape[0], resize_shape[1]))
            label = cv.resize(label, (resize_shape[0], resize_shape[1]))
            merged = np.zeros((resize_shape[1], resize_shape[0]*5, 3), dtype = "uint8")
            merged[0:resize_shape[1],0*resize_shape[0]:1*resize_shape[0],:] = label
            merged[0:resize_shape[1],1*resize_shape[0]:2*resize_shape[0],:] = image
            if calculate_lact:
                lact_prediction = lact_inference(image)
                psnr_ = psnr(label, lact_prediction).numpy()
                ssim_ = ssim(label, lact_prediction).numpy()
                results_dict[image_path]["lact"] = (psnr_, ssim_)
                cv.rectangle(lact_prediction, (resize_shape[0] - 120, 0), (resize_shape[0], 30), (255, 255, 255), -1)
                cv.putText(lact_prediction, "psnr:"+str(psnr_), (resize_shape[0] - 120, 10), cv.FONT_HERSHEY_SIMPLEX , 0.4,  (255,0,0), 1, cv.LINE_AA) 
                cv.putText(lact_prediction, "ssim:"+str(ssim_), (resize_shape[0] - 120, 30), cv.FONT_HERSHEY_SIMPLEX , 0.4,  (255,0,0), 1, cv.LINE_AA) 
                merged[0:resize_shape[1],2*resize_shape[0]:3*resize_shape[0],:] = lact_prediction
                output_file.write(image_path + "\t" + "lact" + "\t" + str(psnr_) + "\t" + str(ssim_) + "\n")
            if calculate_clahe:
                clahe_prediction = clahe_applier(image)
                psnr_ = psnr(label, clahe_prediction).numpy()
                ssim_ = ssim(label, clahe_prediction).numpy()
                results_dict[image_path]["clahe"] = (psnr_, ssim_)
                cv.rectangle(clahe_prediction, (resize_shape[0] - 120, 0), (resize_shape[0], 30), (255, 255, 255), -1)
                cv.putText(clahe_prediction, "psnr:"+str(psnr_), (resize_shape[0] - 120, 10), cv.FONT_HERSHEY_SIMPLEX , 0.4,  (255,0,0), 1, cv.LINE_AA) 
                cv.putText(clahe_prediction, "ssim:"+str(ssim_), (resize_shape[0] - 120, 30), cv.FONT_HERSHEY_SIMPLEX , 0.4,  (255,0,0), 1, cv.LINE_AA) 
                merged[0:resize_shape[1],3*resize_shape[0]:4*resize_shape[0],:] = clahe_prediction
                output_file.write(image_path + "\t" + "clahe" + "\t" + str(psnr_) + "\t" + str(ssim_) + "\n")
            if calculate_gamma:
                gamma_prediction = gamma_applier(image)
                psnr_ = psnr(label, gamma_prediction).numpy()
                ssim_ = ssim(label, gamma_prediction).numpy()
                results_dict[image_path]["gamma"] = (psnr_, ssim_)
                cv.rectangle(gamma_prediction, (resize_shape[0] - 120, 0), (resize_shape[0], 30), (255, 255, 255), -1)
                cv.putText(gamma_prediction, "psnr:"+str(psnr_), (resize_shape[0] - 120, 10), cv.FONT_HERSHEY_SIMPLEX , 0.4,  (255,0,0), 1, cv.LINE_AA) 
                cv.putText(gamma_prediction, "ssim:"+str(ssim_), (resize_shape[0] - 120, 30), cv.FONT_HERSHEY_SIMPLEX , 0.4,  (255,0,0), 1, cv.LINE_AA) 
                merged[0:resize_shape[1],4*resize_shape[0]:5*resize_shape[0],:] = gamma_prediction
                output_file.write(image_path + "\t" + "gamma" + "\t" + str(psnr_) + "\t" + str(ssim_) + "\n")
            cv.putText(merged, "LABEL", (0*resize_shape[0], 40), cv.FONT_HERSHEY_SIMPLEX , 1,  (255,0,0), 2, cv.LINE_AA) 
            cv.putText(merged, "IMAGE", (1*resize_shape[0], 40), cv.FONT_HERSHEY_SIMPLEX , 1,  (255,0,0), 2, cv.LINE_AA) 
            cv.putText(merged, "LACT", (2*resize_shape[0], 40), cv.FONT_HERSHEY_SIMPLEX , 1,  (255,0,0), 2, cv.LINE_AA) 
            cv.putText(merged, "CLAHE", (3*resize_shape[0], 40), cv.FONT_HERSHEY_SIMPLEX , 1,  (255,0,0), 2, cv.LINE_AA) 
            cv.putText(merged, "GAMMA", (4*resize_shape[0], 40), cv.FONT_HERSHEY_SIMPLEX , 1,  (255,0,0), 2, cv.LINE_AA) 
            cv.imwrite(args["merged_predictions_path"]+image_path.replace("/", "_").replace(".", "_")+"_merged.jpg", merged)
    
    output_file.close()
    
    # Parse result dict and calculate overall metrics

    results_len = len(results_dict)
    lact_psnr_sum = 0.0
    lact_ssim_sum = 0.0
    clahe_psnr_sum = 0.0
    clahe_ssim_sum = 0.0
    gamma_psnr_sum = 0.0
    gamma_ssim_sum = 0.0
    for key in results_dict.keys():
        lact_psnr, lact_ssim = results_dict[key]["lact"]
        clahe_psnr, clahe_ssim = results_dict[key]["clahe"]
        gamma_psnr, gamma_ssim = results_dict[key]["gamma"]
        lact_psnr_sum += lact_psnr
        lact_ssim_sum += lact_ssim
        clahe_psnr_sum += clahe_psnr
        clahe_ssim_sum += clahe_ssim
        gamma_psnr_sum += gamma_psnr
        gamma_ssim_sum += gamma_ssim

    lact_psnr_avg = lact_psnr_sum / results_len
    lact_ssim_avg = lact_ssim_sum / results_len
    clahe_psnr_avg = clahe_psnr_sum / results_len
    clahe_ssim_avg = clahe_ssim_sum / results_len
    gamma_psnr_avg = gamma_psnr_sum / results_len
    gamma_ssim_avg = gamma_ssim_sum / results_len

    print("Algorithm\t\tPSNR\t\tSSIM")
    print("LACT\t\t"+str(lact_psnr_avg)+"\t\t"+str(lact_ssim_avg))
    print("CLAHE\t\t"+str(clahe_psnr_avg)+"\t\t"+str(clahe_ssim_avg))
    print("GAMMA\t\t"+str(gamma_psnr_avg)+"\t\t"+str(gamma_ssim_avg))

if __name__ == "__main__":
    main()