# 非生成式层次化 JEPA

来源：Yann LeCun, *A Path Towards Autonomous Machine Intelligence* (2022), OpenReview  
https://openreview.net/forum?id=BZ5a1r-kVsf

## 一句话

不预测未来的像素/原始信号，只在**抽象表征空间**里预测世界会怎样变；多层叠起来就能做短时细节预测和长时抽象预测。

## JEPA 是什么

**JEPA** = Joint Embedding Predictive Architecture（联合嵌入预测架构）。

- 两路编码器：$x \rightarrow s_x$，$y \rightarrow s_y$
- 预测器（可带潜变量 $z$）：用 $s_x$（和 $z$）去对 $s_y$
- 能量就是表征空间里的预测误差：$E = D(s_y, \mathrm{Pred}(s_x, z))$

原文：JEPA “is not generative… It merely capture the dependencies between $x$ and $y$ without explicitly generating predictions of $y$.”（§4.4）

## 为什么叫「非生成式」

| 生成式 | JEPA |
|--------|------|
| 直接生成下一帧像素、波形、token | 只预测表征 $s_y$ |
| 必须交代每个细节（树叶、水波） | 编码器可以丢掉难预测、对规划无用的细节 |
| 视频长期预测几乎不可能准 | 预测「车大概走哪条路」即可 |

多模态未来（车在路口左转或右转）靠两件事表达：

1. **编码器不变性**：多种 $y$ 映到同一个 $s_y$
2. **潜变量 $z$**：扫过集合 $Z$ 得到一组合理的 $\tilde{s}_y$

## 层次化（H-JEPA）

把多层 JEPA 叠起来（文中 Figure 15）：

- **JEPA-1（低层）**：细节多，短时预测（下一秒方向盘、轨迹）
- **JEPA-2（高层）**：更抽象，长时预测（大概几点到目的地）

不可预测的细节被高层编码器丢掉。高层动作还可以当作低层的**子目标**，用来做层次规划。

### JEPA-1 → JEPA-2 层级堆叠

观测序列 $x_0, x_1, x_2, \ldots$ 经 JEPA-1 提取低层表征并做短期预测；JEPA-2 以 JEPA-1 表征为输入，做长期、更抽象预测。

原文（Figure 15 说明，第29页）：

> “JEPA-1 extracts low-level representations and performs short-term predictions. JEPA-2 takes the representations extracted by JEPA-1 as inputs and extracts higher-level representations with which longer-term predictions can be performed.”

### Temporal pooling 粗化表征

层间用 **temporal pooling**（及可选卷积模块）做时间下采样/聚合：

- 时间分辨率降低 → 可预测更远 future
- 表征更抽象 → 丢弃长期不可预测细节

可 envision “architectures of this type with many levels”（§4.6，第30页）。

### 训练：level-wise vs global

原文（§4.6，第30页）：

> “Training can be performed level-wise or globally, using any non-contrastive method for JEPA.”

| 方式 | 做法 |
|------|------|
| **Level-wise** | 先训 JEPA-1，再训 JEPA-2（下层可冻结） |
| **Global** | 所有层联合端到端训练 |

非对比方法（VICReg 等，见 [vicreg.md](vicreg.md)）两层均适用。

### 与 Wayne & Abbott 的分工

Wayne & Abbott 用多层 forward model 指定 intermediate goals，但中间动作词汇需预定义；H-JEPA 希望中间 plan 表征也**可学习**。详见 [wayne-abbott-hierarchical-forward.md](wayne-abbott-hierarchical-forward.md)。
