# 激光雷达数据流

来源：Feng et al. 综述 (arXiv:2501.11260v4) §2.1 形式化（`$\bm{P}$`）、§3.1.4 PC Representation、Table 2、§6.3 点云预报  
https://arxiv.org/abs/2501.11260

## 一句话

LiDAR 一帧扫描的原始 3D 点集 `$\bm{P}$`（式 1 的传感器输入之一），在综述里既是世界模型的**输入观测**，又是 PC 轨要**生成/预报的未来**；处理时常投影成 range image 或体素以适配 CNN/Transformer/扩散骨干。

## 数据怎么流

**传感端**：LiDAR 发激光脉冲、测每束往返时间（time of flight）算距离，一帧得到一组带 `$x,y,z$`、反射强度的 3D 点——即综述 §3.1.4 的 PC representation：

> “A PC representation encodes the world as the raw 3D points returned by LiDAR, preserving fine-grained 3D details for vehicles, pedestrians, and surrounding infrastructure.”

**综述里的两种角色**：
- **作为输入**：式 (1) 里 `$\bm{P}^T,\dots,\bm{P}^{T-t}$` 是过去帧 LiDAR 点集，和图像 `$\bm{I}$` 一起喂给世界模型 `$\bm{w}$`。
- **作为输出**：PC 轨（Figure 2d）生成/预报**未来 LiDAR sweep**——`$z^{T+1}$` 落到点云这种观测级表示。

**表示变换**（处理骨干决定）：原始点集不规则、稀疏，直接喂网络难，所以常做投影：
- **range image / range map**：把球坐标投到 2D 距离图，适配 CNN/LSTM（PCP、PCPNet、SPFNet、S2net、LiDARGen、RangeLDM 都走这条）。
- **体素 / 4D 占用格**：离散成体素做时空预报（4DOcc、UNO）。
- **token 化**：VQ-VAE 离散 token 后自回归/扩散（Copilot4D、UltraLiDAR）。
- **神经场**：NeRF 范式做新视角 LiDAR（NFL、Nerf-LiDAR）。

## 综述给的骨干谱系（Table 2，§3.1.4）

| 骨干 | 代表 | 怎么处理 LiDAR 数据 |
|------|------|---------------------|
| CNN | PCP、PCPNet、4DOcc | range image 堆叠成 3D 时空体 / 4D 占用格，3D CNN |
| Transformer | ViDAR、HERMES | 图像+动作编码，自回归解码未来点序列；可微体素渲染 |
| Diffusion | LiDARGen、Copilot4D、RangeLDM、LiDARCrafter | 在 range image 或潜空间去噪；Copilot4D 用 VQ-VAE 离散扩散 |
| 其他 | lidarGeneration(GAN)、UltraLiDAR(VQ-VAE)、Lidarsim(光线追踪+噪声模型)、NFL/Nerf-LiDAR(NeRF) | GAN/Token/物理仿真/神经渲染各路 |

§6.3 点云预报（Table 7，OpenScene-mini）：DFIT-OccWorld-O 平均 CD 0.70、V 变体 0.76，优于 ViDAR 1.58。

## 综述点名的难点

§3.1.4 原文：LiDAR 扫描的 **sparsity and irregular sampling** + 实时算力约束是持续挑战；这正是 LiDAR 点云生成（3D 点云生成的子任务）受关注的原因。§3.1.4 末还批：多数方法只盯 LiDAR 几何先验，**语义感知生成和下游感知一致性**探索有限。

## 和相邻概念

| 概念 | 差别 |
|------|------|
| [雷达 ADC](radar-adc.md) | 雷达原始电压序列→FFT→点，**带多普勒**；LiDAR 是光学测距点云，**无多普勒**、几何更准更密 |
| [PCE](pce.md) | 那是**雷达**回波抽点；LiDAR 点云本身已是稠密 3D 点，不需类似 PCE 的低层抽取 |
| [图像/鸟瞰图 BEV/占用/点云](image-bev-og-pc.md) | 那篇讲四条输出轨；本条是 PC 轨的底层数据流，也作式 (1) 输入 |
| [体素空间](voxel-space.md) | LiDAR 点云可离散成体素做 4D 占用预报；体素是表示，LiDAR 是传感器 |
| [异构传感器](heterogeneous-sensors.md) | LiDAR 是异构传感器之一（和相机/雷达融合）；本条只讲 LiDAR 单链路 |
| [多传感器压成潜状态](multi-sensor-latent-state.md) | LiDAR 点云和图像一起被压成潜状态；本条是压之前的原始观测 |
| [benchmarks](benchmarks.md) | Table 7 在 OpenScene-mini 上用 Chamfer Distance 评 LiDAR 点云预报 |

## 注意

- **LiDAR 点云 ≠ 雷达点云**：LiDAR 光学测距、点密几何准、无多普勒；雷达电磁波、点稀、带多普勒——别因都叫「点云」混读。
- **range image 是处理投影，不是新传感器**：LiDAR 仍只输出 3D 点，range image 是为适配 2D 卷积做的球坐标投影。
- 综述未给「LiDAR 数据流」独立小节，本条把 §2.1 输入 `$\bm{P}$`、§3.1.4 PC Representation、Table 2、§6.3 里的 LiDAR 相关内容归并提炼，未补独立页码。
