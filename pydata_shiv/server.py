import asyncio

from grpclib.server import Server

from .larry_pb2 import LarryPrediction
from .larry_grpc import LarryProcessorBase

from time import sleep
from random import random

def prediction(request):
    sleep(5*random())
    return LarryPrediction(label=LarryPrediction.YES, confidence=0.5)

class LarryProcessor(LarryProcessorBase):

    async def Predict(self, stream):
        request = await stream.recv_message()
        await stream.send_message(prediction(request))


async def serve(server, *, host='127.0.0.1', port=50051):
    await server.start(host, port)
    print('Serving on {}:{}'.format(host, port))
    try:
        await server.wait_closed()
    except asyncio.CancelledError:
        server.close()
        await server.wait_closed()


async def main():
    server = Server([LarryProcessor()], loop=asyncio.get_event_loop())
    await serve(server)

def main_entrypoint():
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        pass
    

if __name__ == '__main__':
    main_entrypoint()
