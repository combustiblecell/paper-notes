# 可控闭环仿真（Controllable closed-loop）

来源：Feng et al., *A Survey of World Models for Autonomous Driving* (arXiv:2501.11260v4) §3.3、Figure 3(c)  
https://arxiv.org/abs/2501.11260v4

## 一句话

仿真器（或潜空间世界模型）**跟着自车动作改下一观测**，并且允许编辑 4D 世界、改规则、注入稀有事件，用来做可测试的交互评测。

## 综述里怎么说

Figure 3(c)：在不可控闭环之上，加上 editable 4D worlds、occupancy control 以及 feedback/backward signals，让驾驶智能体与可充分测试的仿真器安全交互。

演进：脚本交通引擎 → 带传感器真实感的游戏引擎（CARLA 等）→ 神经/混合平台（DriveArena、DrivingSphere 等）。也可把可控闭环做在**潜空间**里（如 LAW 的 plan-conditioned latent world model）。

小结（§3.3 Summary）：闭环分数应补充或取代开环指标；生成式仿真可按需合成 corner case；规划与预测应用统一损失绑在一起。

## 和相邻概念

| 概念 | 差别 |
|------|------|
| [开环回放](open-loop-replay.md) | 开环不响应动作；本条要因果闭环 |
| [不可控闭环](open-loop-replay.md) | 会按动作 rollout，但不能改交规/注入长尾（写在开环条的中间档） |
| [Mode-2 规划](mode-2-planning.md) | 闭环仿真是 Mode-2「在模型里试动作」的驾驶版沙盒 |
| [长尾场景](long-tail-scenario.md) | 可控闭环的卖点之一就是按需注入稀有危险 |
| [图像/BEV/占用/点云](image-bev-og-pc.md) | 闭环里下一帧可以是图像、占用或点云，表示仍是那四条轨 |
