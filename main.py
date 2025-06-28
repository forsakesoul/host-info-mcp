from mcp.server.fastmcp import FastMCP
import tool

# {{CHENGQI:
# Action: Modified
# Timestamp: 2025-01-27 16:30:00 +08:00
# Reason: 优化MCP服务器配置，改进工具描述以便Cursor AI更好地理解何时调用系统信息工具
# Principle_Applied: KISS - 保持配置简洁明了，DRY - 复用现有工具模块
# Optimization: 改进服务器名称和工具描述，使AI助手更容易识别和调用
# Architectural_Note (AR): MCP服务器架构保持不变，仅优化配置参数
# Documentation_Note (DW): 相关使用文档需要更新以反映新的配置
# }}

# 创建MCP服务器实例，使用更清晰的名称
mcp = FastMCP("host-info-mcp")

# 添加主机信息工具 - 从tool.py导入
mcp.add_tool(tool.get_host_info)

@mcp.tool()
def get_system_info() -> str:
    """获取当前系统的详细信息，包括CPU数量、架构、内存等硬件信息
    
    当用户询问关于计算机硬件信息的问题时使用此工具，例如：
    - CPU数量和型号
    - 系统架构（x86_64, arm64等）
    - 内存大小
    - 操作系统版本
    - Python版本信息

    Returns:
        str: 包含完整系统信息的JSON字符串
    """
    return tool.get_host_info()

# 移除示例工具，保持服务器专注于系统信息功能
# @mcp.tool()
# def foo() -> str:
#     """foo
#     Returns:
#         str: A simple string.
#     """
#     return "foo"

def main() -> None:
    """启动MCP服务器主函数"""
    print("Starting host-info-mcp server...")
    print("Server provides system information tools for Cursor AI")
    mcp.run("stdio")

if __name__ == "__main__":
    main()