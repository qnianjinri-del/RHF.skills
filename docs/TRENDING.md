# TRENDING

> 观测日期：2026-07-01  
> 状态：先挂链接，再谈收编；先看谱系，再谈炼化。

## 这次新增的几条新支线

### 1. 公共人物魂：张雪峰.skill

这批不再是“同事 / 前任 / 自己”那种私人对象蒸馏，而是把公共人物的表达风格、心智模型、决策启发式做成可调用 skill。

已核验代表：

- `alchaincyf/zhangxuefeng-skill`
  - 有 `README.md` 与 `SKILL.md`
  - README 明确称其为“张雪峰的认知操作系统”
  - SKILL.md 有触发条件、角色规则、研究流程、fallback 树
  - 先标记为 `inspected`

候选/分身：

- `OpenDemon/zhang-xue-feng-skill`
  - 有 README 与 SKILL
  - 更轻量，许可证与来源链路暂未充分核验
  - 标记为 `candidate_unverified`

- `a18515373115-droid/ZhangXueFeng-skill`
  - README 标为 v2.0
  - 强调表达引擎、来源标注、情绪危机处理
  - SKILL frontmatter 含额外字段与中文 name，需核验 runtime 兼容性
  - 标记为 `candidate_unverified`

判断：张雪峰.skill 这条线已经不是孤例，而是开始出现多仓、多版本、多表达规则的扩散。

---

### 2. 考试教练魂：花生十三.skill

这批把“人物风格”与“考试方法论库”合在一起，不只是扮演老师，而是把行测/申论的模块、题型、速算、复盘流程写成技能工作流。

已核验代表：

- `WangJunqing-coder/huasheng13-skill`
  - 有 `README.md` 与 `SKILL.md`
  - README 覆盖资料分析、数量关系、言语理解、判断推理、常识判断、申论
  - SKILL.md 有触发词、单题讲解、模块方法论、套题复盘、备考规划流程
  - 标记为 `inspected`

候选/分身：

- `wsjackys/huasheng13-skill`
  - README blob sha 与 `WangJunqing-coder/huasheng13-skill` 一致
  - 先标记为 `duplicate_cluster`

判断：花生十三.skill 已经出现明显同源复制簇，后续适合优先跑相似度审计。

---

### 3. 造魂工具：女娲.skill

这批不再只蒸馏一个对象，而是试图把“蒸馏人物 skill”本身做成工具。

代表：

- `alchaincyf/nuwa-skill`
  - README 明确写到输入名字即可自动完成调研、提炼、验证流程
  - SKILL.md 强调提炼 how they think，而不是复读 what they said
  - 这类项目会让人物 skill 生产成本继续下降
  - 标记为 `inspected`

判断：这是从“单个魂”进化到“炼魂炉”。后续 registry 需要区分 `persona_generator` 与普通 `persona`。

---

### 4. 工具流魂：花叔Design / Huashu Design

这类不是人物蒸馏，但它说明 skills 生态正在从 persona 扩散到可交付工作流。

代表：

- `alchaincyf/huashu-design`
  - README 主打 HTML 原型、动画、PPT、信息图等视觉交付
  - SKILL.md 有明确触发词、事实验证规则、设计流程、反 AI slop 机制
  - 标记为 `inspected`

判断：这类项目不属于传统对象魂，但属于 skills 生态中很重要的“工具流魂”。万魂幡可以先挂，不急着炼。

---

## 新增状态说明

### `duplicate_cluster`

用于标记已经观察到明显同源复制、README/SKILL 高度一致、或者仓库名/文件结构高度近似的条目。

这不是最终定性，不等于抄袭判定。只是说：

> 这几个魂味儿太像，先挂同一串，后面再验 DNA。

---

## 后续优先审计

1. 张雪峰.skill 同主题仓库之间的 SKILL.md frontmatter 差异
2. 花生十三.skill 复制簇的 README / SKILL blob sha 对比
3. 女娲.skill 与张雪峰.skill 的生成链路关系
4. Huashu Design 这类工具流 skill 是否应单独开 theme
5. 公共人物 skill 的免责声明、来源、伦理边界是否需要单列字段
