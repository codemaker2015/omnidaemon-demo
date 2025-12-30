import asyncio
from omnidaemon import OmniDaemonSDK
from omnidaemon import AgentConfig

sdk = OmniDaemonSDK()

async def greeter(message: dict):
    """Your AI agent runs here!"""
    name = message.get("content", {}).get("name", "stranger")
    return {"reply": f"Hello, {name}! 👋"}

async def main():
    await sdk.register_agent(
        agent_config=AgentConfig(
            topic="greet.user",
            callback=greeter,
        )
    )
    await sdk.start()
    print("🎧 Agent running. Press Ctrl+C to stop.")
    
    try:
        while True:
            await asyncio.sleep(1)
    except KeyboardInterrupt:
        pass
    finally:
        await sdk.shutdown()

if __name__ == "__main__":
    asyncio.run(main())