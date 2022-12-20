import asyncio
import json
import subprocess
import time
import regex

import nest_asyncio

from assets.assets_manager import AssetsManager
from disc_presence import Presence
from presences.ingame.reader_util import ScreenReader, TopBarReader
from riot_client import Client as RiotClient
from riot_client import resources as riot_client_resources
from presences.websocket_listener import WebsocketListener
from thread import Thread


class VRPCClient:
   def __init__(self) -> None:
      self.score_reader = TopBarReader(False, True)
      self.screen_reader = ScreenReader(self.score_reader)

      self.riot_client = RiotClient()
      self.riot_client.activate()
      self.riot_client.region = self.get_region()
      self.riot_client.shard = self.get_region()
      if self.riot_client.region in riot_client_resources.region_shard_override.keys():
         self.riot_client.shard = riot_client_resources.region_shard_override[self.riot_client.region]
      if self.riot_client.shard in riot_client_resources.shard_region_override.keys():
         self.riot_client.region = riot_client_resources.shard_region_override[self.riot_client.shard]
      self.riot_client.base_url, self.riot_client.base_url_glz, self.riot_client.base_url_shared = self.riot_client._build_urls()

      self.assets_manager = AssetsManager()

      self.presence = Presence()

      self.websocket = WebsocketListener(self)

   def get_region(self) -> str:
      val_proc_info = json.dumps(self.riot_client.riotclient_session_fetch_sessions())
      return regex.search('"-ares-deployment=(.*)", "-config-endpoint', val_proc_info).group(1)

   def loop(self) -> None:
      asyncio.run(self.websocket.start_loop())


if __name__ == '__main__':
   # required for stupid pypresence to work inside an already existing asyncio
   # loop. :(
   nest_asyncio.apply()

   presence_event_loop = asyncio.new_event_loop()

   def vrpc_loop() -> None:
      asyncio.set_event_loop(presence_event_loop)
      client = VRPCClient()
      client.loop()

   def process_exists(process_name: str) -> bool:
      progs = str(subprocess.check_output('tasklist'))
      if process_name in progs:
         return True
      else:
         return False

   thread = None

   while True:
      if process_exists('VALORANT'):
         if not thread:
            print('vrpc started')
            try:
               thread = Thread(vrpc_loop)
               thread.start()
            except:
               print('vrpc closed when attempting to start')
      else:
         if thread:
            thread.terminate()
            thread = None
            print('vrpc ended')

      time.sleep(8)