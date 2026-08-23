# 多径「鬼影」（Multipath Ghosting）

来源：Wang et al., *SDDiff*, arXiv:2506.16936v1，§1、§3.2；Yataka et al., 2024（文中引用）  
https://arxiv.org/abs/2506.16936

## 一句话

雷达波经墙、地、金属多次反射后，在**没有真实物体**的栅格上仍出现高回波，看起来像假点；只靠强度做 [PCE](pce.md) 时，鬼影会破坏「密度 vs 去杂波」的平衡。

## 要点

- 原文：`non-object regions may display high reflection intensity due to the notorious “multi-path effect”`（第1页，引 Yataka et al., 2024）。
- 后果：强度高 ≠ 占用真；CFAR 要么漏真点、要么留下 clutter。
- SDDiff 不把鬼影当「再设一个强度门限」解决，而是：
  1. 用 [SDDR](sddr.md) 把多普勒和占用对齐；
  2. [IDR](directional-diffusion-idr.md) 用静止目标的多普勒一致性当 critic——与 Eq. 8 不符的占用被压下去。
- 动机句：`Point cloud density variations … and multi-path-induced ghost points hinder model generalization.`（§3.2，第5页）
- 消融：去掉多普勒后 VPR 77.1% → 65.5%（Table 4），与「只靠强度更易吃鬼影」一致。**这是解读（Interpretation）**，文没有单独报「鬼影检出率」。

Cen & Newman 去杂波（§2.1）被作者标为只适用于高分辨率机械扫描雷达，不适合商用单芯片。

## 和相邻概念的对比

| | 多径鬼影 | 热噪声 / 稀疏 | 动态目标 |
|--|----------|---------------|----------|
| 看起来 | 假占用、高强度 | 点少、乱 | 径向速度不再服从静止 Eq. 8 |
| 强度门限 | 难：真假都亮 | CFAR 本职 | 不是门限问题 |
| SDDiff | IDR + 定向纯化 | 稠密生成 | 文假设场景级以静态为主（§3.2） |

动态目标若占主导，Eq. 8 的 critic 会偏——文未给单独拆分实验，**未找到（Not found）**。
