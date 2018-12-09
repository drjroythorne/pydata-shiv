import asyncio

from grpclib.client import Channel

from .larry_pb2 import LarryPredictionRequest, LarryPrediction
from .larry_grpc import LarryProcessorStub


async def main():
    loop = asyncio.get_event_loop()
    channel = Channel('127.0.0.1', 50051, loop=loop)
    stub = LarryProcessorStub(channel)

    while(True):
        try:
            response = await stub.Predict(LarryPredictionRequest(text='Contract text'), timeout=4)
            print(LarryPrediction.LarryLabel.Name(response.label), response.confidence)
        except asyncio.TimeoutError:
            print('Timed out')
        
if __name__ == '__main__':
    asyncio.run(main())
