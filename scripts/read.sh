#!/bin/bash
export CUDA_VISIBLE_DEVICES=$1
ckpt_id=$2
images_path=$3
### DEFINE THE ROOT PATH HERE ###
abs_root=/mnt/g/Lab/OCR/clip4str
exp_path=${abs_root}/output/${ckpt_id}
runfile=read.py
python3 ${runfile} ${exp_path} --images_path ${images_path}
