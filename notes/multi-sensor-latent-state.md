# 多传感器压成潜状态

来源：Feng et al., *A Survey of World Models for Autonomous Driving* (arXiv:2501.11260v4) §1–§2；LeCun 2022 立场文（表征空间预测）  
https://arxiv.org/abs/2501.11260v4

## 一句话

把相机/LiDAR 等原始观测**压缩**成紧凑的内部状态 $`z`$（或 $`s`$），再在这个状态上按假设动作往前滚，而不是直接在像素或原始点云上做长期预测。

## 综述定义

世界模型（第2页）：

> “a generative spatio-temporal neural system that compresses multi-sensor physical observations into a compact latent state and rolls it forward under hypothetical actions, letting the vehicle rehearse futures before they occur.”

更展开（第4页，§2.1）：无标签压缩传感器 → 时间模块用隐状态与动作推下一步 → 全可微，可当虚拟沙盒。驾驶任务形式（式 (1)）是历史图像 $`I`$ 与点云 $`P`$ 同时推出下一场景 $`z_{T+1}`$ 与自车轨迹 $`\tau_{T+1}`$。

## 和 LeCun / JEPA 的衔接

LeCun 路线同样强调**不要在像素里预测一切细节**，而是在表征 $`s_x,s_y`$ 里预测（见 [jepa](jepa.md)、[前向模型](forward-model.md)）。综述的 latent state 是驾驶文献里的同一类想法：压缩 → 前滚 → 规划。JEPA 还主张非生成式、丢掉不可预测细节；驾驶综述里大量工作仍用扩散生成图像/占用（对照 [潜变量生成模型](latent-variable-generative-model.md)）。

## 和相邻概念

| 概念 | 差别 |
|------|------|
| [异构传感器](heterogeneous-sensors.md) | 多种输入；本条是压成**一个**（或一层）潜状态 |
| [前向模型](forward-model.md) | Pred 吃的是已经压好的 $`s`$，不是原始 $`I,P`$ |
| [Mode-2 规划](mode-2-planning.md) | 在潜状态 rollout 上做能量最小化 / 轨迹选择 |
| [长尾场景](long-tail-scenario.md) | 潜空间想象可用来补稀有未来，降低真车试错 |
