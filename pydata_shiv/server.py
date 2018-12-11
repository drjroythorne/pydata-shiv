import asyncio

from grpclib.server import Server

from .prediction_pb2 import Prediction
from .prediction_grpc import PredictionServiceBase

from time import sleep
from random import random


class ThePredictionService(PredictionServiceBase):

    async def Predict(self, stream):
        request = await stream.recv_message()
        await stream.send_message(self.prediction(request))

    def prediction(self, request):
        sleep(5*random())
        return Prediction(label=Prediction.YES, confidence=0.5)


async def serve(server, *, host='127.0.0.1', port=50051):
    await server.start(host, port)
    print('Serving on {}:{}'.format(host, port))
    try:
        await server.wait_closed()
    except asyncio.CancelledError:
        server.close()
        await server.wait_closed()


async def run():
    server = Server([ThePredictionService()], loop=asyncio.get_event_loop())
    await serve(server)

def main_entrypoint():
    try:
        asyncio.run(run())
    except KeyboardInterrupt:
        pass
    

if __name__ == '__main__':
    main_entrypoint()
