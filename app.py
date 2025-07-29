import asyncio
import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from mcp_use import MCPAgent, MCPClient,MCPSession

async def run_memory_chat():
    load_dotenv()
    os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")

    config_file = "browser_mcp.json"
    print("Starting browser automation...")

    client = MCPClient.from_config_file(config_file)
    llm = ChatGroq(model="qwen/qwen3-32b")
    agent = MCPAgent(llm=llm, client=client, max_steps=15, memory_enabled=True)
    print("Agent created")

    try:
        while True:
            user_input = input("Enter your message: ")
            if user_input.lower() in ["exit", "quit", "bye"]:
                print("Ending the chat")
                break
            if user_input.lower() in ["clear", "reset"]:
                agent.clear_conversation_history()
                print("Conversation history cleared")
                continue

            print("\nAssistant:", end="", flush=True)
            try:
                response = await agent.run(user_input)
                print(response)
            except Exception as e:
                print(f"Error: {e}")
    except KeyboardInterrupt:
        print("\nKeyboard interrupt detected. Exiting...")
    finally:
        if client and client.Session:
            await client.close_all_sessions()
            print("All sessions closed")

if __name__ == "__main__":
    asyncio.run(run_memory_chat())
