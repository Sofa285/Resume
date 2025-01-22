'''from websocket import create_connection

wss = create_connection("wss://dev.bubbling.ru?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJfaWQiOiI2NzA5M2FmNjYxYjgxZTM1NTUyYjZmOTgiLCJyb2xlcyI6WyJ1c2VyIl0sImlhdCI6MTczNzUzNzQxMywiZXhwIjoxNzM3NTQxMDEzfQ.pZZ3KriOjElTUnOUDARCIe9xqx4ZmXJoHODSon3JPqM&EIO=4&transport=websocket.")

while True:
    msg = input('Enter a message: ')
    if msg == 'quit':        
        wss.close()
        break
    wss.send(msg)
    result =  wss.recv()
    print ('> ', result)'''

import asyncio
import websockets

async def main():
    async with websockets.connect("wss://dev.bubbling.ru?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJfaWQiOiI2NzA5M2FmNjYxYjgxZTM1NTUyYjZmOTgiLCJyb2xlcyI6WyJ1c2VyIl0sImlhdCI6MTczNzUzODI1MCwiZXhwIjoxNzM3NTQxODUwfQ.eqLwLmk2_5Zb9z3e436FPXC7GwWd2nm-yWcWreP5LFQ&EIO=4&transport=websocket.") as wss:
        while True:
            msg = input('Enter a message: ')          
            if msg == 'quit':        
                wss.close()
                break
            await wss.send(msg)
            result =  await wss.recv()
            print('> ', result)
asyncio.run(main())