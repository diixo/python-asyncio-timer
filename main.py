
import asyncio

# https://stackoverflow.com/questions/45419723/python-timer-with-asyncio-coroutine

class Timer:
    def __init__(self, timeout, callback):
        self._timeout = timeout
        self._callback = callback
        self._task = None

    def create_job(self):
        self._task = asyncio.create_task(self._job())
        print('Timer::create_job')

    async def _job(self):
        await asyncio.sleep(self._timeout)
        await self._callback()

    def cancel(self):
        if self._task:
            self._task.cancel()

async def timeout_callback():
    await asyncio.sleep(0.1)
    print('echo!')

async def main():
    print('\nfirst example:')
    timer = Timer(2, timeout_callback)  # set timer for two seconds
    print('timer created')
    timer.create_job()

    print('\nsecond example:')
    timer = Timer(2, timeout_callback)  # set timer for two seconds
    timer.create_job()
    await asyncio.sleep(1)
    timer.cancel()                      # cancel it
    await asyncio.sleep(1.5)            # and wait to see it won't call callback

#########################
if __name__ == '__main__':
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    try:
        loop.run_until_complete(main())
    finally:
        loop.run_until_complete(loop.shutdown_asyncgens())
        loop.close()
