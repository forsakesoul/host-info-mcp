# Cursor MCP 配置指南

## 概述
本指南将帮助您在 Cursor IDE 中配置 `host-info-mcp` 服务器，使 AI 助手能够获取您电脑的真实系统信息。

## 配置步骤

### 1. 准备工作
确保您的 MCP 服务器已正确安装依赖：
```bash
# 在项目目录中运行
pip install -r requirements.txt
# 或者如果使用 uv
uv sync
```

### 2. 测试 MCP 服务器
在配置 Cursor 之前，先测试服务器是否正常工作：
```bash
python main.py
```

### 3. 配置 Cursor

#### 方法一：通过 Cursor 设置界面
1. 打开 Cursor IDE
2. 按 `Cmd+,` (macOS) 或 `Ctrl+,` (Windows/Linux) 打开设置
3. 搜索 "MCP" 或 "Model Context Protocol"
4. 在 MCP 服务器配置中添加新服务器

#### 方法二：直接编辑配置文件
1. 找到 Cursor 的配置文件位置：
   - **macOS**: `~/Library/Application Support/Cursor/User/globalStorage/cursor.mcp/settings.json`
   - **Windows**: `%APPDATA%\Cursor\User\globalStorage\cursor.mcp\settings.json`
   - **Linux**: `~/.config/Cursor/User/globalStorage/cursor.mcp/settings.json`

2. 在配置文件中添加以下内容：
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

### 4. 重启 Cursor
配置完成后，重启 Cursor IDE 使配置生效。

### 5. 验证配置
1. 重启后，在 Cursor 中应该能看到 MCP 工具已启用
2. 您可以询问类似这样的问题来测试：
   - "我的电脑有多少个 CPU 核心？"
   - "我的系统架构是什么？"
   - "我有多少内存？"
   - "我的操作系统版本是什么？"

## 可用工具

配置完成后，AI 助手将可以访问以下工具：

### `get_host_info`
- **功能**: 获取完整的系统信息
- **返回**: JSON格式的系统信息，包括：
  - CPU 数量和型号
  - 系统架构
  - 内存大小
  - 操作系统版本
  - Python 版本

### `get_system_info`
- **功能**: 同 `get_host_info`，提供额外的中文描述
- **用途**: 当询问系统硬件信息时自动调用

## 使用示例

配置完成后，您可以这样与 AI 对话：

**用户**: "我的电脑有多少个 CPU？什么架构？"

**AI 助手**: *会自动调用 MCP 工具获取真实信息并回答*

## 故障排除

### 问题：显示 "0 tools enabled"
- 检查配置文件路径是否正确
- 确认 Python 环境可以正常运行 `main.py`
- 检查配置文件 JSON 语法是否正确
- 重启 Cursor IDE

### 问题：工具调用失败
- 检查项目依赖是否已安装
- 确认 `PYTHONPATH` 设置正确
- 查看 Cursor 的开发者工具或日志获取错误信息

### 问题：权限错误
- 确保 Python 和项目文件有适当的执行权限
- 在 macOS 上可能需要在安全设置中允许 Python 访问系统信息

## 进阶配置

如果您想添加更多工具，可以：

1. 在 `tool.py` 中添加新的函数
2. 在 `main.py` 中使用 `mcp.add_tool()` 或 `@mcp.tool()` 装饰器注册新工具
3. 重启 Cursor 使新工具生效

## 注意事项

- 确保使用绝对路径以避免路径解析问题
- 定期更新依赖以获得最新功能和安全修复
- 如果移动项目目录，需要更新 Cursor 配置中的路径 