# Luminance Aware Color Transform For Multiple Exposure Correction

## Introduction

This repository is a benchmark for comparing Luminance Aware Color Transform For Multiple Exposure Correction article implementation with classical methods for exposure correction.

## Installation

Warning : There may be version conflict with installed packages before. It is preferred to use python environment.

### Example Python Environment

```
python3 -m venv <environment-name>
source <environment-name>/bin/activate
```

### Requirements

```
pip3 install -r requirements.txt
```

## Getting Started

### Tested Environment

OS : Ubuntu 24.04 LTS

CPU : Intel® Core™ i7-10750H × 12

RAM : 24.0 GiB

GPU : NVIDIA GeForce GTX 1650 Ti

Warning : Due to GPU in the tested environment was not sufficient for inferencing, CPU was used for inference.

### GPU-CPU Settings

If you want to use GPU

```
export CUDA_VISIBLE_DEVICES=<your-cuda-device>
```

Note : Do not forget to add cudnn path to these environment variables

```
export CUDNN_PATH=/path/to/python/cudnn
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/path/to/python/cudnn/lib
```

If you want to use CPU

```
export CUDA_VISIBLE_DEVICES=""
```

### Resources

Pretrained model weight file for the LACT is provided in the repository. (use this when necessary as path : lact/weights/ckpt)

If you want to validate, refer to original LACT repository [LACT Github](https://github.com/whdgusdl48/Luminance-aware-Color-Transform-ICCV-2023-)

Because original dataset is approximately 2.9GB, resized dataset is provided for you.

If you want to use original dataset, please download it from : [DRIVE-LINK]()

```
unzip <dataset-name>.zip
```

## Running

### Experimentation

```
python3 experiment.py -d "/path/to/dataset/" -j "/path/to/dataset/test.json" -c "lact/weights/ckpt" -i <resize-width> <resize-height> -o "path/to/output/results/file/<file-name>.<file-extension>" -p "/path/to/merged/prediction/results/directory/"
```

The images in dataset is resized by <resize-width>x<resize-height> before inferencing or applying an algorithm. Set this value according to your RAM/GPU-RAM.

Please note that the values of directory inputs (-d, -p) expects "/" character at the end.

### Results

Results are stored in file specified in the experiment script parameters that is executed. Specifically for METU Dataset (the dataset provided to you.) You can parse the results with respect to 0, N3, P3, HDR exposure corrections.

### bibtex
```
@InProceedings{Baek_2023_ICCV,
    author    = {Baek, Jong-Hyeon and Kim, DaeHyun and Choi, Su-Min and Lee, Hyo-jun and Kim, Hanul and Koh, Yeong Jun},
    title     = {Luminance-aware Color Transform for Multiple Exposure Correction},
    booktitle = {Proceedings of the IEEE/CVF International Conference on Computer Vision (ICCV)},
    month     = {October},
    year      = {2023},
    pages     = {6156-6165}
}
```