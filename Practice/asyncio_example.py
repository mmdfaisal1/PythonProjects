import asyncio
counter = 0


async def func1():
    global counter

    while True:
        await asyncio.sleep(5)
        counter += 1
        counter -= 1
        # return counter
        print("Value of counter in func1:", counter)


async def func2():
    global counter

    while True:
        await asyncio.sleep(20)
        counter += 1
        counter -= 1
        print("Value of counter in func2:", counter)


values = asyncio.gather(func1(), func2())

# Note the result of Promise.all() is itself a promise, that you can wait on
# var output = Promise.all([promise1, promise2])
# output.then();

# OR

# Promise.all().then(() => {})
# data in

# data send
# processing
# wait for data to be sent






asyncio.get_event_loop().run_forever()






