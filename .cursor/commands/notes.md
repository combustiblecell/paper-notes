---
description: 在 notes/ 里新增或更新一条概念笔记
---

# /notes

把当前对话里正在讲的概念写成仓库笔记。

## 怎么做

1. 在 `notes/` 下新增或更新 `notes/<slug>.md`（slug 用英文短横线，如 `jepa.md`）。
2. 结构尽量包含：标题、一句话、来源（论文/链接）、要点、和相邻概念的对比。
3. 默认中文；论文原文引用保持英文。
4. 不要编造页码、DOI、实验结果。
5. 写完后用 `git add` / `git commit` / `git push origin main` 同步；commit 说明用 `Add [concept] notes`。
6. 用户在对话里用 `@notes` 即可把整个笔记目录当作上下文。
