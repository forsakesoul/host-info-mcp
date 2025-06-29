# AI MCP - 主机信息服务器

[![Python](https://img.shields.io/badge/python-%3E%3D3.11-blue.svg)](https://www.python.org/)
[![MCP](https://img.shields.io/badge/MCP-1.10.1+-green.svg)](https://github.com/modelcontextprotocol/servers)

一个专为 Cursor IDE 设计的 MCP（Model Context Protocol）服务器，用于获取真实的主机系统信息。通过此工具，AI 助手可以准确获取您计算机的硬件配置信息。

## ✨ 功能特性

- 🖥️ **系统信息获取**: CPU型号、架构、核心数量
- 💾 **内存信息**: 系统总内存大小
- 🔧 **操作系统**: 系统类型、版本信息
- 🐍 **Python环境**: Python版本信息
- 🔄 **实时查询**: 获取当前系统状态
- 🎯 **Cursor集成**: 专为Cursor IDE优化

## 🚀 快速开始

### 安装依赖

```bash
# 使用 uv (推荐)
uv sync

# 或使用 pip
pip install mcp psutil
```

### 测试运行

```bash
python main.py
```

### 配置 Cursor IDE

详细配置步骤请参考 [CURSOR_SETUP.md](./CURSOR_SETUP.md)

快速配置：在 Cursor 的 MCP 设置中添加：

**使用 uv (推荐)：**
```json
{
  "mcpServers": {
    "hostInfoMcp": {
      "command": "uv",
      "args": [
        "--directory",
        "${workspaceFolder}",
        "run",
        "main.py"
      ]
    }
  }
}
```

**使用 python：**
```json
{
  "mcpServers": {
    "host-info-mcp": {
      "command": "python",
      "args": ["${workspaceFolder}/main.py"],
      "env": {
        "PYTHONPATH": "${workspaceFolder}"
      }
    }
  }
}
```

## 📋 可用工具

### `get_host_info`
获取完整的主机系统信息，返回 JSON 格式数据：

```json
{
    "system": "Darwin",
    "release": "24.5.0",
    "machine": "arm64",
    "processor": "arm",
    "python_version": "3.11.5",
    "memory_gb": "16.00",
    "cpu_count": "8",
    "cpu_model": "Apple M1 Pro"
}
```

### `get_system_info`
同 `get_host_info`，提供中文描述和使用指导。

## 💬 使用示例

配置完成后，您可以在 Cursor 中这样询问：

- "我的电脑有多少个 CPU 核心？"
- "我的系统架构是什么？"
- "我有多少内存？"
- "我的操作系统版本是什么？"

AI 助手会自动调用 MCP 工具获取真实信息并回答。

## 🛠️ 项目结构

```
host-info-mcp/
├── main.py              # MCP 服务器主文件
├── tool.py              # 系统信息获取工具
├── pyproject.toml       # 项目配置
├── README.md            # 项目说明文档
├── CURSOR_SETUP.md      # Cursor 配置指南
└── uv.lock              # 依赖锁定文件
```

## 🔧 开发说明

### 添加新工具

1. 在 `tool.py` 中添加新函数
2. 在 `main.py` 中注册工具：
   ```python
   @mcp.tool()
   def your_new_tool() -> str:
       """工具描述"""
       return "结果"
   ```
3. 重启 Cursor IDE

### 技术栈

- **MCP Protocol**: 模型上下文协议
- **FastMCP**: MCP 服务器框架
- **psutil**: 系统信息获取
- **Python 3.11+**: 运行环境

## 📝 许可证

本项目采用 MIT 许可证，详见 LICENSE 文件。

## 🤝 贡献

欢迎提交 Issue 和 Pull Request！

## 📞 支持

如遇问题，请：
1. 查看 [CURSOR_SETUP.md](./CURSOR_SETUP.md) 中的故障排除部分
2. 提交 Issue 描述问题
3. 检查项目依赖是否正确安装

---

