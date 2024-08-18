sice_dataset_result_file_path = "results.csv"
sice_dataset_result_file = open(sice_dataset_result_file_path)

results_dict = {}

for line in sice_dataset_result_file.readlines():
    # Image path, algorithm [lact | clahe | gamma | gamma_lact], psnr, ssim
    fields = line.split("\t")
    if fields[0] not in results_dict.keys():
        results_dict[fields[0]] = {}
    results_dict[fields[0]][fields[1]] = (float(fields[2]),float(fields[3]))

sice_dataset_result_file.close()

results_len = len(results_dict)

lact_psnr_sum = {
    "?": 0.0
}
lact_ssim_sum = {
    "?": 0.0
}
clahe_psnr_sum = {
    "?": 0.0
}
clahe_ssim_sum = {
    "?": 0.0
}
gamma_psnr_sum = {
    "?": 0.0
}
gamma_ssim_sum = {
    "?": 0.0
}
gamma_lact_psnr_sum = {
    "?": 0.0
}
gamma_lact_ssim_sum = {
    "?": 0.0
}
for key in results_dict.keys():
    lact_psnr, lact_ssim = results_dict[key]["lact"]
    clahe_psnr, clahe_ssim = results_dict[key]["clahe"]
    gamma_psnr, gamma_ssim = results_dict[key]["gamma"]
    gamma_lact_psnr, gamma_lact_ssim = results_dict[key]["gamma_lact"]
    lact_psnr_sum["?"] += lact_psnr
    lact_ssim_sum["?"] += lact_ssim
    clahe_psnr_sum["?"] += clahe_psnr
    clahe_ssim_sum["?"] += clahe_ssim
    gamma_psnr_sum["?"] += gamma_psnr
    gamma_ssim_sum["?"] += gamma_ssim
    gamma_lact_psnr_sum["?"] += gamma_lact_psnr
    gamma_lact_ssim_sum["?"] += gamma_lact_ssim

print("?##################################")
print("Algorithm\t\tPSNR\t\tSSIM")
print("LACT\t\t"+str(lact_psnr_sum["?"] / results_len)+"\t\t"+str(lact_ssim_sum["?"] / results_len))
print("CLAHE\t\t"+str(clahe_psnr_sum["?"] / results_len)+"\t\t"+str(clahe_ssim_sum["?"] / results_len))
print("GAMMA\t\t"+str(gamma_psnr_sum["?"] / results_len)+"\t\t"+str(gamma_ssim_sum["?"] / results_len))
print("GAMMA_LACT\t\t"+str(gamma_lact_psnr_sum["?"] / results_len)+"\t\t"+str(gamma_lact_ssim_sum["?"] / results_len))
print("###########################")