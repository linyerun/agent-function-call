"""工具注册中心 — 统一导出 TOOL_HANDLERS 与 TOOLS。"""

from tools.calculator import SCHEMA as _CALC_SCHEMA, basic_calculator
from tools.revstr import SCHEMA as _REV_SCHEMA, reverse_string

# 函数名 → 实现映射，供 agent 调用
TOOL_HANDLERS: dict = {
    "reverse_string": reverse_string,
    "basic_calculator": basic_calculator,
}

# OpenAI tools 参数列表
TOOLS: list[dict] = [_REV_SCHEMA, _CALC_SCHEMA]

__all__ = ["TOOL_HANDLERS", "TOOLS"]
