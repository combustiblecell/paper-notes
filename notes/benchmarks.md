# benchmarks

来源：Feng et al. 综述 (arXiv:2501.11260v4) §6 Performance Comparison（§6.1 平台、§6.2–6.5 四类任务表）  
https://arxiv.org/abs/2501.11260

## 一句话

综述 §6 把「世界模型评测」拆成**五个评测平台 + 四类任务表**：平台给数据，任务表给指标和横评，是这篇综述唯一集中给定量结果的地方。

## 评测平台（§6.1）

| 平台 | 来源 | 关键属性 |
|------|------|----------|
| **CarlaSC** | CARLA 合成 (Wilson 2022) | 4D occupancy，`$128\!\times\!128\!\times\!8$`，自车周围 `$25.6m\!\times\!25.6m\!\times\!3m$` |
| **nuScenes** | Caesar 2020 | 1000 场景（700/150/150），6 路 RGB（360°）+ 32 线 LiDAR |
| **Occ3D-nuScenes** | Tian 2024，基于 nuScenes | 700 训练 / 150 验证序列，每序列 ~40 帧 @ 2 Hz |
| **Occ3D-Waymo** | Tian 2024，基于 Waymo (Sun 2020) | 798 训练 / 202 验证，每序列 ~200 帧 @ 10 Hz，17 类 |
| **OpenScene** | Zhang 2024e，来自 nuPlan | 120+ 小时、四城、`$600{,}000{+}$` 帧；8 相机 + 5 LiDAR；mini: 5392 训 / 8729 验 |

## 四类任务与指标（§6.2–6.5）

| 任务 | 表 | 平台 | 指标（方向） |
|------|----|------|-------------|
| **4D 场景生成** | Table 6 | CarlaSC / Occ3D-Waymo | IS`$\uparrow$`、FID`$\downarrow$`、KID`$\downarrow$`、Precision`$\uparrow$`、Recall`$\uparrow$`，2D 和 3D 空间各测一遍 |
| **点云预报** | Table 7 | OpenScene-mini val | Chamfer Distance (CD, m²)`$\downarrow$`，按 0.5/1/1.5/2/2.5/3 s 多时域 |
| **4D 占用预报** | Table 8 | Occ3D-nuScenes | mIoU`$\uparrow$`、IoU`$\uparrow$`，1/2/3 s 三时域 + Avg；分 3D-Occ 输入和 Camera 输入两组 |
| **运动规划** | Table 9 | nuScenes | L2 误差 (m)`$\downarrow$`、碰撞率 (%)`$\downarrow$`，1/2/3 s + Avg；分 LiDAR / Camera / 3D-Occ 三类输入 |

## 综述给出的代表性结论

- **4D 场景生成**（Table 6）：DynamicCity vs OccSora，在 CarlaSC 和 Occ3D-Waymo 上、2D/3D 双空间里 IS/FID 等「感知质量 + 保真-多样性折中」都更好。
- **点云预报**（Table 7）：DFIT-OccWorld-O 平均 CD 0.70、V 变体 0.76，全面优于 ViDAR 的 1.58；随预报时长拉长差距扩大。趋势：从 range-image CNN/LSTM 转向 token 化扩散 + 图像先验 + 物理约束。
- **4D 占用预报**（Table 8）：3D-Occ 输入组里 I2-World-O 平均 mIoU 39.73、T3Former-O 36.09 领先；纯相机 T3Former-F 仍有竞争力。趋势：token/扩散骨干 + 语言或轨迹 prompt + 纯相机降 LiDAR 成本。
- **运动规划**（Table 9）：相机端到端加富监督明显有用——UniAD+DriveWorld 相对 UniAD 平均 L2 降 ~33%、碰撞率降 ~39%（平均 L2 0.69、碰撞 0.19）；3D-Occ 输入组 T3Former-O 1.00 m / 0.30% 拿到最佳折中，3 s 碰撞相对 OccWorld 降 ~62%；FSDrive 0.28/0.10 最好但用了 ego status 特权监督，不完全可比。

## 和相邻概念

| 概念 | 差别 |
|------|------|
| [图像/鸟瞰图 BEV/占用/点云](image-bev-og-pc.md) | 那篇讲四条**输出轨**的方法范式；本条是这些范式在 §6 里被定量评测的舞台 |
| [Diffusion-based Image Generation](diffusion-based-image-generation.md) | 图像轨扩散支线的方法谱系；其代表方法在 §6 各表里被评测 |
| [DriveDreamer](drivedreamer.md) / [DriveDreamer-2](drivedreamer-2.md) | Table 9 里 DriveDreamer 给 3 s 碰撞 0.15（L2 列「-」未报）；DriveDreamer-2 的 FID/FVD 是其原文相对提升数，不在 §6 表里 |
| [ReconDreamer](recondreamer.md) | 服务闭环重建，§6 没单列其指标 |
| [开环回放](open-loop-replay.md) / [可控闭环仿真](controllable-closed-loop.md) | §6 表大多是开环指标（L2/碰撞/mIoU/CD/FID）；闭环仿真评测在本综述未成独立表 |
| [学习式与规则式规划](learning-vs-rule-based.md) | Table 9 的相机端到端 / 3D-Occ 规划器多属学习式；规则式基线（NMP/FF/EO）在 LiDAR 行作对照 |

## 注意

- **不同表测不同事**：FID/FVD（生成质量）、CD（点云）、mIoU/IoU（占用）、L2/碰撞（规划）——**不能跨表直接比数字**。比如 DynamicCity 的 FID 和 I2-World-O 的 mIoU 没有可比性。
- **同一表内也要看输入模态**：Table 8/9 都按 3D-Occ / Camera / LiDAR 分组，跨组比要谨慎（如 FSDrive 用特权 ego status）。
- **Avg 含义**：Table 7 是 6 个时域平均；Table 8/9 是 1/2/3 s 三时域平均——平均的时域集合不同，别混读。
- 综述未给 §6 独立页码；具体方法年份/出处按表内引用，未补额外 DOI。
