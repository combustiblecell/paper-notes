# InfoNCE / SimCLR（对比学习）

来源：LeCun 2022 立场文 §4.3，Eq. 6–9；SimCLR (Chen et al., 2020)  
https://openreview.net/forum?id=BZ5a1r-kVsf

## 一句话

用**正样本能量↓、负样本能量↑**训练嵌入：batch 内其他样本当负例；LeCun 认为高维表征空间下负样本需求随维度指数增长，故 JEPA 改用非对比正则（VICReg）。

## InfoNCE 损失（文中 Eq. 9）

$$
\mathcal{L} = F(x,y) + \log\left[e^{-F(x,y)} + \sum_{k=1}^{K} e^{-F(x,\hat{y}_k)}\right]
$$

## SimCLR 思路

- 同一图像两个 augmentation → 正样本对
- batch 内其余样本 → 负样本
- 拉近正样本 embedding，推远负样本

文中还归类为 contrastive 的方法：DrLIM, PIRL, MoCo, SimCLR, CPT, CPC, GAN, Denoising AE / **MAE**（§4.3，第21页）。

## LeCun 的批评

原文（§4.3，第22页）：

> “a disadvantage of contrastive methods is that the number of contrastive samples necessary to make an energy surface adopt a good shape may grow exponentially with the dimension of $y$ space.”

| | 对比（SimCLR/InfoNCE） | 非对比（VICReg） |
|--|------------------------|-----------------|
| 负样本 | 需要大量 $\hat{y}$ | 不需要 |
| 对比维度 | **样本**维度（batch 内） | **分量**维度（协方差） |
| 维数灾难 | 可能有 | LeCun 认为更有希望避开 |

## 和相邻概念的对比

- **VICReg**：JEPA 推荐的非对比替代，见 [vicreg.md](vicreg.md)
- **MAE**：LeCun 也归为 contrastive（corrupt $y$ 当负例），见 [mae.md](mae.md)
- **JEPA**：可用 contrastive 训练，但 “doing so runs into the curse of dimensionality”（§4.5，第25页）
