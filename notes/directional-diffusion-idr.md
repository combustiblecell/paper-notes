# 定向扩散 + 迭代多普勒精炼

来源：Wang et al., *SDDiff*, arXiv:2506.16936v1，§3.1–3.3  
https://arxiv.org/abs/2506.16936

## 一句话

SDDiff 的两块核心：从**雷达先验**出发、朝 LiDAR 占用走的定向扩散；以及用**多普勒一致性**当 critic 的 Iterative Doppler Refinement。两者一起把粗 [SDDR](sddr.md) 雕成细 SDDR。

## 定向扩散（radar prior）

常规 DDPM 从标准高斯走很远，步数多、对纯化任务结果糊。原文：`it requires a plethora of sampling steps and produces ambiguous outcomes for the SDDR purification task.`（§3.1，第3页）

改为：雷达占用 $`u_0`$ 当先验，目标是 LiDAR 占用 $`x_0`$。正向（Eq. 1，第4页）：

```math
q(x_t \mid x_{t-1}, u_0)
:= \mathcal{N}\big(x_t;\ \alpha_t x_{t-1} + (1-\alpha_t)u_0,\ \lambda_t^2 I\big)
```

反向用噪声网络 $`\epsilon_\theta(x_t, u_0)`$，空间损失 $`L_{\mathrm{Spatial}}`$（Eq. 7）。实现里采样步 $`T=20`$（§4.2）。Theorem 1/2 的证明在 supplementary appendix，**本 PDF 未找到（Not found）**。

## 迭代多普勒精炼（IDR）

静止目标相对雷达的径向速度由自车速度与角度决定（Eq. 8）：

```math
v^r_{i,j}
= [\cos a_i\cos e_j,\ \sin a_i\cos e_j,\ \sin e_j]
\cdot v_{\mathrm{ego}}
```

场景级 PCE 里静态目标占主导，故用 Doppler-consistency  refinement 占用：对 $`x_t`$ 沿 range 做 reduction + softmax 得软掩膜 $`M_t`$，再

```math
L_{\mathrm{Doppler}}
= \mathbb{E}\big[\ldots\ \|v_{\mathrm{ego}} - f_\psi(M_t \odot v)\|_2^2\big]
```

总损失：$`L_{\mathrm{SDDNet}} = L_{\mathrm{Spatial}} + \omega L_{\mathrm{Doppler}}`$，$`\omega=0.01`$（§3.3、§4.2）。

## 和相邻概念的对比

| | 定向扩散 + IDR | 标准潜扩散 / Modified 3D-Diff | JEPA / 潜变量生成 |
|--|---------------|------------------------------|-------------------|
| 起点 | 雷达占用 $`u_0`$ | 标准高斯 | 表征或像素生成 |
| 条件 | 多普勒剖面 cross-attn | 多为强度占用 | — |
| 物理约束 | Eq. 8 可微 $`f_\psi`$ | 无 | 见 [latent-variable-generative-model.md](latent-variable-generative-model.md) |

消融（Table 4，第7页）：去掉多普勒后 VPR 77.1% → 65.5%；只留 EVE 时室外误差 0.11 → 0.37 m/s；仅 PCE 模块相对 Modified 3D-Diff 推理速度 $`3.13\times`$。

输出任务：[PCE](pce.md)、[EVE](eve.md)。要抗的现象：[多径鬼影](multipath-ghosting.md)。
