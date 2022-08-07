# H-PETR-Pose

This is the official implementation of the paper "[DETRs with Hybrid Matching](https://arxiv.org/abs/2207.13080)". 

Authors: Ding Jia, Yuhui Yuan, Haodi He, Xiaopei Wu, Haojun Yu, Weihong Lin, Lei Sun, Chao Zhang, Han Hu

## Citing H-PETR-Pose
If you find H-PETR-Pose useful in your research, please consider citing:
```bibtex
@article{jia2022detrs,
  title={DETRs with Hybrid Matching},
  author={Jia, Ding and Yuan, Yuhui and He, Haodi and Wu, Xiaopei and Yu, Haojun and Lin, Weihong and Sun, Lei and Zhang, Chao and Hu, Han},
  journal={arXiv preprint arXiv:2207.13080},
  year={2022}
}
```
## Model ZOO

We provide a set of baseline results and trained models available for download:

<table><tbody>
<!-- START TABLE -->
<!-- TABLE HEADER -->
<th valign="bottom">Name</th>
<th valign="bottom">Backbone</th>
<th valign="bottom">epochs</th>
<th valign="bottom">AP (Reproduced / Reported)</th>
<th valign="bottom">download</th>
<!-- TABLE BODY -->
 <tr><td align="left"><a href="configs/petr/petr_r50_8x1_100e_coco_custom.py">Deformable-DETR</a></td>
<td align="center">R50</td>
<td align="center">100</td>
<td align="center">69.3 / 68.8</td>
<td align="center"><a href="https://github.com/HDETR/H-PETR-Pose/releases/download/v1.0.0/r50_baseline.pth">model</a></td>
 <tr><td align="left"><a href="HDETR_opera/configs/petr/petr_r101_8x1_100e_coco_custom.py">Deformable-DETR</a></td>
<td align="center">R101</td>
<td align="center">100</td>
<td align="center">69.9 / 70.0</td>
<td align="center"><a href="https://github.com/HDETR/H-PETR-Pose/releases/download/v1.0.0/r101_baseline.pth">model</a></td>
</tr>
</tr>
 <tr><td align="left"><a href="configs/petr/petr_swin-l-p4-w7-22kto1k_8x1_100e_coco_custom_droppath0.5.py">Deformable-DETR</a></td>
<td align="center">Swin Large</td>
<td align="center">100</td>
<td align="center">73.3 / 73.1</td>
<td align="center"><a href="https://github.com/HDETR/H-PETR-Pose/releases/download/v1.0.0/swinL_baseline.pth">model</a></td>
</tr>
</tr>
 <tr><td align="left"><a href="configs/petr/petr_r50_8x1_100e_coco_t900_group5_ffn2x_dp0_custom.py">H-Deformable-DETR</a></td>
<td align="center">R50</td>
<td align="center">100</td>
<td align="center">70.9</td>
<td align="center"><a href="https://github.com/HDETR/H-PETR-Pose/releases/download/v1.0.0/r50_H-PETR.pth">model</a></td>
</tr>
</tr>
 <tr><td align="left"><a href="configs/petr/petr_r101_8x1_100e_coco_t900_group5_ffn2x_dp0_custom.py">H-Deformable-DETR</a></td>
<td align="center">R101</td>
<td align="center">100</td>
<td align="center">71.0</td>
<td align="center"><a href="https://github.com/HDETR/H-PETR-Pose/releases/download/v1.0.0/r101_H-PETR.pth">model</a></td>
</tr>
</tr>
 <tr><td align="left"><a href="configs/petr/petr_swin-l-p4-w7-22kto1k_8x1_100e_coco_t900_group5_ffn2x_dp0_custom_droppath0.5.py">H-Deformable-DETR</a></td>
<td align="center">Swin Large</td>
<td align="center">100</td>
<td align="center">74.9</td>
<td align="center"><a href="https://github.com/HDETR/H-PETR-Pose/releases/download/v1.0.0/swinL_H-PETR.pth">model</a></td>
</tr>
</tbody></table>

- We use 8 V-100 GPUs and `batch_size = 8` for all experiments. 
- We tune the `droppath` of Swin Large backbone from `0.3` to `0.5` for experiments of baseline and our method.

## Installation
We test our models under ```python=3.7.10,pytorch=1.10.1,cuda=10.2```. Other versions might be available as well.

Please follow [get_started.md](docs/get_started.md) to install the repo.


## Run
### To train a model using 8 cards

```Bash
bash ./tools/dist_train.sh <config_path> 8
```

### To eval a model using 8 cards

```Bash
bash ./tools/dist_test.sh  <config_path> <checkpoint_path> 8 --eval keypoints
```

## Modified files compared to Opera

### To support Hybrid-branch
* opera/models/dense_heads/petr_head.py
* opera/models/dense_heads/\_\_init\_\_.py

### To support checkpoint
* opera/models/utils/transformer.py
* opera/models/utils/\_\_init\_\_.py

