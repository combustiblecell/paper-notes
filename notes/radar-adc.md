# 雷达 ADC

来源：Wang et al., *SDDiff: Boost Radar Perception via Spatial-Doppler Diffusion*, arXiv:2506.16936v1  
https://arxiv.org/abs/2506.16936

## 一句话

毫米波雷达天线收到的**原始采样电压序列**（analog-to-digital converter 输出）；SDDiff 从这里出发，而不是从机载 CFAR 已经筛过的稀疏点出发。

## 要点

- 单芯片雷达（文中实验平台：TI AWR1843 + DCA 1000 EVM）把中频信号数字化后得到 ADC。
- 传统链路：ADC → FFT / 测角 → CFAR，得到稀疏、带伪影的点云（§2.1）。
- SDDiff 的选择：`We focus on radar’s information-rich ADC data rather than the sparse points from onboard systems.`（§3.1，第3页）
- ADC 经 FFT 变成 4D cube $`C' \in \mathbb{R}^{R \times A \times E \times D}`$（距离、方位、俯仰、多普勒），再压成 [SDDR](sddr.md)。

## 和相邻概念的对比

| | 雷达 ADC | 机载 CFAR 点 | LiDAR 点 |
|--|----------|--------------|----------|
| 信息量 | 完整回波（强度 + 多普勒轴） | 已被门限砍掉 | 几何准、无多普勒 |
| 噪声 / 鬼影 | 仍在数据里，需后续纯化 | 杂波少但点极稀 | 作 PCE 监督 |
| 在 SDDiff 中 | 编码成 SDDR 的输入 | 对照基线（C.P. 点） | 监督 / GT |

下游：ADC → [SDDR](sddr.md) → [定向扩散 + 迭代多普勒](directional-diffusion-idr.md) → [PCE](pce.md) / [EVE](eve.md)。
