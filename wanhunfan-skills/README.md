# 万魂幡.skills

把 GitHub 上这波围绕 `.skill` / `SKILL.md` / AgentSkills / Claude Code 生态出现的「人格蒸馏」「角色蒸馏」「工作分身」类仓库，整理成一个**可检索、可追踪、可审计、可继续扩展**的总索引。

这个仓库的定位不是“把别人项目直接一锅端”，而是先做成一个**适合公开上传 GitHub 的聚合索引仓**：

1. 统一收录上游仓库
2. 记录结构、命令、对象域、运行环境、许可信号
3. 区分“已人工检查”和“仅名称命中候选”
4. 为后续去重、相似度比对、submodule/vendor 决策留出空间

## 本仓库现在是什么

当前版本是一个 **reference-first** 聚合仓。

也就是：
- 先收录 metadata 和外链
- 暂不直接 vendoring 上游内容
- 暂不做侵入式改写
- 暂不把许可不明或未核验仓库混进“已确认可收录”列表

这样更适合你直接发到 GitHub，也更不容易在一开始就踩到归属和许可证坑。

## 首批已核验收录

### 1. `therealXiaomanChu/ex-skill`
- 主题：前任 / 亲密关系蒸馏
- 结构：`Relationship Memory + Persona`
- 入口：`SKILL.md`
- 输出目录：`exes/{slug}/`
- 状态：`inspected`

### 2. `perkfly/ex-skill`
- 主题：前任 / 亲密关系蒸馏
- 结构：`Memories + Persona`
- 入口：`SKILL.md`
- 输出目录：`exes/{slug}/`
- 状态：`inspected`

### 3. `notdog1998/yourself-skill`
- 主题：自己 / 自我镜像 / 数字分身
- 结构：`Self Memory + Persona`
- 入口：`SKILL.md`
- 输出目录：`.claude/skills/{slug}/`
- 状态：`inspected`

### 4. `titanwings/colleague-skill`
- 主题：同事 / 职场分身 / 工作经验蒸馏
- 结构：`Work Skill + Persona`
- 入口：`SKILL.md`
- 输出目录：`colleagues/{slug}/`
- 状态：`inspected`

## 候选但未纳入“已核验”清单

这些仓库**可以保留在 registry 里**，但当前只建议标成 `candidate_unverified`：

- `LeoYeAI/teammate-skill`
- `echoVic/boss-skill`
- `nicepkg/boss-skill`
- `yian0625/girlfriend-skill`

原因很简单：
- 仓库名和主题命中了
- 但我现在拿到的结构证据还不够完整
- 所以它们适合进候选池，不适合伪装成“已审完可以放心整合”的条目

## 为什么这个思路更适合“万魂幡”

因为这类项目的真正价值不在于“复制越多越好”，而在于：

- 哪些仓库确实有独立增量
- 哪些只是同模板换皮
- 哪些对象域值得单独成类
- 哪些仓库未来适合做 submodule
- 哪些仓库最好只保留索引和外链

所以“万魂幡.skills”最合理的第一阶段，不是代码大杂烩，而是：

- **总目录**
- **总注册表**
- **总审计入口**

## 当前收录标准

### 收录进 registry
满足任一即可进入候选：
- 仓库名明显属于某种 `xxx-skill`
- README / `SKILL.md` 明显处于 Claude Code / AgentSkills / OpenClaw 语境
- 明显是“把人/角色/人格/工作经验蒸馏成 skill”的项目

### 标成 inspected
必须至少满足：
- 看到了 README 或 `SKILL.md` 的有效内容
- 能判断对象域和基本结构
- 能判断它确实不是普通 skills 集合仓或无关项目

### 暂不纳入
- 普通 skills marketplace / skill collection
- 不是对象蒸馏类，而是通用工具 skill
- 许可/归属风险过高且没有必要先碰的

## 目录结构

```text
wanhunfan-skills/
├── README.md
├── registry/
│   └── skills.json
├── docs/
│   ├── CATALOG.md
│   ├── LEGAL.md
│   ├── ROADMAP.md
│   └── REGISTRY_SCHEMA.md
└── tools/
    ├── build_catalog.py
    └── validate_registry.py
```

## 使用方式

### 校验 registry

```bash
python tools/validate_registry.py
```

### 重新生成目录页

```bash
python tools/build_catalog.py
```

## 下一步最值得做的事

1. 继续补“对象蒸馏类”仓库
2. 给 `inspected` 条目补更完整的结构字段
3. 做相似度审计，识别明显套壳/高度重复仓库
4. 再决定哪些可以进入 `submodule_candidate` 或 `vendor_candidate`

## 说明

这个版本已经是**适合直接上传 GitHub** 的版本：
- 有 README
- 有 registry
- 有文档
- 有脚本
- 有已核验首批条目
- 也保留了候选池

但它仍然保持克制：
- 不冒充你已经完成了全部仓库核验
- 不直接复制上游内容
- 不把证据不足的仓库伪装成“已确认可收录”
