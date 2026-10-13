from dotenv import load_dotenv
import os
from openai import OpenAI
from agent import chat_with_tools

load_dotenv()


def main():
    api_key = os.environ.get("API_KEY")
    base_url = os.environ.get("BASE_URL")
    model = os.environ.get("MODEL")
    if not api_key:
        raise ValueError("未找到 API_KEY，请在 .env 文件中配置。")
    if not base_url:
        raise ValueError("未找到 BASE_URL，请在 .env 文件中配置。")
    if not model:
        raise ValueError("未找到 MODEL，请在 .env 文件中配置。")

    client = OpenAI(api_key=api_key, base_url=base_url)

    while True:
        try:
            user_input = input("\n[你] ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\n再见！")
            break

        if not user_input:
            continue

        if user_input.lower() in ("exit", "quit"):
            print("再见！")
            break

        print("\n\n")
        print("*" * 60)
        print(f"User>\t {user_input}")
        print("*" * 60)

        answer = chat_with_tools(client, user_input, model)

        print("\n\n")
        print("=" * 60)
        print(f"Assistant>\t {answer}")
        print("*" * 60)
        print(f"\n[助手] {answer}\n{'─' * 60}\n")

if __name__ == "__main__":
    main()
