# ReconDreamer

来源：Ni et al., *ReconDreamer: Crafting World Models for Driving Scene Reconstruction via Online Restoration* (arXiv:2411.19548)；Feng 综述 (arXiv:2501.11260v4) Table 1 放在图像轨 Dreamer 系列  
https://arxiv.org/abs/2411.19548

## 一句话

用世界模型做 **在线修复（DriveRestorer）**，把新轨迹上糊掉的 NeRF/3DGS 渲染补干净，再逐步喂回重建模型，好在大变道（文称可到约 6 m）时仍能渲出可用传感器画面，服务闭环仿真。

## 要解决什么

闭环仿真需要任意新视角的传感器图。NeRF / 3DGS 只在接近训练轨迹时好看，换道、跨多车道就会鬼影。DriveDreamer4D 用预训练世界模型当「数据机器」扩新视角，仍扛不住更大机动。ReconDreamer 不一次性扩完，而是**边训边修、逐步加大机动**。

两块（原文 Figure 2）：

1. **DriveRestorer**：在世界模型上微调，按 HDMap / 3D 框等结构条件，把新轨迹渲染里的伪影修掉（类似扩散去噪）；训练时 mask 天空、远处等难点。
2. **PDUS**（Progressive Data Update Strategy）：机动幅度一点点加大，修好的视频再写进重建训练集，直到收敛。

实验在 Waymo 上选了 8 个交互多的场景。骨干消融里 Restorer 可用 DriveDreamer-2 等视频世界模型（原文 Tab. 4）。

## 综述怎么归类

Feng Table 1：扩散；输入 Image + HDMap + Box；输出 2D Image；数据 **Waymo**（不是 nuScenes）。§3.1 一笔：online restoration，把动态场景视频重建得更准。§7.3 把它写成用在线修复保时间一致性。

注意：综述表格看起来像「再生成一张 2D 图」；原文主任务是 **驾驶场景重建 + 新轨迹渲染**，服务闭环取传感器，不是 DriveDreamer 那种开环出规划轨迹。

原文相对提升（Abstract，相对百分比，不是绝对 IoU）：相对 Street Gaussians，NTA-IoU / NTL-IoU / FID 约 **+24.87% / +6.72% / +29.97%**；大机动上相对 DriveDreamer4D+PVG 的 NTA-IoU 约 **+195.87%**。NTA/NTL-IoU 分别量新轨迹上他车与车道的时空一致性。用户研究胜率原文写相对 DriveDreamer4D+PVG 约 96.88%。不要和 Feng 规划表 L2 混读。

## 和相邻概念

| 概念 | 差别 |
|------|------|
| [DriveDreamer](drivedreamer.md) | 初代：nuScenes 上条件生成视频+开环动作；本条：Waymo 上修新视角重建 |
| DriveDreamer4D | 预训练世界模型直接扩新视角（training-free）；本条强调在线修复 + 渐进更新 |
| [图像/鸟瞰图 BEV/占用/点云](image-bev-og-pc.md) | 综述把它挂在图像轨；几何重建骨架是 3DGS/NeRF，输出仍是渲出来的图 |
| [扩散模型](diffusion-model.md) | DriveRestorer 的修复过程像去噪；不是 SDDiff 雷达纯化 |
| [开环回放](open-loop-replay.md) | 原文批评开环评不准端到端规划，动机是闭环 |
| [可控闭环仿真](controllable-closed-loop.md) | 本条提供「新轨迹上还能看的传感器」；不是改交规、注入长尾的仿真器本身 |
| [多径鬼影](multipath-ghosting.md) | 雷达多径假占用；这里 ghosting 是新视角渲染伪影 |

## 注意

「first to effectively render large maneuvers」是原文自称。Feng 表写 CVPR’24，以 arXiv:2411.19548 为准核对发表信息。
