# SDDiff: Boost Radar Perception via Spatial-Doppler Diffusion

- 作者：Shengpeng Wang, Xin Luo, Yulong Xie, Wei Wang
- 标识：https://arxiv.org/abs/2506.16936v1
- 来源：paper-read

## 摘要

毫米波雷达的点云提取与自车速度估计以往常被分开处理，容易忽略空间占用与多普勒的协同，从而在多径鬼影和稀疏噪声点上引入偏差。本文提出 SDDiff：将雷达 ADC 编码为同时包含占用与多普勒的空间-多普勒表示，用带雷达先验的定向扩散从粗糙表示净化到稠密点云，并用迭代多普勒精炼抑制鬼影、适应密度变化。在 ColoRadar 与自采数据上，相对已有方法，室内/室外 EVE 约提升 30% 与 59%，有效点密度与 PCE 可靠性也明显提高。
