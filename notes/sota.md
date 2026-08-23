# SOTA（本文评测语境）

来源：Wang et al., *SDDiff*, arXiv:2506.16936v1，Abstract、§4.3、§5  
https://arxiv.org/abs/2506.16936

## 一句话

这篇里的「state of the art」不是泛称，而是**作者选定的 PCE / EVE 基线里最好的那一档**；数字都要回到对应表，不要和别的雷达论文混用。

## 本文对照的基线

**PCE**（§4.3）：OS-CFAR（1988）；生成式 RPDNet（2022）、RadarHD（2023）、RadarDiff（2024）；以及作者改的 Modified 3D-Diff（因为「no generative models exist for scene-level 3D PCE」）。RadarHD / RadarDiff 标了 $`\dagger`$（2D）。

**EVE**（§4.3）：ICP（1992）、RANSAC（Kellner 2013）、RadarEVE（Pang et al., 2024）。文中写当时没有同时从 ADC 做稠密 3D PCE + 3D EVE 的生成模型（§2.3）。

## 作者声称相对 SOTA 的数字

| 声称 | 正文落点 | 注意 |
|------|----------|------|
| EVE 高 59% | §5.2 + Table 3 室外 0.11 vs RadarEVE 0.27 | 室内是约 30%，不是 59% |
| VPR +30%、SRL +33% | §5.1，第6页 | 未写清对哪一条 PCE 基线、哪个阈值 |
| 有效生成密度 $`4\times`$ | 仅 Abstract | 表内 EGD=1.17；**4× 算法未找到（Not found）** |

公开代码与自采数据 URL：**未找到（Not found）**。仅有 `we will make our self-collected dataset publicly available`（第2页）。

## 和相邻概念的对比

- [PCE](pce.md) / [EVE](eve.md) 是任务；SOTA 是**比较尺子**。
- [室外 EVE](outdoor-eve.md) 是 59% 那条尺子实际量的场景。
- 和仓库里 JEPA 线的「主推 / 对照」不同：这里 SOTA 是雷达感知实验表，不是 LeCun 立场文里的训练范式。
