# from python_phoenix_miner import PhoenixClient
from src.python_phoenix_miner.phoenix_client import PhoenixClient

miner_name = "Miner 01"
ip = '192.168.1.89'
port = 3333

client = PhoenixClient(miner_name="miner01", ip=ip, port=port)

# basic_miner_stats = client.Miner.get_stats()
extended_miner_stats = client.Miner.get_extended_stats()
print(extended_miner_stats.to_json())
print("Done")
