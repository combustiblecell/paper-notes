# 通用世界模型 taxonomy

来源：Feng et al. (arXiv:2501.11260v4) §1 对既有综述的划分；Ding et al., *Understanding World or Predicting Future?* (arXiv:2411.14499)；Zhu et al., *Is Sora a World Simulator?* (arXiv:2405.03520)

## 一句话

「通用」世界模型综述不把驾驶当唯一场景，而按**能力**或**应用域**切刀；Feng 认为它们覆盖面宽，但对车上「预测怎么跟规划咬合」切得粗。

## Feng 怎么给综述分档（§1）

| 档 | 代表 | Feng 的批评 |
|----|------|----------------|
| 通用 WM | Zhu et al. 2024；Ding et al. 2024b | 驾驶只是应用之一 |
| 驾驶 WM | Guan et al. 2024；Fu et al. 2024b | 分类粗，常只谈仿真，缺少规划–预测交互 |

Feng 自己的刀是驾驶专用三层（见 L10：[图像/鸟瞰图 BEV/占用/点云](image-bev-og-pc.md)、[学习式与规则式](learning-vs-rule-based.md)、[开环](open-loop-replay.md)→[可控闭环](controllable-closed-loop.md)），不要和下面两条通用刀混成一张表。

## Ding：两功能（理解 vs 预测）

原文共识：世界模型要 **understand the dynamics of the world and predict future scenarios**。分类轴是两条主功能，不是传感器种类。

| 支 | 做什么 | 文献锚点（文中） |
|----|--------|------------------|
| **内部表征 / 理解当下** | 把外界压成隐变量，支撑决策（MBRL 的转移 $`M`$、LLM 里的世界知识） | Ha & Schmidhuber 2018；LeCun JEPA 2022 |
| **预测未来 / 模拟** | 生成看起来像未来物理世界的视频，再走到空间表征与具身环境 | Sora 等视频世界模型 |

应用域另切三块：自动驾驶、机器人、社会模拟（social simulacra）。驾驶被写成既要实时感知、又要预报复杂演变。

Ding 对 Sora：常被叫 world simulator，但 **causal reasoning** 弱（被动生成、不能按动作改进程），物理定律也不稳定复现——所以「像世界模型」≠「完整世界模型」。

## Zhu：三应用域

Figure 1 把主流发展收成三条，视频生成是后两条的技术底座：

1. **视频生成 WM**：条件生成 / 编辑，用来理解并模拟世界（媒体、艺术）
2. **自动驾驶 WM**：用生成造驾驶场景、从视频学要素与策略，辅助端到端
3. **自主智能体 WM**：游戏 / 机器人等动态环境里的交互与策略（Dreamer、UniPi、UniSim 等）

和 Ding 的差别：Zhu 按**用在哪**切；Ding 按**理解还是预测**切。驾驶在 Zhu 里是主轴之一，在 Ding 里只是应用章。

## 和本仓库相邻概念

| 概念 | 差别 |
|------|------|
| [形式化](world-model-formalization.md) / L10 | 驾驶专用：$`w(I,P)\to(z,\tau)`$ 再拆生成 / 规划 / 交互 |
| [前向模型](forward-model.md) / [JEPA](jepa.md) | Ding 理解支的核心；LeCun 还要求用表征去**设想未来**再决策 |
| [潜变量生成模型](latent-variable-generative-model.md) | Ding/Zhu 预测支、Zhu 视频生成支；Sora 落在这边 |
| [可控闭环仿真](controllable-closed-loop.md) | 通用综述里「交互式视频 / 具身」的驾驶落点；开环视频生成过不了动作因果 |

## 注意

不要把 Guan 的驾驶初综述写成通用 taxonomy。不要给 Ding/Zhu 编他们没写的第三、第四条主轴。
