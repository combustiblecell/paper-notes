# 前向模型（Forward Model）

来源：LeCun 2022 立场文 §2.1、§3、§4；心理学 Craik (1943)；最优控制 Bryson & Ho (1969)；RL Sutton Dyna (1991)  
https://openreview.net/forum?id=BZ5a1r-kVsf

## 一句话

给定当前状态与动作，预测**下一时刻世界会怎样变**；在 LeCun 架构里由 World Model 模块承担，JEPA 路线下在**表征空间**而非像素空间做预测。

## 要点

- 形式：$`\hat{s}_{t+1} = \mathrm{Pred}(s_t, a_t)`$
- 在 Figure 2 架构中，World Model 角色 twofold：（1）补全感知缺失信息；（2）预测自然演化或动作条件下的未来状态（§3）
- Mode-2 规划时递归 rollout：$`s[t+1] = \mathrm{Pred}(s[t], a[t])`$，再对 $`\sum_t C(s[t])`$ 做能量最小化（Figure 4）
- 原文把 World Model 称为 “a kind of simulator of the relevant aspects of world”（§3）

## 历史脉络（文中 §7.1 提及）

| 脉络 | 代表 |
|------|------|
| 心理学 | Craik (1943) 内部世界模型 |
| 最优控制 | Model-Predictive Control (Bryson & Ho, 1969) |
| RL | Sutton Dyna (1991)；Ha & Schmidhuber World Models (2018) |
| LeCun 2022 | JEPA World Model：表征空间预测 |

## 和相邻概念的对比

| | 经典前向模型 | JEPA 前向模型 |
|--|-------------|--------------|
| 预测对象 | 像素 / 低维状态 | 嵌入 $`s_y`$ |
| 不可预测细节 | 常硬要重建 | 编码器可丢弃 |
| 多模态 | 需 GAN/VAE 等 | encoder 不变性 + 潜变量 $`z`$ |
| 用途 | MPC / Dyna | Mode-2 分层规划（见 [mode-2-planning.md](mode-2-planning.md)） |

与 **Wayne & Abbott 多层前向模型** 的差别：后者每层显式建模低层控制器输出；H-JEPA 在**可学习表征**上堆叠（见 [wayne-abbott-hierarchical-forward.md](wayne-abbott-hierarchical-forward.md)）。
