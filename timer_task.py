import asyncio

# https://stackoverflow.com/questions/45419723/python-timer-with-asyncio-coroutine

class Timer_Task:

    def __init__(self, interval, timer_name, context, callback):
        self._interval = interval
        self._name = timer_name
        self._context = context
        self._callback = callback
        self._ok = False
        self._task = None
        print(timer_name + " init done")

    async def start(self):
        self._ok = True
        while self._ok:
            await asyncio.sleep(self._interval)
            self._callback(self._context, self)

    def cancel(self):
        self._ok = False
        if self._task:
            self._task.cancel()
        print(self._name + "::cancel")


def some_callback_1(context, timer):
    context['count'] += 1
    print('callback: ' + timer._name + ", count: " + str(context['count']))

###########################################################################

timer1 = Timer_Task(interval=1, timer_name="Timer_1", context={'count': 0}, callback=some_callback_1)

if __name__ == '__main__':
    
    loop = asyncio.get_event_loop()
    timer1._task = loop.create_task(timer1.start())

    try:
        print('>>>')
        loop.run_forever()
        print('<<<')
    except KeyboardInterrupt:
        timer1.cancel()
        print("clean up done")
