# DriveDreamer-2

来源：Zhao et al., *DriveDreamer-2: LLM-Enhanced World Models for Diverse Driving Video Generation* (AAAI 2025, arXiv:2403.06845)；Feng 综述 (arXiv:2501.11260v4) Table 1 放在图像轨 Dreamer 系列  
https://arxiv.org/abs/2403.06845

## 一句话

在 DriveDreamer 上加一个微调过的 **LLM**：用户用一句话描述场景，LLM 生成 agent 轨迹，扩散模型再据此生成 HDMap，最后用 UniMVM 出多视角驾驶视频；主打「用户自定义 + 多样性」，仍属图像轨生成。

## 做什么

输入只要**文本提示**（不再强依赖数据集给的 3D 框/地图）。流程（原文 Figure 2）：

1. **LLM 生成轨迹**：用 18 个函数（steering、cut_in、U-turn…）构造 Text→Python-Script 对，微调 GPT-3.5，把「一辆车突然加塞」这类话变成 agent 轨迹数组。
2. **HDMap 生成**：扩散模型以前一步轨迹为条件，生成与轨迹不冲突的道路结构（车道边界/分隔线/人行道）。
3. **UniMVM**（Unified Multi-view Video Model）：把多视角拼成一张宽图统一生成，兼顾视角内和跨视角一致性，不像 Drive-WM 那样分视角生成。

输出：多视角驾驶视频。落在综述四条轨的 **Image**。

## 综述怎么归类

Feng Table 1：**LLM + Diffusion Model**；条件 Text + HDMap + Box；输出 2D Image；数据 **nuScenes**。§3.1 一句：加 LLM 提示机制增强交互性和多样性。§4.3 数据生成表：从文本生成用户自定义视频，作者讨论可加进 3D 检测训练集。

原文数字（Abstract，相对提升，不是绝对 FID）：FID 11.2、FVD 55.7，相对此前最佳约 **+30% / +50%**；下游检测/跟踪相对约 **+4% / +8%**。不要和 Feng 规划表 L2 混读。

## 和相邻概念

| 概念 | 差别 |
|------|------|
| [DriveDreamer](drivedreamer.md) | 初代吃结构条件 + 动作，出视频和开环动作；本条把条件换成文本，靠 LLM 造结构 |
| [ReconDreamer](recondreamer.md) | 同系列但任务不同：新轨迹渲染修复，服务闭环；本条是文本到多视角视频生成 |
| [图像/鸟瞰图 BEV/占用/点云](image-bev-og-pc.md) | 本条仍属图像轨；HDMap 生成那步是在 BEV 平面上做的条件图，不是 BEV 预报主轨 |
| [扩散模型](diffusion-model.md) | HDMap 生成和视频生成都用扩散；LLM 负责把文本变成结构条件 |
| [长尾场景](long-tail-scenario.md) | 卖点之一是文本可点「突然加塞」「行人横穿」等稀有情形 |
| [开环回放](open-loop-replay.md) | 综述把这类生成视频当数据增强，仍不响应在线控制 |

## 注意

「first world model to generate customized driving videos」是原文自称。LLM 在这里是**条件翻译器**（文本→轨迹脚本），不是当规划器或世界模型本体；别和 DrivingGPT 那种把驾驶当 next-token 的 LLM 规划器混。
