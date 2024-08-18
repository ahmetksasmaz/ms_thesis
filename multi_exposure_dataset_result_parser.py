
multi_exposure_dataset_result_file_path = "multi_exposure_results.csv"
multi_exposure_dataset_result_file = open(multi_exposure_dataset_result_file_path)

results_dict = {}

for line in multi_exposure_dataset_result_file.readlines():
    # Image path, algorithm [lact | clahe | gamma | gamma_lact], psnr, ssim
    fields = line.split("\t")
    if fields[0] not in results_dict.keys():
        results_dict[fields[0]] = {}
    results_dict[fields[0]][fields[1]] = (float(fields[2]),float(fields[3]))

multi_exposure_dataset_result_file.close()

results_len = len(results_dict) / 5

# 0 N1.5 N1 P1.5 P1

lact_psnr_sum = {
    "0": 0.0,
    "N1.5": 0.0,
    "N1": 0.0,
    "P1.5": 0.0,
    "P1": 0.0
}
lact_ssim_sum = {
    "0": 0.0,
    "N1.5": 0.0,
    "N1": 0.0,
    "P1.5": 0.0,
    "P1": 0.0
}
clahe_psnr_sum = {
    "0": 0.0,
    "N1.5": 0.0,
    "N1": 0.0,
    "P1.5": 0.0,
    "P1": 0.0
}
clahe_ssim_sum = {
    "0": 0.0,
    "N1.5": 0.0,
    "N1": 0.0,
    "P1.5": 0.0,
    "P1": 0.0
}
gamma_psnr_sum = {
    "0": 0.0,
    "N1.5": 0.0,
    "N1": 0.0,
    "P1.5": 0.0,
    "P1": 0.0
}
gamma_ssim_sum = {
    "0": 0.0,
    "N1.5": 0.0,
    "N1": 0.0,
    "P1.5": 0.0,
    "P1": 0.0
}
gamma_lact_psnr_sum = {
    "0": 0.0,
    "N1.5": 0.0,
    "N1": 0.0,
    "P1.5": 0.0,
    "P1": 0.0
}
gamma_lact_ssim_sum = {
    "0": 0.0,
    "N1.5": 0.0,
    "N1": 0.0,
    "P1.5": 0.0,
    "P1": 0.0
}
for key in results_dict.keys():
    lact_psnr, lact_ssim = results_dict[key]["lact"]
    clahe_psnr, clahe_ssim = results_dict[key]["clahe"]
    gamma_psnr, gamma_ssim = results_dict[key]["gamma"]
    gamma_lact_psnr, gamma_lact_ssim = results_dict[key]["gamma_lact"]
    image_index = int(key.split("/")[-1].split(".")[0])
    remain = image_index % 5
    if remain == 1:
        lact_psnr_sum["N1.5"] += lact_psnr
        lact_ssim_sum["N1.5"] += lact_ssim
        clahe_psnr_sum["N1.5"] += clahe_psnr
        clahe_ssim_sum["N1.5"] += clahe_ssim
        gamma_psnr_sum["N1.5"] += gamma_psnr
        gamma_ssim_sum["N1.5"] += gamma_ssim
        gamma_lact_psnr_sum["N1.5"] += gamma_lact_psnr
        gamma_lact_ssim_sum["N1.5"] += gamma_lact_ssim
    elif remain == 2:
        lact_psnr_sum["N1"] += lact_psnr
        lact_ssim_sum["N1"] += lact_ssim
        clahe_psnr_sum["N1"] += clahe_psnr
        clahe_ssim_sum["N1"] += clahe_ssim
        gamma_psnr_sum["N1"] += gamma_psnr
        gamma_ssim_sum["N1"] += gamma_ssim
        gamma_lact_psnr_sum["N1"] += gamma_lact_psnr
        gamma_lact_ssim_sum["N1"] += gamma_lact_ssim
    elif remain == 3:
        lact_psnr_sum["P1.5"] += lact_psnr
        lact_ssim_sum["P1.5"] += lact_ssim
        clahe_psnr_sum["P1.5"] += clahe_psnr
        clahe_ssim_sum["P1.5"] += clahe_ssim
        gamma_psnr_sum["P1.5"] += gamma_psnr
        gamma_ssim_sum["P1.5"] += gamma_ssim
        gamma_lact_psnr_sum["P1.5"] += gamma_lact_psnr
        gamma_lact_ssim_sum["P1.5"] += gamma_lact_ssim
    elif remain == 4:
        lact_psnr_sum["P1"] += lact_psnr
        lact_ssim_sum["P1"] += lact_ssim
        clahe_psnr_sum["P1"] += clahe_psnr
        clahe_ssim_sum["P1"] += clahe_ssim
        gamma_psnr_sum["P1"] += gamma_psnr
        gamma_ssim_sum["P1"] += gamma_ssim
        gamma_lact_psnr_sum["P1"] += gamma_lact_psnr
        gamma_lact_ssim_sum["P1"] += gamma_lact_ssim
    elif remain == 0:
        lact_psnr_sum["0"] += lact_psnr
        lact_ssim_sum["0"] += lact_ssim
        clahe_psnr_sum["0"] += clahe_psnr
        clahe_ssim_sum["0"] += clahe_ssim
        gamma_psnr_sum["0"] += gamma_psnr
        gamma_ssim_sum["0"] += gamma_ssim
        gamma_lact_psnr_sum["0"] += gamma_lact_psnr
        gamma_lact_ssim_sum["0"] += gamma_lact_ssim

print("0##################################")
print("Algorithm\t\tPSNR\t\tSSIM")
print("LACT\t\t"+str(lact_psnr_sum["0"] / results_len)+"\t\t"+str(lact_ssim_sum["0"] / results_len))
print("CLAHE\t\t"+str(clahe_psnr_sum["0"] / results_len)+"\t\t"+str(clahe_ssim_sum["0"] / results_len))
print("GAMMA\t\t"+str(gamma_psnr_sum["0"] / results_len)+"\t\t"+str(gamma_ssim_sum["0"] / results_len))
print("GAMMA_LACT\t\t"+str(gamma_lact_psnr_sum["0"] / results_len)+"\t\t"+str(gamma_lact_ssim_sum["0"] / results_len))
print("###########################")

print("N1.5##################################")
print("Algorithm\t\tPSNR\t\tSSIM")
print("LACT\t\t"+str(lact_psnr_sum["N1.5"] / results_len)+"\t\t"+str(lact_ssim_sum["N1.5"] / results_len))
print("CLAHE\t\t"+str(clahe_psnr_sum["N1.5"] / results_len)+"\t\t"+str(clahe_ssim_sum["N1.5"] / results_len))
print("GAMMA\t\t"+str(gamma_psnr_sum["N1.5"] / results_len)+"\t\t"+str(gamma_ssim_sum["N1.5"] / results_len))
print("GAMMA_LACT\t\t"+str(gamma_lact_psnr_sum["N1.5"] / results_len)+"\t\t"+str(gamma_lact_ssim_sum["N1.5"] / results_len))
print("###########################")

print("N1##################################")
print("Algorithm\t\tPSNR\t\tSSIM")
print("LACT\t\t"+str(lact_psnr_sum["N1"] / results_len)+"\t\t"+str(lact_ssim_sum["N1"] / results_len))
print("CLAHE\t\t"+str(clahe_psnr_sum["N1"] / results_len)+"\t\t"+str(clahe_ssim_sum["N1"] / results_len))
print("GAMMA\t\t"+str(gamma_psnr_sum["N1"] / results_len)+"\t\t"+str(gamma_ssim_sum["N1"] / results_len))
print("GAMMA_LACT\t\t"+str(gamma_lact_psnr_sum["N1"] / results_len)+"\t\t"+str(gamma_lact_ssim_sum["N1"] / results_len))
print("###########################")

print("N1.5##################################")
print("Algorithm\t\tPSNR\t\tSSIM")
print("LACT\t\t"+str(lact_psnr_sum["N1.5"] / results_len)+"\t\t"+str(lact_ssim_sum["N1.5"] / results_len))
print("CLAHE\t\t"+str(clahe_psnr_sum["N1.5"] / results_len)+"\t\t"+str(clahe_ssim_sum["N1.5"] / results_len))
print("GAMMA\t\t"+str(gamma_psnr_sum["N1.5"] / results_len)+"\t\t"+str(gamma_ssim_sum["N1.5"] / results_len))
print("GAMMA_LACT\t\t"+str(gamma_lact_psnr_sum["N1.5"] / results_len)+"\t\t"+str(gamma_lact_ssim_sum["N1.5"] / results_len))
print("###########################")

print("ALL WO 0##################################")
print("Algorithm\t\tPSNR\t\tSSIM")
print("LACT\t\t"+str((lact_psnr_sum["N1.5"] + lact_psnr_sum["N1"] + lact_psnr_sum["P1.5"] + lact_psnr_sum["P1"]) / (results_len * 4))+"\t\t"+str((lact_ssim_sum["N1.5"] + lact_ssim_sum["N1"] + lact_ssim_sum["P1.5"] + lact_ssim_sum["P1"]) / (results_len * 4)))
print("CLAHE\t\t"+str((clahe_psnr_sum["N1.5"] + clahe_psnr_sum["N1"] + clahe_psnr_sum["P1.5"] + clahe_psnr_sum["P1"]) / (results_len * 4))+"\t\t"+str((clahe_ssim_sum["N1.5"] + clahe_ssim_sum["N1"] + clahe_ssim_sum["P1.5"] + clahe_ssim_sum["P1"]) / (results_len * 4)))
print("GAMMA\t\t"+str((gamma_psnr_sum["N1.5"] + gamma_psnr_sum["N1"] + gamma_psnr_sum["P1.5"] + gamma_psnr_sum["P1"]) / (results_len * 4))+"\t\t"+str((gamma_ssim_sum["N1.5"] + gamma_ssim_sum["N1"] + gamma_ssim_sum["P1.5"] + gamma_ssim_sum["P1"]) / (results_len * 4)))
print("GAMMA_LACT\t\t"+str((gamma_lact_psnr_sum["N1.5"] + gamma_lact_psnr_sum["N1"] + gamma_lact_psnr_sum["P1.5"] + gamma_lact_psnr_sum["P1"]) / (results_len * 4))+"\t\t"+str((gamma_lact_ssim_sum["N1.5"] + gamma_lact_ssim_sum["N1"] + gamma_lact_ssim_sum["P1.5"] + gamma_lact_ssim_sum["P1"]) / (results_len * 4)))
print("###########################")

print("ALL##################################")
print("Algorithm\t\tPSNR\t\tSSIM")
print("LACT\t\t"+str((lact_psnr_sum["N1.5"] + lact_psnr_sum["N1"] + lact_psnr_sum["P1.5"] + lact_psnr_sum["P1"] + lact_psnr_sum["0"]) / (results_len * 5))+"\t\t"+str((lact_ssim_sum["N1.5"] + lact_ssim_sum["N1"] + lact_ssim_sum["P1.5"] + lact_ssim_sum["P1"] + lact_ssim_sum["0"]) / (results_len * 5)))
print("CLAHE\t\t"+str((clahe_psnr_sum["N1.5"] + clahe_psnr_sum["N1"] + clahe_psnr_sum["P1.5"] + clahe_psnr_sum["P1"] + clahe_psnr_sum["0"]) / (results_len * 5))+"\t\t"+str((clahe_ssim_sum["N1.5"] + clahe_ssim_sum["N1"] + clahe_ssim_sum["P1.5"] + clahe_ssim_sum["P1"] + clahe_ssim_sum["0"]) / (results_len * 5)))
print("GAMMA\t\t"+str((gamma_psnr_sum["N1.5"] + gamma_psnr_sum["N1"] + gamma_psnr_sum["P1.5"] + gamma_psnr_sum["P1"] + gamma_psnr_sum["0"]) / (results_len * 5))+"\t\t"+str((gamma_ssim_sum["N1.5"] + gamma_ssim_sum["N1"] + gamma_ssim_sum["P1.5"] + gamma_ssim_sum["P1"] + gamma_ssim_sum["0"]) / (results_len * 5)))
print("GAMMA_LACT\t\t"+str((gamma_lact_psnr_sum["N1.5"] + gamma_lact_psnr_sum["N1"] + gamma_lact_psnr_sum["P1.5"] + gamma_lact_psnr_sum["P1"] + gamma_lact_psnr_sum["0"]) / (results_len * 5))+"\t\t"+str((gamma_lact_ssim_sum["N1.5"] + gamma_lact_ssim_sum["N1"] + gamma_lact_ssim_sum["P1.5"] + gamma_lact_ssim_sum["P1"] + gamma_lact_ssim_sum["0"]) / (results_len * 5)))
print("###########################")

