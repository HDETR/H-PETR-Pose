_base_ = './petr_r50_8x1_100e_coco_t900_group5_ffn2x_dp0_custom.py'
model = dict(
    backbone=dict(
        depth=101,
        init_cfg=dict(type='Pretrained', checkpoint='torchvision://resnet101')))
