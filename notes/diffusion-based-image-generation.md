# Diffusion-based Image Generation

来源：Feng et al. 综述 (arXiv:2501.11260v4) §3.1.1 Image-based Generation 内的扩散分支；Table 1  
https://arxiv.org/abs/2501.11260

## 一句话

综述 §3.1.1「Image-based Generation」下按骨干网络拆成两条支线之一：用**潜在扩散**从 BEV 布局/文本/光流/轨迹等条件渲染高保真、几何一致的 2D 驾驶图像/视频；另一条支线是 Transformer-based（见对照）。

## 综述怎么说

§3.1.1 把 Image-based Generation 分成三组叙述：Dreamer 系列、**Diffusion-based**、Transformer-based。本条对应中间那组，原文归纳为两个互补方向：

- **可控生成**：BEVControl、DrivingDiffusion、GeoDrive 等，用 latent diffusion 从 BEV 布局、文本提示、光流等丰富条件渲染几何一致的视频。
- **高保真时空建模**：Drive-WM、Vista、LongDWM 把扩散 roll-out 推到更长时域、更高分辨率，提升时间连贯性和逐帧细节。

随后列出多模态条件的演进：自车轨迹 + 人体姿态 + DINO 外观 token 做行为感知视频（Hassan 2024）；级联扩散把仿真器布局转成照片级场景（Zhou 2024）；双尺度 ControlNet-SD（Li 2025c）；LiDAR+相机在 BEV 潜栅格里做跨传感器预报（Zhang 2024a）；潜空间里对齐自车-他车轨迹做全可控多智能体视频（Zhu 2025b）；用自车世界坐标 + 3D 流 + 框引导遮挡推理做物理 grounded 多相机视频（Yang 2024c）。

近期趋势（原文罗列）：RGB → 图像+深度（Liang 2025b）；布局条件 → 细粒度轨迹条件（Li 2025e）；2D 条件 → 多视角一致（Jiang 2025b）；2D 布局 → 全 3D 场景条件（Ji 2025）；单视角 → 多视角多智能体交互（Russell 2025）；短片段 → 长时域（Wang 2025a）；失败案例增强稳健性（Ma 2024b）；事故预期 benchmark（Guan 2025）。InfiniCube（Lu 2025）用世界引导的视频扩散（HD map + 3D 框 + 文本）生成长时视频，再前馈重建为动态 3D 高斯场景。

Table 1 里归到这一支的代表：BEVControl（Diffusion Model，BEV+Image+Text → 2D Image，nuScenes）等。输出仍属综述四条轨的 **Image**。

## 和相邻概念

| 概念 | 差别 |
|------|------|
| [图像/鸟瞰图 BEV/占用/点云](image-bev-og-pc.md) | 本条是 Image 轨的扩散支线；那篇讲四条输出轨的整体区别 |
| [扩散模型](diffusion-model.md) | 那是扩散模型本身的方法论；本条是它在「图像轨未来生成」里的应用谱系 |
| Transformer-based Image Generation（未单列笔记） | 同属 §3.1.1 的另一支：HoloDrive/BEVGen/GAIA-1/DrivingWorld 等，走 token 序列建模而非扩散去噪 |
| [DriveDreamer](drivedreamer.md) / [DriveDreamer-2](drivedreamer-2.md) / [ReconDreamer](recondreamer.md) | Dreamer 系列在 §3.1.1 里单列一组叙述，和 Diffusion-based / Transformer-based 并列；DriveDreamer 本身用扩散，可看作这条支线的代表之一，但综述把它归到 Dreamer 系列叙事 |
| [WorldDreamer](worlddreamer.md) | 走 Transformer 掩码预测，属另一支；和扩散支线对照 |
| [长尾场景](long-tail-scenario.md) | 扩散支线常被用来补稀有数据，是长尾场景的生成手段之一 |
| [开环回放](open-loop-replay.md) | 生成的图像/视频多用于数据增强和开环评估，不直接响应在线控制 |

## 注意

「Diffusion-based Image Generation」是综述 §3.1.1 的**叙事分组名**，不是某篇论文的自称模型名。它和 Dreamer 系列在 §3.1.1 里是并列的两组叙述（Dreamer 系列横跨扩散与 Transformer，所以别把 DriveDreamer 简单等同于本条）。具体方法名、年份、出处均按综述原文，未补页码（综述未给本条独立页码）。
