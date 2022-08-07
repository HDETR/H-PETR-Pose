_base_ = './petr_r101_8x1_100e_coco_custom.py'
model = dict(
    bbox_head=dict(
        num_queries_one2many = 900,
        k_one2many = 5,
        transformer=dict(
            two_stage_num_proposals=1200,
            encoder=dict(
                transformerlayers=dict(
                    ffn_dropout=0.0,            
                ),
            ),
            decoder=dict(
                transformerlayers=dict(
                    attn_cfgs=[
                        dict(
                            type="mmcv.MultiheadAttention",
                            embed_dims=256,
                            num_heads=8,
                            dropout=0.0,
                        ),
                        dict(
                            type="opera.MultiScaleDeformablePoseAttention",
                            embed_dims=256,
                        ),
                    ],
                    feedforward_channels=2048,
                    ffn_dropout=0.0,

                ),
            ),
            hm_encoder=dict(
                transformerlayers=dict(
                    ffn_dropout=0.0,
                ),
            ),
            refine_decoder=dict(
                transformerlayers=dict(
                    attn_cfgs=[
                        dict(
                            type="mmcv.MultiheadAttention",
                            embed_dims=256,
                            num_heads=8,
                            dropout=0.0,
                        ),
                        dict(
                            type="mmcv.MultiScaleDeformableAttention",
                            embed_dims=256,
                            im2col_step=128,
                        ),
                    ],
                    ffn_dropout=0.0,
                ),
            ),
        ),
        
    ),
)  # set 'max_per_img=20' for time counting