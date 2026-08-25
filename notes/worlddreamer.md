# WorldDreamer

来源：Wang et al., *WorldDreamer: Towards General World Models for Video Generation via Predicting Masked Tokens* (arXiv:2401.09985, 2024)；Feng 综述 (arXiv:2501.11260v4) Table 1 归为 **LLM** 类  
https://arxiv.org/abs/2401.09985 ｜ https://world-dreamer.github.io

## 一句话

把世界建模当成**无监督视觉序列建模**：用 VQGAN 把图像/视频切成离散 token，随机 mask 一部分，再用 Transformer（STPT）预测被 mask 的 token，靠文本+动作做跨注意力提示；目标是「通用世界」视频生成，驾驶只是其中一个场景。

## 做什么

- **视觉分词**：VQGAN 把图像/视频编码成离散 token。
- **掩码预测**：随机 mask 一部分 token，用未 mask 的去预测它们——借鉴 LLM 的 masked-token 思路，而不是扩散去噪。
- **STPT**（Spatial Temporal Patchwise Transformer）：注意力只落在时空窗口内的局部 patch，便于学视觉动态、加速收敛。
- **多模态提示**：文本和动作各自编码成 embedding，经 cross-attention 注入，作为交互条件。
- **训练数据**：Visual-Text-Action 三元组；监督只有「预测被 mask 的视觉 token」，无额外标签；也支持无文本/无动作训练。
- **推理任务**：text-to-video、image-to-video、video stylization、video inpainting、action-to-video（给驾驶首帧 + 未来动作命令，预测后续帧）。

输出：2D 图像/视频。落在综述四条轨的 **Image**。

## 综述怎么归类

Feng Table 1：**LLM**（非 Diffusion）；条件 Image + Video + Text + Action；输出 2D Image；数据 **nuScenes**。和 DriveDreamer 系列同作者群，但路线不同——DriveDreamer 走扩散，WorldDreamer 走 Transformer 掩码预测。

原文卖点（Abstract/Intro，相对说法，非绝对指标）：相比扩散法**约 3× 更快**（并行解码只需少量迭代），可复用 LLM 基础设施和优化经验；自称「first general world model for video generation」。不要把这条「general world」和 Feng 综述里的「通用 WM taxonomy」（Ding/Zhu 分类）混——那是更高层的 taxonomy 概念，这里是模型自称的通用性。

## 和相邻概念

| 概念 | 差别 |
|------|------|
| [DriveDreamer](drivedreamer.md) | 同作者群，但走扩散 + 结构条件，专注驾驶；本条走 Transformer 掩码预测，主打通用世界 |
| [DriveDreamer-2](drivedreamer-2.md) | 在 DriveDreamer 上加 LLM 翻译文本→轨迹；本条的 LLM 思路是直接当序列建模骨干，不是条件翻译器 |
| [扩散模型](diffusion-model.md) | 本条明确对标扩散：并行解码、复用 LLM 栈，声称更快 |
| [VAE/GAN/VQ-VAE](vae-gan-vqvae.md) | 用 VQGAN 做视觉分词，是 VQ-VAE 一族在视频生成里的应用 |
| [通用 WM taxonomy](general-wm-taxonomy.md) | 那是综述层面的分类框架；本条是具体模型，别把「general」混读 |
| [图像/鸟瞰图 BEV/占用/点云](image-bev-og-pc.md) | 本条属图像轨；动作条件下的 image-to-video 是驾驶场景里的用法 |

## 注意

「first general world model」是原文自称，不是综述定性。Feng 综述只把它列为 LLM 类图像轨一例，没单列「通用世界」赛道。掩码预测 ≠ 扩散去噪：前者是离散 token 上的 LLM 式预测，后者是连续潜空间逐步去噪。
