# 长尾场景（Long-tail scenarios）

来源：Feng, Wang & Yang, *A Survey of World Models for Autonomous Driving* (arXiv:2501.11260v4) §1、§4、§8  
https://arxiv.org/abs/2501.11260v4

## 一句话

日志里极少出现、却一旦失手就危及安全的驾驶情形（极端天气、施工区、异常驾驶等）；世界模型常被用来**生成/排练**这些稀有情况，而不是只靠路上再采一遍。

## 综述里怎么说

原文（第2页，Introduction）：

> “Equally pivotal is the system’s resilience in extreme or long-tail scenarios (e.g., severe weather, construction zones, or erratic driving behaviors), where performance shortfalls can compromise overall safety.”

生成式世界模型的卖点之一是用扩散等手段补长尾数据（第25页，Conclusion）：

> “Generative methods, particularly diffusion-based approaches, now facilitate diverse synthetic data for long-tail scenarios, enhancing model robustness in rare or extreme conditions.”

§4 还写：条件生成可以外推到日志里没有的 corner case；但纯合成课程的安全评估仍开放。

## 和相邻概念

| 概念 | 差别 |
|------|------|
| [异构传感器](heterogeneous-sensors.md) | 长尾常伴随传感器退化（大雨、脏污）；多源融合是应对手段之一 |
| [多传感器压成潜状态](multi-sensor-latent-state.md) | 潜状态前滚用来在「脑子里」试稀有未来，不必真开到事故现场 |
| [多模态](multimodality.md) | 预测一对多；长尾是**数据分布**上的稀有，不是路口左转/右转那种分支本身 |
| SDDiff / 室外 EVE | 开阔地点数少、性能掉，是雷达感知里的一类长尾/分布偏移 |

## 注意

不要把「长尾」写成论文里没写的具体事故类型。本文举例限于恶劣天气、施工、异常驾驶。
