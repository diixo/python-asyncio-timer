
import asyncio


async def hello_world():
    """An asynchronous function to print 'Hello World'"""
    await asyncio.sleep(3)
    print('Hello World')

# Create and run the event loop
async def main():
    # Schedule a call to hello_world()
    await hello_world()

# Run the event loop using asyncio.run()
asyncio.run(main())
