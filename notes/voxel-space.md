# 体素空间

来源：Feng et al. 综述 (arXiv:2501.11260v4) §3.1.3 OG Representation、§6.1、§7.1；InfiniCube (Lu et al., ICCV 2025)  
https://arxiv.org/abs/2501.11260

## 一句话

把驾驶场景沿三维切成均匀小格子（voxel），每个格子存占用概率/语义/特征——是 [OG 占用预报](image-bev-og-pc.md) 的底座，也是 InfiniCube 这类生成-重建管线的中间世界表示。

## 是什么

**体素（voxel）= 3D 像素**。把自车周围空间离散成 `$H\!\times\!W\!\times\!D$` 的网格，每格挂一个或几个量：占用概率、语义类别、几何特征、甚至高斯属性。综述 §3.1.3 原文：

> “An OG representation divides the driving scene into 3D voxels and assigns each cell a probability of being occupied, producing a single lattice that simultaneously tracks static structure and moving actors.”

和 BEV 的根本差别：BEV 是**俯视投影**（2D，深度被压扁），体素空间是**完整 3D 离散**，能保留竖直方向几何（天桥、悬挂标志、高低路面）。代价是显存和算力随分辨率立方增长。

## 综述里怎么用

- **作为表示**：OG 占用预报（§3.1.3）和 4D 占用预报（§6.4，Table 8）都在体素空间里做；评测平台 Occ3D-nuScenes / Occ3D-Waymo / CarlaSC 给的就是体素标注（CarlaSC 是 `$128\!\times\!128\!\times\!8$`）。
- **作为骨干运算空间**：MUVO 在 voxel-level Transformer 融相机+LiDAR；InfiniCube 的 voxel 分支用 **3D 稀疏卷积 U-Net** 在体素上出每体素高斯属性；Occupancy-MAE 直接 mask 体素做自监督。
- **作为生成中间态**：InfiniCube 三段管线的第一段就是「map + 3D 框 → 生成 3D voxel world」，再把 voxel 渲染成 guidance buffer 去引导视频扩散，最后前馈重建 lift 成动态 3DGS。

## 体素空间的几个变体/省内存招数

综述 §3.1.3 / §7.1 反复提：**稠密体素显存贵**，所以一路在减负：

| 招数 | 例子 | 思路 |
|------|------|------|
| 稀疏体素 | InfiniCube voxel 分支、Occupancy-MAE | 只在非空处算，3D 稀疏卷积 |
| 体素 token 化 | OccWorld、DFIT-OccWorld、OccLLaMA | 把体素切成离散 token 自回归预测 |
| 三平面 / HexPlane | T3Former（triplane）、DynamicCity（HexPlane+DiT） | 把 4D 体素投影到几个 2D 平面再 roll |
| 升级到高斯 | GaussianWorld、RenderWorld、InfiniCube 终态 | “from voxel fusion to tokenisation and further to Gaussian splats”（§3.1.3 末），用 3DGS 替体素降显存、提渲染速度 |

## 和相邻概念

| 概念 | 差别 |
|------|------|
| [图像/鸟瞰图 BEV/占用/点云](image-bev-og-pc.md) | 那篇讲四条**输出轨**；体素空间是 OG 轨的底座，也常作内部表示 |
| OG（占用栅格） | OG 是**任务/输出**（预测占用）；体素空间是 OG 赖以表达的**表示/离散方式**——别混 |
| [benchmarks](benchmarks.md) | CarlaSC/Occ3D-nuScenes/Occ3D-Waymo 给体素标注；Table 8 在体素空间评 mIoU/IoU |
| InfiniCube（未单列笔记） | 用体素世界做 world-guided 视频扩散的中间态，再前馈重建出动态 3DGS |
| 3DGS（未单列笔记） | 显式高斯点云式表征，实时渲染；体素是离散网格，3DGS 是连续点集——综述说趋势从体素迁向高斯 |
| [多传感器压成潜状态](multi-sensor-latent-state.md) | 潜状态是压缩后的连续向量；体素空间是离散网格观测级表示，两者可互转 |

## 注意

- **「体素空间」≠「OG」**：OG 专指占用预报任务，体素空间是更底层的表示概念，OG 只是它的一种用法。
- **稠密 vs 稀疏**：综述批评的多是稠密体素的显存压力；实际系统常用稀疏体素或三平面绕开。
- 综述未给「体素空间」独立小节定义，本条是把 §3.1.3 OG Representation、§6.1 平台描述、§7.1 趋势句里的体素相关内容归并提炼，未补独立页码。
