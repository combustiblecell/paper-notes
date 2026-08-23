# SDDR（Spatial-Doppler Domain Representation）

来源：Wang et al., *SDDiff*, arXiv:2506.16936v1，§3.1、Figure 3  
https://arxiv.org/abs/2506.16936

## 一句话

一张同时带**空间占用**和**多普勒速度**的极性 3D 张量；PCE 与 EVE 被定义成把粗糙、易鬼影的 SDDR 纯化成干净 SDDR。

## 要点

设计原则（§3.1）：（1）尽量不丢空间占用与多普勒；（2）能砍的冗余就砍，省算力与显存。

步骤：

1. [雷达 ADC](radar-adc.md) FFT 得 $`C' \in \mathbb{R}^{R \times A \times E \times D}`$
2. 空间位置 $`s_{k,i,j}=(r_k,a_i,e_j)`$ 上，沿多普勒轴取**峰值下标**当径向速度 $`v`$（经验：有点时第一峰通常 ≥ 第二峰的 $`6\times`$）
3. 强度 $`u`$（占用）与速度 $`v`$ 拼接：

```math
C = [u; v] \in \mathbb{R}^{R \times A \times E \times 2}
```

LiDAR 点按同一雷达极性包成占用，作为纯化目标。原文：`PCE and EVE are jointly refined through SDDR Purification Process, sculpting coarse, ghost-prone representations into fine, uncontaminated ones.`（第2页）

## 和相邻概念的对比

| | SDDR | 仅强度 RA / BEV 图 | CFAR 稀疏点 |
|--|------|-------------------|-------------|
| 空间 | 极性 $`R\times A\times E`$ | 多为 2D | 无规则网格 |
| 多普勒 | 与占用对齐的一通道 | 通常没有 | 点上有，但点太少 |
| 本文批评 | — | RadarHD / RadarDiff「overlook … Doppler features」（§2.2） | EVE 吃稀疏点会在开阔地失效（§2.3） |

纯化手段见 [定向扩散 + 迭代多普勒](directional-diffusion-idr.md)。鬼影如何污染占用见 [多径鬼影](multipath-ghosting.md)。
