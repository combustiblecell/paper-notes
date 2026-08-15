# Figure 2 六模块架构

来源：LeCun 2022 立场文 §3，Figure 2–4  
https://openreview.net/forum?id=BZ5a1r-kVsf

## 一句话

LeCun 提出的**可微分自主智能体**蓝图：六个模块全部可反传梯度，World Model 做前向预测，Actor 在 Mode-2 下做 MPC 式规划，行为由不可变的 Intrinsic Cost 驱动。

## 六模块

| 模块 | 功能 | 可训练？ |
|------|------|---------|
| **Configurator** | 执行控制：按任务调制其他模块参数与注意力 | ✓ |
| **Perception** | 传感器 → 分层世界状态 $s[0]$ | ✓ |
| **World Model** | 补全缺失 + 预测未来（含动作条件） | ✓ |
| **Cost** | 标量 energy = Intrinsic Cost + Critic | IC **不可**训练 |
| **Short-term Memory** | 存 $(\tau, s_\tau, IC(s_\tau))$，Key-Value 联想记忆 | 存储 |
| **Actor** | Policy（Mode-1）+ Action Optimizer（Mode-2） | ✓ |

原文：“All modules in this model are assumed to be ‘differentiable’… The configurator module takes inputs from all other modules and configures them to perform the task at hand.”（Figure 2 说明，第6页）

## 两种行为模式

| | Mode-1 (System 1) | Mode-2 (System 2) |
|--|-------------------|-------------------|
| 路径 | Perception → Policy → Action | 提动作序列 → WM rollout → Cost → 优化 |
| 规划 | 反应式，无 deliberate planning | MPC + receding horizon |
| 梯度 | 无法通过真实世界反传 | Cost 梯度可穿过 World Model |

详见 [mode-2-planning.md](mode-2-planning.md)。

## 设计要点

- **单一可配置 World Model 引擎**：多任务共享，Configurator 切换（§2.2 假设）
- **Intrinsic Cost 不可变**：“The IC must be immutable and not subject to learning”（§3.2，第13页）——防行为漂移
- **Critic 可训练**：从 short-term memory 检索过去状态与未来 intrinsic cost 做预测

## 和相邻概念的对比

| | 传统 RL 智能体 | Figure 2 架构 |
|--|---------------|--------------|
| 世界模型 | 可选、常与 policy 割裂 | 核心模块，与 Cost/Actor 可微联通 |
| 奖励 | 外部 reward | Intrinsic Cost（硬编码）+ 可配置 Critic |
| 规划 | 多在真实环境试错 | Mode-2 在模型内 imagination |
| 任务切换 | 常需重训 | Configurator 动态配置 |

World Model 的具体实现见 [jepa.md](jepa.md)；前向预测机制见 [forward-model.md](forward-model.md)。
