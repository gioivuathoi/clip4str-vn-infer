# CLIP4STR for Vietnamese with Multilingual CLIP - from AICS lab

This is code CLIP4STR (Multilingual_CLIP) for inference Vietnamese STR 

##  Table of Contents

<!--ts-->
* [Introduction](#Introduction)
* [Installation](#Installation)
* [Results](#Results)
* [Inference](#Inference)
* [Citations](#Citations)
* [Acknowledgements](#Acknowledgements)
<!--te-->


## Introduction

<div align="justify">

This is inference implementation of CLIP4STR for Vietnamese STR using Multilingual CLIP

The text encoder of original CLIP is swapped by text encoder of Multilingual CLIP
The models is train on Vintext STR dataset and internal synthetic dataset (1M samples)


## Installation

### Prepare data

First of all, you need to download all pre-trained models


- Weights of CLIP4STR with Mulingual_CILIP for Vietnamese STR:
    - [CLIP-ViT-B-16](https://drive.google.com/file/d/1ZA-JuDK6UKrpR7aAX-zvU_IHATeYlyNQ/view?usp=sharing)
    - [xlm-roberta-base-ViT-B-32, finetuned with Vintext 1M](https://drive.google.com/file/d/17DLNRW38dLluHMp96RO5l3oqIvTj1dbi/view?usp=sharing)
    - [M-CLIP--XLM-Roberta-Large-Vit-B-32](https://drive.google.com/drive/folders/1-aCM5xHcHWe2Z4Mw4NlAV3RDxSxP3Koc?usp=sharing)
    - [clip4str-large-vietnamese](https://drive.google.com/file/d/1yI-F9VBWNtZ-VuK_r9zoBjag_iGDat0R/view?usp=sharing)


Generally, pretrained model directorie are organized as follows:
```
${ABSOLUTE_ROOT}
├── clip4str-VN-infer
│   │
│   └── pretrained (download all the  pre-trained weights and put them like this)         
│       ├── clip
│       │   ├── vintext-1M
|       |   |    |__ just_model_epoch_19.pt
│       │   └── ViT-B-16.pt
│       ├── M_clip
|       |   |__ models--M-CLIP--XLM-Roberta-Large-Vit-B-32
│       └── clip4str
|           |__ clip4str-large-epoch=4--step=2084-val_accuracy=85.0748-val_NED=91.7947.ckpt
│

...
```

### Dependency

Requires `Python >= 3.8`
The following commands are tested on a Linux machine with CUDA Driver Version `535.104.05` and CUDA Version: 12.2.
```
pip install -r requirements.txt 
```


## Results on Vintext testset



| Method     | Train data | Word Acc | 1-NED |
|------------|------------|----------|-------|
| PARSEQ–VN  | Vin+ST(1M) |   86.38  | 91.3  |
| CLIP4STR-VN| Vin+ST(1M) |   90.16  | 94.48 |



## Inference

Here I share colab code to run inference: [Colab](https://colab.research.google.com/drive/1FYIs-aMKJvsXyNgPjL-B09ivd3OAPGAz?usp=sharing)
To run the inference for images:
```
python ./read.py ./pretrained/clip4str/clip4str-large-epoch=4--step=2084-val_accuracy=85.0748-val_NED=91.7947.ckpt --images_path ./testset
```
```
Result
1.jpg: BÉO
2.jpg: BÒ
3.jpg: TÂN
4.jpg: DO
5.jpg: VIỄN
```
## Citations

This model is a Vietnamese version (using multilingual CLIP) of CLIP4STR:
```
@article{DBLP:journals/corr/abs-2305-14014,
  author       = {Shuai Zhao and
                  Xiaohan Wang and
                  Linchao Zhu and
                  Yi Yang},
  title        = {{CLIP4STR:} {A} Simple Baseline for Scene Text Recognition with Pre-trained
                  Vision-Language Model},
  journal      = {CoRR},
  volume       = {abs/2305.14014},
  year         = {2023},
  url          = {https://doi.org/10.48550/arXiv.2305.14014},
  doi          = {10.48550/arXiv.2305.14014},
  eprinttype    = {arXiv},
  eprint       = {2305.14014},
  timestamp    = {Mon, 05 Jun 2023 15:42:15 +0200},
  biburl       = {https://dblp.org/rec/journals/corr/abs-2305-14014.bib},
  bibsource    = {dblp computer science bibliography, https://dblp.org}
}
```


## Acknowledgements

This repo is built upon these previous works.

<!--ts-->
[CLIP4STR](https://github.com/VamosC/CLIP4STR)
<!--te-->
