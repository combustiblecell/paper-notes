# 非生成式层次化 JEPA

来源：Yann LeCun, *A Path Towards Autonomous Machine Intelligence* (2022), OpenReview  
https://openreview.net/forum?id=BZ5a1r-kVsf

## 一句话

不预测未来的像素/原始信号，只在**抽象表征空间**里预测世界会怎样变；多层叠起来就能做短时细节预测和长时抽象预测。

## JEPA 是什么

**JEPA** = Joint Embedding Predictive Architecture（联合嵌入预测架构）。

- 两路编码器：\(x \rightarrow s_x\)，\(y \rightarrow s_y\)
- 预测器（可带潜变量 \(z\)）：用 \(s_x\)（和 \(z\)）去对 \(s_y\)
- 能量就是表征空间里的预测误差：\(E = D(s_y, \mathrm{Pred}(s_x, z))\)

原文：JEPA “is not generative… It merely capture the dependencies between \(x\) and \(y\) without explicitly generating predictions of \(y\).”（§4.4）

## 为什么叫「非生成式」

| 生成式 | JEPA |
|--------|------|
| 直接生成下一帧像素、波形、token | 只预测表征 \(s_y\) |
| 必须交代每个细节（树叶、水波） | 编码器可以丢掉难预测、对规划无用的细节 |
| 视频长期预测几乎不可能准 | 预测「车大概走哪条路」即可 |

多模态未来（车在路口左转或右转）靠两件事表达：

1. **编码器不变性**：多种 \(y\) 映到同一个 \(s_y\)
2. **潜变量 \(z\)**：扫过集合 \(Z\) 得到一组合理的 \(\tilde{s}_y\)

## 层次化（H-JEPA）

把多层 JEPA 叠起来（文中 Figure 15）：

- **JEPA-1（低层）**：细节多，短时预测（下一秒方向盘、轨迹）
- **JEPA-2（高层）**：更抽象，长时预测（大概几点到目的地）

不可预测的细节被高层编码器丢掉。高层动作还可以当作低层的**子目标**，用来做层次规划。
