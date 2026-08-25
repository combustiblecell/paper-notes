# DriveDreamer

来源：Wang et al., *DriveDreamer: Towards Real-World-Drive World Models for Autonomous Driving* (ECCV 2024, arXiv:2309.09777)；Feng 综述 (arXiv:2501.11260v4) 把它放在 §3.1 图像轨、§3.3 开环生成例  
https://arxiv.org/abs/2309.09777

## 一句话

用**真车 nuScenes 视频**训的扩散世界模型：按 HD 地图、3D 框、文本和动作条件生成驾驶视频，并预报未来动作；作者自称相对游戏/仿真世界模型，这是实路数据上的先行者。

## 做什么

输入参考帧、HDMap、3D box、文本（天气/时段）、历史动作；输出未来透视视频，以及未来驾驶动作/轨迹。落在综述四条轨的 **Image**（2D 图像/视频），不是 BEV/占用/点云主输出。

两阶段训练（原文 Figure 2）：

1. **Auto-DM** 先吃结构化交通条件（地图、框）学生成单帧再学视频，缩小像素搜索空间。
2. 再用动作去更新未来结构条件，做视频预测，并出未来策略。

后续同系列（综述表，不是本条主体）：DriveDreamer-2 加 LLM 提示；DriveDreamer4D 走向 4D 视频/4DGS。新轨迹重建见 [ReconDreamer](recondreamer.md)。

## 综述怎么归类

Feng Table 1：扩散；条件 Text + Image + HDMap + Box + Actions；输出 2D Image + Actions；数据 nuScenes。

§3.1 把 Dreamer 游戏/机器人世界模型接到车上，并写 DriveDreamer **仍限 2D、时空一致性不足**——这是综述判断，原文自己加了时间注意力。

§3.3 与 DriveGAN、MagicDrive 并列：**偏外观的开环生成**，重放预采样未来，**不响应在线控制**，动作与下一观测的因果链是断的。原文则强调第二阶段可用动作条件生成不同未来视频，并在 nuScenes 上做**开环**规划评测。两边不矛盾：能按给定动作序列生成视频 ≠ 仿真器里动作会改下一帧传感器。

综述 Table 9（转引各论文）：相机、辅助监督 Map & Box & Motion，平均 L2 **0.29**、碰撞 **0.15**；1s/2s/3s 分项未列出。原文称开环规划平均 $`L_2`$ 为 0.29 m。不要和 UniAD+DriveWorld 的 0.69/0.19 横比难度（监督和设定不同）。

## 和相邻概念

| 概念 | 差别 |
|------|------|
| [图像/鸟瞰图 BEV/占用/点云](image-bev-og-pc.md) | 本条是图像轨上的一个方法，不是四条轨本身 |
| [扩散模型](diffusion-model.md) | Auto-DM 是驾驶条件扩散；本条还带结构条件和动作头 |
| [开环回放](open-loop-replay.md) | 综述把 DriveDreamer 放进开环生成例 |
| [可控闭环仿真](controllable-closed-loop.md) | 要动作改下一观测、可注入规则/长尾；DriveDreamer 原评测是开环 |
| [长尾场景](long-tail-scenario.md) | 原文动机含用生成视频补感知训练；综述开环档仍难在线注入稀有事件 |
| Ha/Hafner Dreamer | 名字同源；那些多在游戏/仿真，本条强调实路视频 |

## 注意

作者「first real-world driving world model」是原文自称。规划数字来自开环 nuScenes，综述又把它放进开环体制——读表时当生成+开环规划，不当闭环仿真 SOTA。
