import asyncio

# https://stackoverflow.com/questions/45419723/python-timer-with-asyncio-coroutine

class TimerTask:

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

async def other_operation():
    # Ваш код для другой операции
    print("other_operation-1")
    await asyncio.sleep(10)
    print("other_operation-2")
    await asyncio.sleep(50)
    print("other_operation <<")

###########################################################################
timer_action = TimerTask(1, "Timer1", {'count': 0}, some_callback_1)


if __name__ == "__main__":
    loop = asyncio.get_event_loop()

    main_task = loop.create_task(timer_action.start())

    other_task = loop.create_task(other_operation())

    tasks = [main_task, other_task]

    try:
        loop.run_until_complete(asyncio.gather(*tasks))
        print("run_until_complete")
    except KeyboardInterrupt:
        timer_action.cancel()
        #loop.close()
        print("clean up done")
