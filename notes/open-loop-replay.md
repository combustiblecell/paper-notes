# 开环回放（Open-loop replay）

来源：Feng et al., *A Survey of World Models for Autonomous Driving* (arXiv:2501.11260v4) §3.3、Figure 3(a)  
https://arxiv.org/abs/2501.11260v4

## 一句话

用日志或生成器**重放已经定好的未来**；自车当下怎么打方向，周围场景也不改。动作与下一帧观测的因果链是断的。

## 综述里怎么说

§3.3 把预测–规划交互写成一条演进：被动日志回放 → 交互式世界模型。

开环体制（Figure 3(a)）：从 logged data 在静态条件下合成场景；生成器记住场景，却**从不对 new actions 作出反应**。

原文：

> “they merely replay pre-sampled futures without responding to online control inputs, thus confining research to a data-centric, open-loop paradigm that breaks the causal link between present actions and subsequent observations.”

DriveGAN / MagicDrive / [DriveDreamer](drivedreamer.md) 一类偏外观；TrafficGen / LCTGen / RealGen 生成交通仍属严格开环。NAVSIM 也被写成非反应式，只有 quasi-closed-loop 分数。批评：智能体动作从不影响被评的未来时，开环指标会夸大安全与性能。

中间档（Figure 3(b)，不可控闭环）：自回归世界模型会按自车动作往前滚，但潜物理不透明，用户不能改交规、注入稀有事件或调回放速度。本条不把这一档写成开环。

## 和相邻概念

| 概念 | 差别 |
|------|------|
| [可控闭环仿真](controllable-closed-loop.md) | 动作改变下一观测，且场景可编辑、可注入规则/长尾 |
| [形式化](world-model-formalization.md) | 式 (1) 本身没写动作条件；开环就是 $`\bm{w}`$ 不拿当前 $`a`$ 去改 $`\bm{z}`$ |
| [长尾场景](long-tail-scenario.md) | 开环日志里长尾本来就少；综述认为开环也难**注入**稀有事件 |
| [Mode-2 规划](mode-2-planning.md) | 需要「动作 → 未来状态」；纯开环回放评不了这种因果 |
