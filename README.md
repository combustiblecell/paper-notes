# paper-notes

研究笔记仓库。在 Cursor 对话里输入 `@notes` 可把 `notes/` 当作上下文。

**概念关系总览（推荐先看）**：[notes/overview.md](notes/overview.md)

## 当前笔记

- [概念总览 · 关系图](notes/overview.md)
- [非生成式层次化 JEPA](notes/jepa.md)
- [前向模型](notes/forward-model.md)
- [Figure 2 六模块架构](notes/six-module-architecture.md)
- [VAE / GAN / VQ-VAE](notes/vae-gan-vqvae.md)
- [扩散模型](notes/diffusion-model.md)
- [MAE](notes/mae.md)
- [InfoNCE / SimCLR（对比学习）](notes/contrastive-learning.md)
- [Wayne & Abbott 多层前向模型](notes/wayne-abbott-hierarchical-forward.md)
- [多模态（预测不确定性）](notes/multimodality.md)
- [非对比自监督（VICReg）](notes/vicreg.md)
- [Mode-2 规划](notes/mode-2-planning.md)
- [潜变量生成模型](notes/latent-variable-generative-model.md)
- [雷达 ADC](notes/radar-adc.md)
- [SDDR（占用 + 多普勒）](notes/sddr.md)
- [定向扩散 + 迭代多普勒精炼](notes/directional-diffusion-idr.md)
- [PCE 点云提取](notes/pce.md)
- [EVE 自车速度估计](notes/eve.md)
- [室外 EVE](notes/outdoor-eve.md)
- [SOTA（本文评测）](notes/sota.md)
- [多径鬼影](notes/multipath-ghosting.md)
- [异构传感器](notes/heterogeneous-sensors.md)
- [多传感器压成潜状态](notes/multi-sensor-latent-state.md)
- [长尾场景](notes/long-tail-scenario.md)
- [通用 WM taxonomy](notes/general-wm-taxonomy.md)
- [形式化（式 1）](notes/world-model-formalization.md)
- [图像 / 鸟瞰图 BEV / 占用 / 点云](notes/image-bev-og-pc.md)
- [DriveDreamer](notes/drivedreamer.md)
- [DriveDreamer-2](notes/drivedreamer-2.md)
- [ReconDreamer](notes/recondreamer.md)
- [WorldDreamer](notes/worlddreamer.md)
- [Diffusion-based Image Generation](notes/diffusion-based-image-generation.md)
- [Benchmarks](notes/benchmarks.md)
- [学习式与规则式规划](notes/learning-vs-rule-based.md)
- [开环回放](notes/open-loop-replay.md)
- [可控闭环仿真](notes/controllable-closed-loop.md)

## 论文摘要

- [SDDiff（空间-多普勒扩散）](summary/wang-2025-sddiff.md)
- [世界模型与自动驾驶综述](summary/feng-2025-survey-world-models-ad.md)

## 工作流

```bash
# 编辑 notes/ 后
git add .
git commit -m "Add [concept] notes"
git push origin main
```
