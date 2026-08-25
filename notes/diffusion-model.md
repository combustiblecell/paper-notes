# 扩散模型（Diffusion models）

来源：Feng et al., *A Survey of World Models for Autonomous Driving* (arXiv:2501.11260v4) §2.2、§3.1、§8；Wang et al., *SDDiff* (arXiv:2506.16936v1) §3.1（对照「常规 DDPM」）  
https://arxiv.org/abs/2501.11260v4

## 一句话

先把数据逐步加噪，再学一个网络把噪声一步步剥回去，从而**采样**出新的图像、占用或点云；驾驶综述里它是补长尾、画未来世界的主力生成器，不是 JEPA 那种只预测表征。

## 机制（本仓库用到的程度）

1. **正向**：干净样本 $`x_0`$ 逐步变成近高斯噪声（常规 DDPM 从标准高斯起步）。
2. **反向**：噪声网络 $`\epsilon_\theta`$（或等价地预测 $`x_0`$）按时间步去噪，得到新样本。
3. **条件**：布局、轨迹、文本、动作、雷达先验等可以喂进去噪网络，用来控内容。

Feng §2.2 把 VAE 与 diffusion 并列为驾驶仿真里的生成模型，用于轨迹预测、稀有事件合成、不确定性。结论里写：

> “Generative methods, particularly diffusion-based approaches, now facilitate diverse synthetic data for long-tail scenarios…”

综述图像/占用/点云轨里常见变体（名称以各论文为准，此处不展开数字）：

| 变体 | 在本仓库里出现的用法 |
|------|----------------------|
| 像素/占用上的扩散 | OccSora 等 4D 占用生成 |
| **Latent diffusion** | 先压到潜空间再扩；DrivingDiffusion 一类多视角视频 |
| **DiT** | 用 Transformer 当去噪骨干（如 DynamicCity 的 HexPlane+DiT） |
| 雷达定向扩散 | 不从纯高斯走，从雷达占用先验走向 LiDAR 占用，见 [定向扩散 + IDR](directional-diffusion-idr.md) |

LeCun 2022 立场文对照的是 VAE/GAN/VQ-VAE，**未把扩散写成主对照**；本条不把扩散塞进那篇的 Figure 10。

## 和相邻概念

| 概念 | 差别 |
|------|------|
| [VAE / GAN / VQ-VAE](vae-gan-vqvae.md) | 同属观测空间生成；扩散用逐步去噪，不是一次解码或对抗 |
| [潜变量生成模型](latent-variable-generative-model.md) | 扩散采样时的噪声/时间步扮演「未观测自由度」；仍会画出 $`y`$，JEPA 不画 |
| [JEPA](jepa.md) | 非生成式、预测 $`s_y`$；扩散要重建或合成像素/体素/点 |
| [图像/鸟瞰图 BEV/占用/点云](image-bev-og-pc.md) | 四条轨是**表示**；扩散常是上面的**生成器** |
| [长尾场景](long-tail-scenario.md) | 综述把扩散当成补稀有数据的主要手段之一 |
| [定向扩散 + IDR](directional-diffusion-idr.md) | 雷达纯化任务上的特化：先验 + 多普勒 critic，不是通用文生视频 |
| [开环回放](open-loop-replay.md) | 很多扩散驾驶视频仍不响应在线动作；生成器 ≠ 闭环世界模型 |

## 注意

不要把「用了扩散」写成「就是世界模型」：Ding/Zhu 对 Sora 的保留（缺动作因果、物理不稳）同样适用于开环扩散视频。也不要把 SDDiff 的 PCE 数字和 Feng 表里的 OccSora/DynamicCity 生成分数加在一起。
