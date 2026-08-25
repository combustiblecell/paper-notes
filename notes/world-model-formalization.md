# 形式化（Problem formulation）

来源：Feng et al., *A Survey of World Models for Autonomous Driving* (arXiv:2501.11260v4) §2  
https://arxiv.org/abs/2501.11260v4

## 一句话

驾驶世界模型 $`\bm{w}`$ 吃历史多视角图像 $`\bm{I}`$ 与 LiDAR 点 $`\bm{P}`$，同时吐出下一步场景 $`\bm{z}`$ 与自车轨迹 $`\tau`$。

## 综述里怎么写

定义（§2.1）：世界模型是把外部环境编成紧凑潜状态的生成式时空网络；无标签压缩传感器，再用隐状态与动作推下一步，在「脑子里」排练整条轨迹。

驾驶任务形式（§2.2 式 (1)）：

```math
\bm{z}^{T+1},\;\tau^{T+1}
=\bm{w}\bigl((\bm{I}^{T},\cdots,\bm{I}^{T-t}),\,(\bm{P}^{T},\cdots,\bm{P}^{T-t})\bigr).
```

两个核心任务：生成未来物理世界（$`\bm{z}`$），以及智能体行为规划（$`\tau`$）。

## 和相邻概念

| 概念 | 差别 |
|------|------|
| [多传感器压成潜状态](multi-sensor-latent-state.md) | 潜状态是 $`\bm{z}`$ 这一侧；形式化还同时要轨迹 $`\tau`$ |
| [图像/BEV/占用/点云](image-bev-og-pc.md) | $`\bm{z}`$ 可以实例化成这四条生成轨 |
| [学习式与规则式](learning-vs-rule-based.md) | 规划任务怎么出 $`\tau`$ |
| [前向模型](forward-model.md) | LeCun 写成 $`\hat{s}_{t+1}=\mathrm{Pred}(s_t,a_t)`$；这里把观测显式写成 $`I,P`$，输出拆成场景+轨迹 |
