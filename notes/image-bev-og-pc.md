# 图像 / BEV / 占用 / 点云

来源：Feng et al., *A Survey of World Models for Autonomous Driving* (arXiv:2501.11260v4) §2.2 术语、§3.1、Figure 2  
https://arxiv.org/abs/2501.11260v4

## 一句话

未来物理世界生成的四条轨：图像、鸟瞰 BEV、占用栅格 OG、点云 PC；它们是式 (1) 里场景 $`\bm{z}`$ 的不同落地方式，不是四种互不相干的任务。

## 四条轨（Figure 2）

| 轨 | 生成什么 | 综述里的代价 |
|----|----------|--------------|
| Image | 高保真 2D / 多视角视频 | 外观真，三维几何弱 |
| BEV | 俯视地图级布局 | 便于预测与规划；细 3D 几何、复杂深度关系吃亏 |
| OG | 4D 占用体素 | 静动物体统一、几何更完整；显存算力大 |
| PC | 未来 LiDAR 扫描 | 几何细；稀疏、不规则、算得贵 |

原文把四条轨写成：photoreal frames → map-level layouts → 4D voxels → LiDAR sweeps（§3.1）。

## 和相邻概念

| 概念 | 差别 |
|------|------|
| [形式化](world-model-formalization.md) | 形式化给 $`\bm{z},\tau`$；本条只谈 $`\bm{z}`$ 怎么画出来 |
| [多传感器压成潜状态](multi-sensor-latent-state.md) | 潜状态是压缩后的内部量；四条轨常是解码/生成出来的观测级未来 |
| [SDDR](sddr.md) / [PCE](pce.md) | 雷达占用+多普勒、抽点，是雷达感知表示，不是综述这条「未来 PC 生成」主线 |
| [潜变量生成模型](latent-variable-generative-model.md) | 扩散/VAE 是四条轨里常用的生成器，不是表示本身 |

## 注意

不要把 BEV 占用预报和 3D OG 混成同一种：综述写 OG 预报起源于 BEV 语义占用，再扩到 4D 体素（§3.1.3）。
