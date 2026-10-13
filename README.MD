# 目录结构
```text
agent-function-call/
├── main.py                  # 入口：控制台交互循环
├── agent.py                 # Function Calling 编排（工具执行 + 对话循环），System Prompt 定义
├── llm.py                   # LLM 调用封装（API 请求 + JSON 日志）
├── tools/
│   ├── __init__.py          # 工具注册中心（TOOL_HANDLERS + TOOLS）
│   ├── revstr.py            # 工具：反转字符串
│   └── calculator.py        # 工具：四则运算
├── .env.example             # 环境变量模板
└── README.md
└── requirements.txt         # 项目依赖
```

# 配置apiKey
```bash
cp .env.example .env
```

# 运行
```bash
pip install -r requirements.txt
```

````bash
python main.py
````


# 测试
```text
191911加上202588191等于多少
```

```text
反转下面字符串: linyerun
```