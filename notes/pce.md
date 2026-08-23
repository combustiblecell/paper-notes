# PCE（Point Cloud Extraction，点云提取）

来源：Wang et al., *SDDiff*, arXiv:2506.16936v1，§1、§4.3、§5.1  
https://arxiv.org/abs/2506.16936

## 一句话

从雷达回波里抽出三维点（位置、反射、多普勒）的**低层传感**；SDDiff 把它和 [EVE](eve.md) 绑在同一套 [SDDR](sddr.md) 纯化里做，而不是只看强度图。

## 要点

- 原文角色：`PCE acts as a low-level sensory process, extracting fundamental object information from reflected radar signals, including position, reflectivity, and Doppler velocity.`（第1页）
- 单独做 PCE 的问题：多径让非目标区也高亮，`relying solely on signal intensity may mislead PCE`（第1页）；密度与去杂波难兼顾。
- 与 EVE 的互惠（Fig. 2）：更准的 ego velocity 可按多普勒筛点；更密、更干净的点反过来抬 EVE。CFAR 点室内 inlier 约 25.9%，LiDAR-warped 达 98.6%（第1–2页）。

## 本文指标与数字

定义（§4.3）：VPR = $`1-|P_{\mathrm{clutter}}|/|P|`$；SRL = $`|Q_{\mathrm{shot}}|/|Q|`$；EGD = $`|(P-P_{\mathrm{clutter}})|/|Q_{\mathrm{shot}}|`$。阈值 $`\tau_1,\tau_2`$ 的具体数值 **未找到（Not found）**。

- 文称相对 SOTA：VPR +30%、SRL +33%（§5.1，第6页）
- Table 1 Classroom：SDDiff EMD/CD = 0.25 / 0.24（第7页）
- Table 4 完整模型：VPR 77.1%，SRL 79.6%，EGD 1.17
- Abstract 写 `4× greater in valid generation density`（第1页）；正文表内 EGD 为 1.17，**4× 的计算式未找到（Not found）**

基线：OS-CFAR、RPDNet、RadarHD、RadarDiff、Modified 3D-Diff（§4.3）。

## 和相邻概念的对比

| | PCE | EVE |
|--|-----|-----|
| 层级 | 传感（抽点） | 认知（由点/表示推断自车速度） |
| 失败模式 | 鬼影、漏检、2D 无俯仰 | 点太稀、对应差 |
| SDDiff | 纯化后的占用解码为点 | 同一表示 + IDR / decoder |

对照「只生成强度图」的 RadarHD / RadarDiff：见 [sddr.md](sddr.md)。鬼影见 [multipath-ghosting.md](multipath-ghosting.md)。
