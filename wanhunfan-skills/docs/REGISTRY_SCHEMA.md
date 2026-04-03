# Registry Schema

`registry/skills.json` 的顶层结构：

```json
{
  "project": "wanhunfan-skills",
  "version": "0.1.0",
  "entries": []
}
```

## entry 字段

- `id`: 全局唯一 ID
- `title`: 项目标题
- `repo_full_name`: `owner/repo`
- `repo_url`: GitHub URL
- `theme`: 主题分类，如 `relationship`, `workplace`, `self`
- `object_type`: 蒸馏对象类型，如 `ex`, `colleague`, `self`
- `entry_file`: 一般为 `SKILL.md`
- `commands`: 触发命令列表
- `runtime_targets`: 兼容环境，如 `Claude Code`, `AgentSkills`, `OpenClaw`
- `generated_output_dir`: 项目用于写出实例 skill 的目录
- `license_signal`: 当前观测到的许可证信号
- `inspection_status`: `inspected` / `candidate_unverified` / `rejected`
- `integration_strategy`: `reference_only` / `submodule_candidate` / `vendor_candidate` / `rejected`
- `notes`: 备注
- `evidence`: 证据列表，记录本仓库是根据哪些文件得出判断

## 说明

这个 schema 刻意偏“审计型”，而不是偏“安装器型”。

原因是当前这批仓库高度同构，直接安装不是问题，**甄别差异、避免误收、保留归属** 才是核心问题。
