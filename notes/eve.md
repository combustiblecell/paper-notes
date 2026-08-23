# EVE（Ego Velocity Estimation，自车速度估计）

来源：Wang et al., *SDDiff*, arXiv:2506.16936v1，§1、§2.3、§5.2  
https://arxiv.org/abs/2506.16936

## 一句话

从雷达观测推断**雷达自身相对于地面的速度**；SDDiff 把它当成与 [PCE](pce.md) 互惠的高层认知，而不是在机载稀疏点上单独回归。

## 要点

- 原文：`EVE serves as a high-level cognitive process, leveraging elemental point clouds to infer the radar’s ego velocity.`（第1页）
- 几何：静止目标的径向速度由 $`v_{\mathrm{ego}}`$ 与方位/俯仰决定，见 [定向扩散 + IDR](directional-diffusion-idr.md) Eq. 8。
- 前人路线（§2.3）：
  - 帧间配准 ICP / NDT：雷达点噪声大、点对点对应差
  - RANSAC / RadarEVE：吃机载稀疏点；开阔地点数少会明显掉点甚至失败
- 本文宣称：从单芯片 raw ADC 同时做稠密 PCE 与 **3D** EVE（§2.3 末）

## 本文数字

Table 3（第7页），MAE 室内/室外 (m/s)：

| 方法 | 室内 | 室外 |
|------|------|------|
| ICP | 0.60 | 0.77 |
| RANSAC | 0.31 | 0.57 |
| RadarEVE | 0.13 | 0.27 |
| SDDiff | **0.09** | **0.11** |

正文：`improves EVE by 30% and 59% over the state-of-the-art in indoor and outdoor scenarios, respectively.`（§5.2，第6页）  
室外这一档单独见 [室外 EVE](outdoor-eve.md)。

## 和相邻概念的对比

| | EVE | PCE | 配准式里程计 |
|--|-----|-----|--------------|
| 输入 | 多普勒 + 占用（或稀疏点） | 回波 / SDDR | 相邻两帧点 |
| 输出 | $`v_{\mathrm{ego}}`$ | 三维点 | 位姿增量 |
| 本文耦合 | IDR 用速度约束占用 | 纯化占用给 EVE 更多 inlier | 不作主路径 |

SOTA 对照对象在本文评测里主要是 RadarEVE，见 [sota.md](sota.md)。
