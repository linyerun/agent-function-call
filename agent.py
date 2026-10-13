from tools import TOOL_HANDLERS
import json
from openai import OpenAI
from llm import call_llm, append_assistant

"""System prompt for the function-calling agent."""
SYSTEM_PROMPT = (
    "你是一个有用的助手，拥有两个工具：\n"
    "  • reverse_string：反转字符串\n"
    "  • basic_calculator：四则运算（add/subtract/multiply/divide）\n"
    "需要时调用工具，然后用自然语言回答用户。"
)


def _execute_tool(name: str, arguments: str) -> str:
    handler = TOOL_HANDLERS.get(name)
    if not handler:
        return f"ERROR: unknown tool '{name}'"
    try:
        args = json.loads(arguments or "{}")
        return str(handler(**args))
    except Exception as exc:
        return f"ERROR: {exc}"


def chat_with_tools(client: OpenAI, user_message: str, model: str) -> str:
    """单问题问答：最多 1 次工具调用 + 1 次最终生成。"""
    messages: list[dict] = [
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": user_message},
    ]

    # 调用模型
    msg = call_llm(client, messages, model)

    # 把模型回复填入messages中
    append_assistant(messages, msg)

    # 无工具调用直接返回
    if not msg.tool_calls:
        return msg.content or ""

    # 调用工具
    for tc in msg.tool_calls:
        result = _execute_tool(tc.function.name, tc.function.arguments)
        messages.append({"role": "tool", "tool_call_id": tc.id, "content": result})

    # 结合工具调用结果再次调用模型获取最值结果
    final_msg = call_llm(client, messages, model)
    print(f"Model>\t {final_msg.content or ''}")

    return final_msg.content or ""
