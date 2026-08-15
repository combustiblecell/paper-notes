# 多模态（Multimodality）

来源：LeCun 2022 立场文 §4.1–4.4、Figure 8/12；§4.8 规划中的不确定性  
https://openreview.net/forum?id=BZ5a1r-kVsf

## 一句话

给定过去观察 $`x`$，未来 $`y`$ 往往**不唯一**（路口左转/右转、前车刹车/加速）；世界模型必须能表示**一簇 plausible 结果**，而不是只吐一个平均预测。

## 在本笔记体系里指什么

LeCun 立场文里的「多模态」主要指 **predictive multimodality**（预测多模态）：$`x \to y`$ 是一对多，而非跨模态 VLM 那种「图像+文本」。  
JEPA 也允许 $`x`$ 与 $`y`$ **不同模态**（如 video / audio），两路 encoder 可不同构（§4.4）。

## 为什么必须处理

原文（§4.1，第17页）：

> “there may be an infinite number of $`y`$ that are compatible with a given $`x`$… there is an infinite number of video clips that are plausible continuations of a given clip.”

世界本质上不可完全预测（混沌、部分可观测、其他智能体），硬做**单点预测**会：

- 生成式：输出**模糊平均**（early video prediction without latent）
- 回归式（Figure 10(a)）：只给一个 $`\tilde{y}`$，**无法**表达分支

## 三条主流路线

| 路线 | 做法 | 代表 |
|------|------|------|
| **确定性回归** | 一个 $`x`$ → 一个 $`\tilde{y}`$ | Figure 10(a)；无 latent 的视频预测 → 模糊 |
| **生成式 + 潜变量** | $`z`$ 采样 → 不同像素 $`\tilde{y}`$ | VAE / GAN / VQ-VAE（见 [vae-gan-vqvae.md](vae-gan-vqvae.md)） |
| **JEPA（表征空间）** | 不变性 + 潜变量 → 不同 $`\tilde{s}_y`$ | 见 [jepa.md](jepa.md) |

## JEPA 如何表示多模态

Figure 12 / §4.4 给出**两种方式**（可同时用）：

### 1. 编码器不变性（invariance）

多种不同的 $`y`$ 映到**同一个** $`s_y`$ → 能量相同 → 模型承认「这些未来语义等价」。

### 2. 潜变量 $`z`$（predictor 内）

$`z`$ 扫过集合 $`Z`$ 时，预测器输出一簇合理表征：

```math
\mathrm{Pred}(s_x, Z) = \{\tilde{s}_y = \mathrm{Pred}(s_x, z) \mid z \in Z\}
```

**经典例子**（§4.4，Figure 12）：车 approaching 岔路口——$`s_x, s_y`$ 只保留位置/速度等语义，忽略路边树、人行道纹理；$`z`$ 表示走左支还是右支（离散 $`z=0/1`$）。

能量：$`E = D(s_y, \mathrm{Pred}(s_x, z))`$；正确的 $`z`$ 使能量更低。

## 与 EBM / 潜变量的关系

- EBM $`F(x,y)`$ 天然可表示 **multi-modal dependencies**：多个 $`y`$ 或 $`y`$ 的流形与 $`x`$ 相容（Figure 8，§4.1）。
- 潜变量 EBM：$`\check{z} = \arg\min_z E_w(x,y,z)`$，再得 $`F_w(x,y)`$（见 [latent-variable-generative-model.md](latent-variable-generative-model.md)）。
- 训练时要**限制 $`z`$ 信息量**，否则 predictor 抄 $`z`$、能量面塌缩（§4.5，Figure 13 准则 4）。

## 规划时的多模态（§4.8）

不确定环境下，各层 predictor 的 $`z`$ 采样 → 多条轨迹；离散 $`z`$ 有 $`k`$ 值时，$`t`$ 步后轨迹数可呈 $`k^t`$ 增长，需 **MCTS / pruning**（Figure 17）。  
Actor 可对多条轨迹算期望代价或 risk-aware 代价，而非只押一条未来。

## 和相邻概念的对比

| | 确定性回归 | 生成式 latent | JEPA |
|--|-----------|--------------|------|
| 输出 | 单个 $`\tilde{y}`$ | 多个像素 $`\tilde{y}`$ | 多个 $`\tilde{s}_y`$ |
| 多模态机制 | 无 | $`z`$ → decoder | 不变性 + $`z`$ → predictor |
| 无关细节 | 硬预测 → 模糊 | 塞进 $`z`$ | encoder 可丢弃 |
| 能否「看到」分支 | 否 | 能（生成帧） | 否（嵌入空间，需探针/解码） |

**跨模态**（$`x`$=视频、$`y`$=音频）：JEPA 两路 encoder 可不同构；与 VL-JEPA 等后续工作相关，本立场文仅架构层面允许，未展开训练细节。

## 相关笔记

- [jepa.md](jepa.md) — 多模态在 JEPA 中的两种机制
- [latent-variable-generative-model.md](latent-variable-generative-model.md) — $`z`$ 与能量推断
- [vae-gan-vqvae.md](vae-gan-vqvae.md) — 生成式多模态对照
- [mode-2-planning.md](mode-2-planning.md) — 规划时 rollout 多条未来
