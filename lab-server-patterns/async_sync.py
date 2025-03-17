import asyncio
import time, sys

# regular functions to do network IO with two clients
def sync_netio(delay, addr):
	time.sleep(delay)
	print("talked to {}".format(addr))

def sync_main():
	print("begin at time {}".format(time.strftime('%X')))
	sync_netio(3, 'client 1')
	sync_netio(3, 'client 2')
	print("end at time {}".format(time.strftime('%X')))

# Define asynchronous coroutines
# to run the network IO to two clients asynchronously (concurrently)
async def async_netio(delay, addr):
	await asyncio.sleep(delay)
	print("talked to {}".format(addr))

async def async_main():
	client1 = asyncio.ensure_future(async_netio(3, 'client 1'))
	client2 = asyncio.ensure_future(async_netio(3, 'client 2'))
	print("begin at time {}".format(time.strftime('%X')))
	await client1
	await client2
	print("end at time {}".format(time.strftime('%X')))

if (sys.argv[1] == 'sync'):
	# run clients synchronously
	# this will take 6 seconds in total 
	sync_main()

elif (sys.argv[1] == 'async'):
	# now make them run asynchronously, i.e., concurrently
	# will only take 3 seconds
	loop = asyncio.get_event_loop()
	result = loop.run_until_complete(async_main())


