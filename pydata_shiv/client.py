import asyncio

from grpclib.client import Channel

from .prediction_pb2 import PredictionRequest, Prediction
from .prediction_grpc import PredictionServiceStub


async def run():
    loop = asyncio.get_event_loop()
    channel = Channel('127.0.0.1', 50051, loop=loop)
    stub = PredictionServiceStub(channel)

    while(True):
        try:
            response = await stub.Predict(PredictionRequest(text='Contract text'), timeout=2)
            print(Prediction.Label.Name(response.label), response.confidence)
        except asyncio.TimeoutError:
            print('Timed out')
      
def main_entrypoint():
    asyncio.run(run())

if __name__ == '__main__':
    main_entrypoint()
    
