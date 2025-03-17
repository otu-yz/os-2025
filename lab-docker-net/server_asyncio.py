import asyncio, helpers

# Define asynchronous coroutines
# to talk to multiple clients asynchronously (concurrently)
async def handle_client(reader, writer):
    # get address of client on the other end of this connection
    addr = writer.get_extra_info('peername')
    print('Connected to {}'.format(addr))
    while True:
        data = await reader.read(4096)
        if not data:
            break
        elif data.endswith(b'?'):
            reply = helpers.make_reply(data)
            writer.write(reply) 
            await writer.drain()
        else:
            print("Got incomplete question {} from {}".format(data, addr))
            break
    writer.close()
        
if __name__ == '__main__':
    addr = helpers.get_address()
    loop = asyncio.get_event_loop()
    coroutine = asyncio.start_server(handle_client, *addr)
    result = loop.run_until_complete(coroutine)
    print('Listening for incoming connections at {}'.format(addr))
    try:
        loop.run_forever()
    finally:
        server.close()
        loop.close()


