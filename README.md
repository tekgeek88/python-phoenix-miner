
# python-phoenix-miner

## What it is

An API Wrapper for the Phoenix miner RPC socket client API

## How to use it
```
from python_phoenix_miner import PhoenixClient

miner_name = "Miner 01"
ip = '192.168.1.1'
port = 3333

client = PhoenixClient(miner_name="miner01", ip=ip, port=port)

basic_miner_stats = client.Miner.get_stats()
extended_miner_stats = client.Miner.get_extended_stats()
print("Done")
```

## The latest version

The current version of this program is written for Python 3.8

## Licensing

Copyright 2021 Carl Argabright

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.

## Contact
carl.argbright@gmail.com
