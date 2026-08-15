# VAE / GAN / VQ-VAE（生成式视频/世界模型）

来源：LeCun 2022 立场文 §4.3、§7.1；Figure 10(b)  
https://openreview.net/forum?id=BZ5a1r-kVsf

## 一句话

在**观测空间**（像素/帧）用潜变量建模多模态未来 $p(y|x)$ 的三类主流生成式方法；LeCun 将其作为 JEPA 的对照——能生成画面，但难学抽象、浪费容量于不可预测细节。

## 要点

| 方法 | 机制 | 多模态 |
|------|------|--------|
| **VAE** | 编码 → 高斯 latent → 解码重建；ELBO | latent 采样不同 $y$ |
| **GAN** | Generator vs Discriminator | 随机噪声 → 不同帧 |
| **VQ-VAE** | latent 离散化（codebook） | 不同 code → 不同输出 |

文中 §7.1 举例：Mathieu, Luc, Babaeizadeh, Denton 等用于视频预测；Henaff, Mercat 用于驾驶轨迹；Oh, Finn 等用于机器人控制。  
原文：“Unlike the proposed JEPA, these models are generative.”（§7.1，第40页）

## LeCun 的批评（为何转向 JEPA）

1. **无法消除无关细节**——只能把细节推进 latent，不能产生抽象不变表征（§4.6）
2. **长期像素预测不现实**：“it is essentially impossible to predict every pixel value of every future frame”（§4.5，第27页）
3. **latent 容量过大时 collapse**（Figure 10(b)）
4. 早期无 latent 的视频预测 → 模糊（Lerer et al., 2016，§7.1 提及）

## 和相邻概念的对比

| | VAE/GAN/VQ-VAE | MAE | JEPA |
|--|----------------|-----|------|
| 预测空间 | 像素 $y$ | 被 mask 像素 | 嵌入 $s_y$ |
| 是否生成 | ✓ | ✓（decoder） | ✗ |
| 多模态 | latent / 对抗 | 通常单峰重建 | 不变性 + $z$ |
| LeCun 态度 | 对照组 | 对比式重建 | 主推 |

更一般的潜变量框架见 [latent-variable-generative-model.md](latent-variable-generative-model.md)。
