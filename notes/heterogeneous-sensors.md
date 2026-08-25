# 异构传感器（Heterogeneous sensors）

来源：Feng et al., *A Survey of World Models for Autonomous Driving* (arXiv:2501.11260v4) §1–§2；Wang et al., *SDDiff* (arXiv:2506.16936v1)  
https://arxiv.org/abs/2501.11260v4

## 一句话

车上同时有相机、LiDAR、雷达、HD 地图等**物理机理不同**的传感器；世界模型要把它们收进**同一套环境表示**，而不是各做各的流水线。

## 综述里怎么说

感知难点（第2页）：

> “perceiving and understanding dynamic traffic scenarios, which requires fusing heterogeneous sensor streams into an environmental representation.”

驾驶版世界模型（第4页，§2.1）：

> “mapping synchronized camera images, LiDAR sweeps, radar echoes and HD-maps into a single latent scene graph, thereby unifying perception and prediction within one representation.”

未来方向仍把「任意传感器进同一 embedding、少用手调适配器」列为开放问题（§7.2）。

## SDDiff 里的实例

毫米波雷达 ADC 与 LiDAR 点云是典型异构对：雷达有多普勒、易多径鬼影；LiDAR 几何密、作 PCE 监督。SDDiff 用 SDDR 对齐占用与多普勒，而不是只在 CFAR 稀疏点上干活。

## 和相邻概念

| 概念 | 差别 |
|------|------|
| [多传感器压成潜状态](multi-sensor-latent-state.md) | 异构是**输入种类**；压成潜状态是**怎么编码** |
| [多模态](multimodality.md) | 本仓库「多模态」主指预测一对多；跨传感器是 **sensor multimodality**，综述里常叫 heterogeneous / multi-modal fusion |
| [雷达 ADC](radar-adc.md) | 异构集合里的一种输入，不是全部 |
| [SDDR](sddr.md) | 雷达侧把占用+多普勒收成一张量，是单传感器内的「异构特征」对齐 |
