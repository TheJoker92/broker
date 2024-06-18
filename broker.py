import asyncio
from hbmqtt.broker import Broker
import yaml

with open('broker_config.yml', 'r') as f:
    config = yaml.safe_load(f)

broker = Broker(config)

async def start_broker():
    await broker.start()

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(start_broker())
    loop.run_forever()
