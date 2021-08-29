from python_phoenix_miner import PhoenixClient

miner_name = "Miner 01"
ip = '192.168.1.1'
port = 3333

client = PhoenixClient(miner_name="miner01", ip=ip, port=port)

basic_miner_stats = client.Miner.get_stats()
extended_miner_stats = client.Miner.get_extended_stats()
print("Done")
