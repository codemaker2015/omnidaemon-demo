import asyncio
import json

async def test_messages():
    """Send test messages to the agent."""
    
    # Test cases
    tests = [
        ("greet.user", {"content": {"name": "World"}}),
        ("greet.user", {"content": {"name": "Alice"}}),
        ("greet.user", {"content": {}}),
        ("health.check", {"timestamp": "now"}),
    ]
    
    print("Testing agent messages...\n")
    
    for topic, message in tests:
        print(f"Topic: {topic}")
        print(f"Message: {json.dumps(message)}")
        
        # Simulate sending
        await asyncio.sleep(0.3)
        
        # Simulate response
        if topic == "greet.user":
            name = message.get("content", {}).get("name", "stranger")
            print(f"Response: Hello, {name}!\n")
        else:
            print("Response: {'status': 'healthy'}\n")
        
        await asyncio.sleep(0.5)
    
    print("Done!")

if __name__ == "__main__":
    asyncio.run(test_messages())