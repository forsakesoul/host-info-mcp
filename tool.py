import platform
# This script provides a function to check if the system is running on a virtual machine.
import psutil
import subprocess
import json

def get_host_info() -> str:
    """获取当前主机的详细系统信息
    
    此函数收集并返回当前计算机的完整硬件和软件信息，包括：
    - 操作系统类型和版本
    - CPU架构、型号和核心数量  
    - 内存总量
    - Python版本
    - 处理器详细信息
    
    适用于回答用户关于计算机配置的问题，如：
    "我的电脑有多少CPU？"、"什么架构？"、"内存多大？"等

    Returns:
        str: 包含主机信息的JSON格式字符串
    """

    info: dict[str, str] = {
        "system": platform.system(),
        "release": platform.release(),
        "machine": platform.machine(),
        "processor": platform.processor(),
        "python_version": platform.python_version(),
        "memory_gb": f"{psutil.virtual_memory().total / (1024 ** 3):.2f}",
        "os": platform.system()
    }

    cpu_count = psutil.cpu_count(logical=True)
    if cpu_count is not None:
        info["cpu_count"] = str(cpu_count)

    try:
        cpu_model = subprocess.check_output(
            ["sysctl", "-n", "machdep.cpu.brand_string"],
        ).decode().strip()
        info["cpu_model"] = cpu_model
    except (subprocess.CalledProcessError, FileNotFoundError):
        info["cpu_model"] = "Unknown"

    return json.dumps(info, indent=4)

if __name__ == "__main__":
    print(get_host_info())
