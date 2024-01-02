import asyncio

# https://stackoverflow.com/questions/45419723/python-timer-with-asyncio-coroutine

class Timer_Interval:
    def __init__(self, interval, timer_name, context, callback):
        self._interval = interval
        self._name = timer_name
        self._context = context
        self._callback = callback
        self._ok = True
        self._task = None
        print(timer_name + " init done")

    async def start(self):
        while self._ok:
            await asyncio.sleep(self._interval)
            await self._callback(self._name, self._context, self)

    async def _job(self):
        print(">>job")
        while self._ok:
            await asyncio.sleep(self._interval)
            await self._callback(self._name, self._context, self)

    def cancel(self):
        self._ok = False
        self._task.cancel()


async def some_callback_1(timer_name, context, timer):
    context['count'] += 1
    print('callback: ' + timer_name + ", count: " + str(context['count']))


timer1 = Timer_Interval(interval=1, timer_name="Timer_1", context={'count': 0}, callback=some_callback_1)

##########################
if __name__ == '__main__':
    
    loop = asyncio.get_event_loop()

    try:
        print('>>>')
        timer1._task = loop.create_task(timer1.start())
        loop.run_forever()
    except KeyboardInterrupt:
        timer1.cancel()
        print("clean up done")
