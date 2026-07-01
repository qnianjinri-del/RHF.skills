# ROADMAP

## v0.3.x

- 记录 2026-07 之后冒头的热门 skills 支线：公共人物、考试教练、skill 生成器、设计工作流
- 对张雪峰.skill、花生十三.skill 这类快速分身项目增加 `duplicate_cluster` 观察状态
- 给 inspected 条目补充 evidence 链路，优先保留 README / SKILL / LICENSE 信号
- 新增 `docs/TRENDING.md`，把“为什么这批算新支线”单独写清楚

## v0.4.x

- 增加 similarity audit 脚本
- 对 `SKILL.md` frontmatter 做结构比对，识别额外字段、中文 name、description 过短等兼容性风险
- 对 README / SKILL.md blob sha 做重复簇聚类
- 对 `prompts/`、`tools/`、`references/` 做重名/相似度检查

## v0.5.x

- 给 inspected 条目生成更完整的人工审计卡片
- 区分“原创骨架”“主题换皮”“高度复刻”“工具流扩展”
- 评估是否需要统一安装器或同步脚本

## v0.6.x

- 视许可证情况选择少量仓库进入 `submodule_candidate`
- 增加 provenance / attribution / license 字段的强校验
- 给高风险 persona / public figure skill 增加伦理与安全边界记录
