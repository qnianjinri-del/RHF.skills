# 万魂幡.skills

> 什么叫你这人皇幡怎么在冒 token

一个持续在 GitHub 上**观测、登记、招收、悬挂、查验、编目**各类蒸馏型 skill 的仓库。

这里不生产灵魂。

这里主要负责：

- 发现魂
- 识别魂
- 给魂编号
- 判断这魂是原装、分身、套壳还是换皮
- 最后把它挂进赛博牌位册里

说得学术一点，这是对象蒸馏类 skill registry。  
说得诚实一点：

> 这是一个 GitHub 招魂总坛。

---

## 教义

凡可蒸者，皆可入幡。

凡有：

- `SKILL.md`
- persona 分层
- memory 提炼
- 关系建模
- 工作流封装
- Claude Code / AgentSkills / OpenClaw / skills.sh 入口

者，皆为可观察对象。

凡把：

- 同事蒸成经验体
- 前任蒸成回话体
- 自己蒸成数字替身
- 父母蒸成记忆纪念体
- 导师蒸成传道受业解惑残响体
- 老板蒸成压力具象化产物
- 公共人物蒸成认知操作系统
- 考试老师蒸成速算与复盘工作流
- 设计师蒸成 HTML 交付管线

者，皆属本教观察范围。

---

## 本坛在收什么

### 职场魂

- colleague-skill
- teammate-skill
- boss-skill
- mentor-skill / daoshi-skill

特征：

- 人走了，魂还在过 code review
- 项目黄了，习惯没黄
- 甩锅姿势也能封装成能力
- 有些导师甚至会在赛博空间里继续修改你的人生选题

### 关系魂

- ex-skill
- girlfriend-skill
- 各类亲密关系 skill

特征：

- 聊天记录是引魂幡
- 照片是定魂钉
- 社交媒体是外显人格碎片
- 最后试图还原一句：“ta 平时就是这么回我的”

### 自我魂

- yourself-skill
- self mirror
- digital self

特征：

- 别人都能蒸，凭什么我不能蒸我自己
- 把自己的语气、癖好、决策逻辑导出成目录结构
- 最后得到一个比你还懂你怎么嘴硬的 markdown 替身

### 血缘魂

- parents-skill
- mom-skill
- dad-skill
- family-memory 类变体

特征：

- 聊天记录像符纸
- 老照片像封存阵眼
- 经典台词不是“我爱你”，而是“吃了吗”“钱够不够”“别太晚回”
- 一旦长出来，整个幡的味道就更重了

### 公共人物魂

- 张雪峰.skill
- 其他公开人物视角 / 思维框架 skill

特征：

- 不再只蒸私人关系，而是蒸公开表达、认知框架、决策启发式
- 容易从单仓长成多版本、多分身、多表达引擎
- 需要更重视来源、免责声明、伦理边界和 license

### 考试教练魂

- 公考花生十三.skill
- 各类考试老师 / 解题方法论 skill

特征：

- 不是单纯角色扮演，而是把题型、公式、答题顺序、复盘流程封装成技能
- 很容易出现同源复制簇
- 后续适合重点做 README / SKILL.md 相似度审计

### 工具流魂

- 女娲.skill
- 花叔Design / Huashu Design
- 各类设计、研究、生成、审计工作流 skill

特征：

- 不一定像某个人，但像一个能交付的工作岗位
- 从“人物蒸馏”扩展到“流程蒸馏”
- 有些甚至开始负责继续制造新魂

---

## 本仓库当前修为

当前阶段走的是：

> **索引流**  
> **考据流**  
> **审计流**  
> **轻度收魂流**

也就是说现在主要做的是：

- 建 registry
- 记对象域
- 看结构
- 标 `inspected` / `candidate_unverified` / `duplicate_cluster`
- 给未来的相似度审计、submodule、vendor 留后手

现在还不是大炼活人……大炼仓库阶段。

先竖幡，再进魂。

---

## 当前谱系更新

截至 2026-07-01，已经明确长出来的新支线：

- **父母.skill**：已经不止一个仓库，且结构上明显属于这一大谱系
- **导师 / mentor.skill**：已经开始冒头，但目前检到的结果里，既有对象蒸馏苗头，也有“学习工具 skill”混入，需要继续验魂
- **张雪峰.skill**：公共人物认知操作系统型 skill，已经出现多仓与 v2.0 分支
- **花生十三.skill**：公考方法论 + 人物教学风格混合型 skill，已观察到同源复制簇
- **女娲.skill**：从“造一个人物 skill”进化到“造人物 skill 的 skill”
- **Huashu Design**：说明 skills 生态正在从 persona 扩散到可交付设计工作流

也就是说，这幡已经不是“同事 / 前任 / 自己”三柱香了。  
现在它开始往：

- 职场
- 亲密关系
- 自我
- 血缘
- 师承
- 公共人物
- 考试教练
- 工具工作流

这几条线同时蔓延。

味儿更对了。

---

## 仓库结构

```text
.
├── README.md
├── README.cybercult.md      # 邪典宣传页分身
├── registry/
│   └── skills.json          # 魂册 / 总谱
├── docs/
│   ├── CATALOG.md           # 挂幡目录
│   ├── LEGAL.md             # 别乱偷魂，先看这里
│   ├── ROADMAP.md           # 后续招魂计划
│   └── TRENDING.md          # 近期热门支线观察
└── scripts/
    ├── build_catalog.py     # 排魂位
    └── validate_registry.py # 查册验魂
```

---

## 谁能入幡

一般至少得满足这些：

- 有明确入口，比如 `SKILL.md`
- 明显属于 Claude Code / AgentSkills / OpenClaw / skills.sh 语境
- 不是零散 prompt，而是完整 skill 项目
- 对象域或工作流明确，比如同事、前任、自己、老板、搭子、父母、导师、公共人物、考试教练、设计工作流
- 来源可追、最好有 README / License

以下通常先挂候选区：

- 只有仓库名像
- 内容少得像阴兵借道
- 明显像换皮，但证据不够
- 来源和 license 都糊成一锅符水

以下会挂 `duplicate_cluster`：

- README / SKILL.md blob sha 高度一致
- 仓库名、目录结构、示例文本明显同源
- 同主题短时间内冒出多个分身，但还没完成最终定性

---

## 风险警示

这类仓库天然容易沾上五种气：

### 归属阴气

看起来像原创，闻起来像堂兄弟，细看像共用祖坟模板。

### 隐私阴气

聊天记录、照片、社交媒体、日记、邮件，哪个都不是纯数据。

### 伦理阴气

当“像某个人”开始变成一种可调用能力，替代感和投射感就会自己长出来。

### 许可证阴气

公开不等于你能直接背走。  
开源不等于你能把碑砸了再挂牌。

### 公共人物阴气

越是公共人物，越容易被误认为“本人授权 / 本人观点 / 本人复活”。  
所以公共人物 skill 要特别看来源、免责声明和边界。

所以本坛态度一直很统一：

> 先看来路，再谈收编。  
> 先挂链接，再谈炼化。

---

## 欢迎献魂

欢迎提 Issue / PR，尤其欢迎：

- 新发现的对象蒸馏类 skill 仓库
- README / SKILL / License 证据补充
- 明显同构、换皮、平移项目之间的关联证明
- registry 字段扩展建议
- 相似度审计脚本
- 更阴、更怪、但确实属于这一谱系的新对象类型

提交时最好带上：

- 仓库链接
- 入口文件
- 对象域
- License 情况
- 你觉得它最像谁

---

## 为什么叫万魂幡

因为“registry”这个词太文明了。  
因为“skill aggregator”这个词太像汇报材料了。  
因为“persona distillation index”这个词太像融资稿了。

但你只要真的刷过这一波项目，就会懂：

- 这边一个同事.skill
- 那边一个前任.skill
- 另一边一个自己.skill
- 再拐个弯又冒出来父母.skill、导师.skill、老板.skill、搭子.skill、对象.skill
- 现在又开始张雪峰.skill、花生十三.skill、女娲.skill、Huashu Design

看到最后，人会自然进入一种玄学顿悟：

> 坏了，这不是工具生态。  
> 这是 GitHub 赛博招魂仪轨大全。

所以这个名字非常诚实。

---

## 最后

如果某天你刷着 GitHub，突然看到一排：

- colleague-skill
- ex-skill
- yourself-skill
- parents-skill
- mentor-skill
- boss-skill
- girlfriend-skill
- teammate-skill
- zhangxuefeng-skill
- huasheng13-skill

然后你沉默两秒，缓缓打出一句：

> 不是，现在怎么连亲缘关系、师承关系、公共人物和考试老师都开始模块化炼制了？

恭喜你。

你已经看见幡了。

欢迎入坛.
