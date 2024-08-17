
metu_dataset_result_file_path = "metu_results.csv"
metu_dataset_result_file = open(metu_dataset_result_file_path)

results_dict = {}

for line in metu_dataset_result_file.readlines():
    # Image path, algorithm [lact | clahe | gamma], psnr, ssim
    fields = line.split("\t")
    if fields[0] not in results_dict.keys():
        results_dict[fields[0]] = {}
    results_dict[fields[0]][fields[1]] = (float(fields[2]),float(fields[3]))

metu_dataset_result_file.close()

results_len = len(results_dict) / 4
lact_psnr_sum = {
    "0": 0.0,
    "N3": 0.0,
    "P3": 0.0,
    "HDR": 0.0
}
lact_ssim_sum = {
    "0": 0.0,
    "N3": 0.0,
    "P3": 0.0,
    "HDR": 0.0
}
clahe_psnr_sum = {
    "0": 0.0,
    "N3": 0.0,
    "P3": 0.0,
    "HDR": 0.0
}
clahe_ssim_sum = {
    "0": 0.0,
    "N3": 0.0,
    "P3": 0.0,
    "HDR": 0.0
}
gamma_psnr_sum = {
    "0": 0.0,
    "N3": 0.0,
    "P3": 0.0,
    "HDR": 0.0
}
gamma_ssim_sum = {
    "0": 0.0,
    "N3": 0.0,
    "P3": 0.0,
    "HDR": 0.0
}
gamma_lact_psnr_sum = {
    "0": 0.0,
    "N3": 0.0,
    "P3": 0.0,
    "HDR": 0.0
}
gamma_lact_ssim_sum = {
    "0": 0.0,
    "N3": 0.0,
    "P3": 0.0,
    "HDR": 0.0
}
for key in results_dict.keys():
    lact_psnr, lact_ssim = results_dict[key]["lact"]
    clahe_psnr, clahe_ssim = results_dict[key]["clahe"]
    gamma_psnr, gamma_ssim = results_dict[key]["gamma"]
    gamma_lact_psnr, gamma_lact_ssim = results_dict[key]["gamma_lact"]
    image_index = int(key.split("/")[-1].split(".")[0].split("_")[-1])
    remain = image_index % 4
    if remain == 1:
        lact_psnr_sum["0"] += lact_psnr
        lact_ssim_sum["0"] += lact_ssim
        clahe_psnr_sum["0"] += clahe_psnr
        clahe_ssim_sum["0"] += clahe_ssim
        gamma_psnr_sum["0"] += gamma_psnr
        gamma_ssim_sum["0"] += gamma_ssim
        gamma_lact_psnr_sum["0"] += gamma_lact_psnr
        gamma_lact_ssim_sum["0"] += gamma_lact_ssim
    elif remain == 2:
        lact_psnr_sum["N3"] += lact_psnr
        lact_ssim_sum["N3"] += lact_ssim
        clahe_psnr_sum["N3"] += clahe_psnr
        clahe_ssim_sum["N3"] += clahe_ssim
        gamma_psnr_sum["N3"] += gamma_psnr
        gamma_ssim_sum["N3"] += gamma_ssim
        gamma_lact_psnr_sum["N3"] += gamma_lact_psnr
        gamma_lact_ssim_sum["N3"] += gamma_lact_ssim
    elif remain == 3:
        lact_psnr_sum["P3"] += lact_psnr
        lact_ssim_sum["P3"] += lact_ssim
        clahe_psnr_sum["P3"] += clahe_psnr
        clahe_ssim_sum["P3"] += clahe_ssim
        gamma_psnr_sum["P3"] += gamma_psnr
        gamma_ssim_sum["P3"] += gamma_ssim
        gamma_lact_psnr_sum["P3"] += gamma_lact_psnr
        gamma_lact_ssim_sum["P3"] += gamma_lact_ssim
    elif remain == 0:
        lact_psnr_sum["HDR"] += lact_psnr
        lact_ssim_sum["HDR"] += lact_ssim
        clahe_psnr_sum["HDR"] += clahe_psnr
        clahe_ssim_sum["HDR"] += clahe_ssim
        gamma_psnr_sum["HDR"] += gamma_psnr
        gamma_ssim_sum["HDR"] += gamma_ssim
        gamma_lact_psnr_sum["HDR"] += gamma_lact_psnr
        gamma_lact_ssim_sum["HDR"] += gamma_lact_ssim

print("HDR##################################")
print("Algorithm\t\tPSNR\t\tSSIM")
print("LACT\t\t"+str(lact_psnr_sum["HDR"] / results_len)+"\t\t"+str(lact_ssim_sum["HDR"] / results_len))
print("CLAHE\t\t"+str(clahe_psnr_sum["HDR"] / results_len)+"\t\t"+str(clahe_ssim_sum["HDR"] / results_len))
print("GAMMA\t\t"+str(gamma_psnr_sum["HDR"] / results_len)+"\t\t"+str(gamma_ssim_sum["HDR"] / results_len))
print("GAMMA_LACT\t\t"+str(gamma_lact_psnr_sum["HDR"] / results_len)+"\t\t"+str(gamma_lact_ssim_sum["HDR"] / results_len))
print("###########################")

print("0##################################")
print("Algorithm\t\tPSNR\t\tSSIM")
print("LACT\t\t"+str(lact_psnr_sum["0"] / results_len)+"\t\t"+str(lact_ssim_sum["0"] / results_len))
print("CLAHE\t\t"+str(clahe_psnr_sum["0"] / results_len)+"\t\t"+str(clahe_ssim_sum["0"] / results_len))
print("GAMMA\t\t"+str(gamma_psnr_sum["0"] / results_len)+"\t\t"+str(gamma_ssim_sum["0"] / results_len))
print("GAMMA_LACT\t\t"+str(gamma_lact_psnr_sum["0"] / results_len)+"\t\t"+str(gamma_lact_ssim_sum["0"] / results_len))
print("###########################")

print("N3##################################")
print("Algorithm\t\tPSNR\t\tSSIM")
print("LACT\t\t"+str(lact_psnr_sum["N3"] / results_len)+"\t\t"+str(lact_ssim_sum["N3"] / results_len))
print("CLAHE\t\t"+str(clahe_psnr_sum["N3"] / results_len)+"\t\t"+str(clahe_ssim_sum["N3"] / results_len))
print("GAMMA\t\t"+str(gamma_psnr_sum["N3"] / results_len)+"\t\t"+str(gamma_ssim_sum["N3"] / results_len))
print("GAMMA_LACT\t\t"+str(gamma_lact_psnr_sum["N3"] / results_len)+"\t\t"+str(gamma_lact_ssim_sum["N3"] / results_len))
print("###########################")

print("P3##################################")
print("Algorithm\t\tPSNR\t\tSSIM")
print("LACT\t\t"+str(lact_psnr_sum["P3"] / results_len)+"\t\t"+str(lact_ssim_sum["P3"] / results_len))
print("CLAHE\t\t"+str(clahe_psnr_sum["P3"] / results_len)+"\t\t"+str(clahe_ssim_sum["P3"] / results_len))
print("GAMMA\t\t"+str(gamma_psnr_sum["P3"] / results_len)+"\t\t"+str(gamma_ssim_sum["P3"] / results_len))
print("GAMMA_LACT\t\t"+str(gamma_lact_psnr_sum["P3"] / results_len)+"\t\t"+str(gamma_lact_ssim_sum["P3"] / results_len))
print("###########################")

print("ALL WO HDR##################################")
print("Algorithm\t\tPSNR\t\tSSIM")
print("LACT\t\t"+str((lact_psnr_sum["P3"] + lact_psnr_sum["0"] + lact_psnr_sum["N3"]) / (results_len * 3))+"\t\t"+str((lact_ssim_sum["P3"] + lact_ssim_sum["0"] + lact_ssim_sum["N3"]) / (results_len * 3)))
print("CLAHE\t\t"+str((clahe_psnr_sum["P3"] + clahe_psnr_sum["0"] + clahe_psnr_sum["N3"]) / (results_len * 3))+"\t\t"+str((clahe_ssim_sum["P3"] + clahe_ssim_sum["0"] + clahe_ssim_sum["N3"]) / (results_len * 3)))
print("GAMMA\t\t"+str((gamma_psnr_sum["P3"] + gamma_psnr_sum["0"] + gamma_psnr_sum["N3"]) / (results_len * 3))+"\t\t"+str((gamma_ssim_sum["P3"] + gamma_ssim_sum["0"] + gamma_ssim_sum["N3"]) / (results_len * 3)))
print("GAMMA_LACT\t\t"+str((gamma_lact_psnr_sum["P3"] + gamma_lact_psnr_sum["0"] + gamma_lact_psnr_sum["N3"]) / (results_len * 3))+"\t\t"+str((gamma_lact_ssim_sum["P3"] + gamma_lact_ssim_sum["0"] + gamma_lact_ssim_sum["N3"]) / (results_len * 3)))
print("###########################")

print("ALL##################################")
print("Algorithm\t\tPSNR\t\tSSIM")
print("LACT\t\t"+str((lact_psnr_sum["P3"] + lact_psnr_sum["0"] + lact_psnr_sum["N3"] + lact_psnr_sum["HDR"]) / (results_len * 4))+"\t\t"+str((lact_ssim_sum["P3"] + lact_ssim_sum["0"] + lact_ssim_sum["N3"] + lact_ssim_sum["HDR"]) / (results_len * 4)))
print("CLAHE\t\t"+str((clahe_psnr_sum["P3"] + clahe_psnr_sum["0"] + clahe_psnr_sum["N3"] + clahe_psnr_sum["HDR"]) / (results_len * 4))+"\t\t"+str((clahe_ssim_sum["P3"] + clahe_ssim_sum["0"] + clahe_ssim_sum["N3"] + clahe_ssim_sum["HDR"]) / (results_len * 4)))
print("GAMMA\t\t"+str((gamma_psnr_sum["P3"] + gamma_psnr_sum["0"] + gamma_psnr_sum["N3"] + gamma_psnr_sum["HDR"]) / (results_len * 4))+"\t\t"+str((gamma_ssim_sum["P3"] + gamma_ssim_sum["0"] + gamma_ssim_sum["N3"] + gamma_ssim_sum["HDR"]) / (results_len * 4)))
print("GAMMA_LACT\t\t"+str((gamma_lact_psnr_sum["P3"] + gamma_lact_psnr_sum["0"] + gamma_lact_psnr_sum["N3"] + gamma_lact_psnr_sum["HDR"]) / (results_len * 4))+"\t\t"+str((gamma_lact_ssim_sum["P3"] + gamma_lact_ssim_sum["0"] + gamma_lact_ssim_sum["N3"] + gamma_lact_ssim_sum["HDR"]) / (results_len * 4)))
print("###########################")

