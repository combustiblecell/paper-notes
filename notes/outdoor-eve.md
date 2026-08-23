# 室外 EVE

来源：Wang et al., *SDDiff*, arXiv:2506.16936v1，§2.3、§5.2、Table 3–4  
https://arxiv.org/abs/2506.16936

## 一句话

开阔室外是 EVE 的**更难档**：机载点更稀，基线掉得更凶；SDDiff 把室外 MAE 做到 0.11 m/s，文称相对 SOTA 高 59%。

## 要点

- 失败原因（§2.3）：`In open environments with few points, such methods suffer significant performance degradation or even complete failure.`
- Table 3（第7页）室外 MAE：ICP 0.77、RANSAC 0.57、RadarEVE 0.27、SDDiff **0.11** m/s。相对 RadarEVE：$(0.27-0.11)/0.27 \approx 59\%$，与 §5.2 表述一致。
- 室内对照：RadarEVE 0.13 → SDDiff 0.09（约 30%）。
- 消融 Table 4：去掉可靠占用、只留 EVE 模块时，室外误差 0.11 → **0.37** m/s（文称 $`3.4\times`$）；室内 0.09 → 0.11。室外更依赖 PCE 给的稠密、可信点。
- 累计误差密度（Table 3，室外）：SDDiff 在 $`\le 0.1`$ m/s 为 55%，RadarEVE 为 14%。

Abstract 的 `59% higher in EVE accuracy`（第1页）按正文应对**室外**，不是室内外平均。

## 和相邻概念的对比

| | 室内 EVE | 室外 EVE |
|--|----------|----------|
| 点数 / 结构 | 墙面多，CFAR 仍能凑合 | 开阔、回波少 |
| 基线 | RadarEVE 尚可用（0.13） | 掉到 0.27，配准更差 |
| SDDiff 增益 | 约 30% | 约 59%，也更吃 PCE |

总任务定义见 [eve.md](eve.md)；评测对手见 [sota.md](sota.md)；互惠机制见 [pce.md](pce.md)。
