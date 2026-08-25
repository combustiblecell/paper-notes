# 概念总览 · 关系图

两条来源主线：

- LeCun, *A Path Towards Autonomous Machine Intelligence* (2022) → L0–L5
- Wang et al., *SDDiff* (arXiv:2506.16936v1) → L6–L8
- Feng et al., *A Survey of World Models for Autonomous Driving* (arXiv:2501.11260v4) → L9

节点对应 `notes/` 下各条笔记；**实线**=组成/实现，**虚线**=对照或历史先驱。

```mermaid
flowchart TB
  subgraph L0["L0 · 总架构"]
    ARCH["Figure 2 六模块架构<br/>six-module-architecture"]
  end

  subgraph L1["L1 · 行为与预测"]
    WM["前向模型 / World Model<br/>forward-model"]
    M2["Mode-2 规划<br/>mode-2-planning"]
  end

  subgraph L2["L2 · 世界模型实现（主推）"]
    JEPA["JEPA / H-JEPA<br/>jepa"]
    MULTI["多模态<br/>multimodality"]
  end

  subgraph L3["L3 · 训练范式"]
    VIC["VICReg 非对比<br/>vicreg"]
    CL["InfoNCE / SimCLR<br/>contrastive-learning"]
  end

  subgraph L4["L4 · 对照路线"]
    LV["潜变量生成模型<br/>latent-variable-generative-model"]
    VAE["VAE / GAN / VQ-VAE<br/>vae-gan-vqvae"]
    MAE["MAE<br/>mae"]
  end

  subgraph L5["L5 · 分层规划先驱"]
    WA["Wayne & Abbott<br/>wayne-abbott-hierarchical-forward"]
  end

  subgraph L6["L6 · 雷达输入与表示"]
    ADC["雷达 ADC<br/>radar-adc"]
    SDDR["SDDR 占用+多普勒<br/>sddr"]
    GHOST["多径鬼影<br/>multipath-ghosting"]
  end

  subgraph L7["L7 · SDDiff 纯化"]
    DIFF["定向扩散 + IDR<br/>directional-diffusion-idr"]
  end

  subgraph L8["L8 · 雷达任务与尺子"]
    PCE["点云提取 PCE<br/>pce"]
    EVE["自车速度 EVE<br/>eve"]
    OUT["室外 EVE<br/>outdoor-eve"]
    SOTA["SOTA（本文评测）<br/>sota"]
  end

  subgraph L9["L9 · 驾驶 WM 综述用语"]
    HET["异构传感器<br/>heterogeneous-sensors"]
    LAT["多传感器潜状态<br/>multi-sensor-latent-state"]
    TAIL["长尾场景<br/>long-tail-scenario"]
  end

  ARCH -->|"World Model 模块"| WM
  ARCH -->|"Actor Mode-2"| M2

  WM -->|"表征空间预测"| JEPA
  JEPA -->|"JEPA-1 → JEPA-2 堆叠"| JEPA
  JEPA -->|"不变性 + z"| MULTI

  JEPA -->|"推荐训练"| VIC
  JEPA -.->|"可用但易维数灾难"| CL
  VIC -.->|"对比 vs 非对比"| CL

  JEPA -.->|"非生成式替代"| LV
  LV --> VAE
  JEPA -.->|"不重建像素"| MAE
  MULTI -.->|"z 采样多分支"| LV

  JEPA -.->|"可学习中间表征"| WA
  WA -.->|"子目标 / 分层 rollout"| M2
  MULTI -->|"不确定环境下多轨迹"| M2
  WM -->|"Pred(s,a) rollout"| M2

  ADC -->|"FFT + 峰位"| SDDR
  GHOST -.->|"假占用/高强度"| SDDR
  GHOST -.->|"只靠强度会误导"| PCE
  SDDR -->|"纯化对象"| DIFF
  DIFF -->|"稠密点"| PCE
  DIFF -->|"速度约束"| EVE
  PCE -->|"互惠 inlier"| EVE
  EVE -->|"更难档"| OUT
  PCE -.->|"VPR/SRL/EGD"| SOTA
  OUT -.->|"59% 那条"| SOTA
  LV -.->|"生成式扩散对照"| DIFF

  HET -->|"压缩进同一表示"| LAT
  LAT -->|"驾驶版 WM"| WM
  LAT -->|"表征空间预测"| JEPA
  HET -->|"雷达是其中一种"| ADC
  TAIL -.->|"稀有天气/施工/异常驾驶"| LAT
  TAIL -.->|"生成式补数据"| LV
```

## 图例

| 线型 | 含义 |
|------|------|
| 实线 `-->` | 组成、实现、推荐路径 |
| 虚线 `-.->` | 对照组、历史先驱、可选但不主推 |

## 分层阅读顺序（建议）

**JEPA 线**

1. **总架构** → [six-module-architecture.md](six-module-architecture.md)
2. **世界模型核心** → [forward-model.md](forward-model.md) → [jepa.md](jepa.md)
3. **怎么训练** → [vicreg.md](vicreg.md)（对照 [contrastive-learning.md](contrastive-learning.md)）
4. **多模态与规划** → [multimodality.md](multimodality.md) → [mode-2-planning.md](mode-2-planning.md)
5. **为何不用生成式** → [latent-variable-generative-model.md](latent-variable-generative-model.md) / [vae-gan-vqvae.md](vae-gan-vqvae.md) / [mae.md](mae.md)
6. **分层先驱** → [wayne-abbott-hierarchical-forward.md](wayne-abbott-hierarchical-forward.md)

**SDDiff 雷达线**

1. **输入** → [radar-adc.md](radar-adc.md) → [sddr.md](sddr.md)
2. **干扰** → [multipath-ghosting.md](multipath-ghosting.md)
3. **方法** → [directional-diffusion-idr.md](directional-diffusion-idr.md)
4. **任务** → [pce.md](pce.md) → [eve.md](eve.md) → [outdoor-eve.md](outdoor-eve.md)
5. **怎么读表** → [sota.md](sota.md)

**驾驶 WM 综述用语（Feng et al.）**

1. **输入种类** → [heterogeneous-sensors.md](heterogeneous-sensors.md)
2. **怎么编码** → [multi-sensor-latent-state.md](multi-sensor-latent-state.md)
3. **为何要想象未来** → [long-tail-scenario.md](long-tail-scenario.md)

## 三条主轴（一句话）

| 主轴 | 节点链 |
|------|--------|
| **架构（JEPA）** | 六模块 → 前向模型 → JEPA → Mode-2 规划 |
| **训练（JEPA）** | JEPA ← VICReg；对比 InfoNCE/MAE 为对照 |
| **雷达感知（SDDiff）** | ADC → SDDR → 定向扩散+IDR → PCE ↔ EVE；鬼影为干扰，SOTA 为尺子 |
| **驾驶 WM 用语（综述）** | 异构传感器 → 压成潜状态 → 前向模型；长尾靠潜空间/生成补稀有情况 |

## 笔记索引

| 笔记 | 一句话 |
|------|--------|
| [six-module-architecture](six-module-architecture.md) | 可微分六模块 + Mode-1/2 |
| [forward-model](forward-model.md) | $`s_{t+1}=\mathrm{Pred}(s_t,a_t)`$ |
| [jepa](jepa.md) | 表征空间非生成式预测 + H-JEPA |
| [multimodality](multimodality.md) | 一对多未来：不变性 + $`z`$ |
| [vicreg](vicreg.md) | 非对比防 collapse |
| [contrastive-learning](contrastive-learning.md) | InfoNCE/SimCLR 对照 |
| [mode-2-planning](mode-2-planning.md) | 世界模型内 MPC |
| [latent-variable-generative-model](latent-variable-generative-model.md) | $`z`$ 参数化相容 $`y`$ 集合 |
| [vae-gan-vqvae](vae-gan-vqvae.md) | 像素空间生成式多模态 |
| [mae](mae.md) | mask 重建像素（对比式） |
| [wayne-abbott-hierarchical-forward](wayne-abbott-hierarchical-forward.md) | 多层前向模型分层控制先驱 |
| [radar-adc](radar-adc.md) | 原始采样；SDDiff 的输入，不是 CFAR 点 |
| [sddr](sddr.md) | 极性占用 + 多普勒，PCE/EVE 的共同表示 |
| [directional-diffusion-idr](directional-diffusion-idr.md) | 雷达先验定向扩散 + 多普勒一致性精炼 |
| [pce](pce.md) | 低层抽点；与 EVE 互惠 |
| [eve](eve.md) | 高层估自车速度；吃纯化后的点/表示 |
| [outdoor-eve](outdoor-eve.md) | 开阔地更难；文称相对 SOTA +59% |
| [sota](sota.md) | 本文选定的 PCE/EVE 基线尺子 |
| [multipath-ghosting](multipath-ghosting.md) | 多径假占用；只靠强度会误导 PCE |
| [heterogeneous-sensors](heterogeneous-sensors.md) | 相机/LiDAR/雷达等收进同一环境表示 |
| [multi-sensor-latent-state](multi-sensor-latent-state.md) | 多传感器压缩成可前滚的潜状态 |
| [long-tail-scenario](long-tail-scenario.md) | 稀有危险情形；生成/排练补数据 |

> GitHub 可直接渲染上方 Mermaid。本地若看不到图，用 VS Code Mermaid 插件或 Obsidian。
