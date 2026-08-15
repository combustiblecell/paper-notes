# Wayne & Abbott 多层前向模型

来源：LeCun 2022 立场文 §4.6–4.7、§7.1；Wayne & Abbott, *Hierarchical Control Using Networks Trained with Higher-Level Forward Models*, Neural Computation 26(10), 2014  
https://doi.org/10.1162/neco_a_00639

## 一句话

**高层控制器控制低层控制器**，训练时用各层 forward model（含对低层控制器的模型）+ cost minimization 生成最优关联；LeCun 引为分层规划先驱，但批评其中间动作词汇需预定义。

## 要点

```
高层 Controller ──▶ 低层 Controller ──▶ Plant
       ↑                    ↑
  高层前向模型          低层前向模型
（含低层控制器模型）
```

- 训练：forward model + cost minimization → 最优 (感知, 命令) 关联
- 推理：网络直接映射，快速
- 任务示例：铰接式卡车穿越障碍物到目标
- 可扩展多层；低层不必为复杂任务重训

LeCun 原文（§4.7，第31页）：

> “Hierarchical planning is a difficult topic with few solutions, most of which require that the intermediate vocabulary of actions be predefined. But if one abides by the deep learning philosophy, those intermediate representations of action plans should also be learned.”

§7.1 明确引用 Wayne & Abbott (2014) 的 stacked forward models 指定 intermediate goals。

## 和 H-JEPA 的对比

| | Wayne & Abbott | H-JEPA (LeCun) |
|--|----------------|----------------|
| 层级关系 | 高层控**低层控制器** | JEPA-2 预测 JEPA-1 **表征** |
| 中间表示 | 训练时构造，动作词汇预定义 | **端到端可学习**抽象表征 |
| 前向模型 | 每层显式 forward model | JEPA predictor 在嵌入空间 |
| 高层「动作」 | 低层命令 | 下层**状态条件 / 子目标**（§4.7） |
| 不确定性 | 未重点讨论 | latent $`z`$ + MCTS 式 pruning（Figure 17） |

H-JEPA 堆叠与训练方式见 [jepa.md](jepa.md)；Mode-2 规划见 [mode-2-planning.md](mode-2-planning.md)。
