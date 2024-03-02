#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# this script will be called from tintin++ to parse ZMP events
# and store the data in a JSON file
# and should now also append the args to a log file

import sys
import json
from pathlib import Path

# Define the path to the JSON store file
store_path = Path("store.json")


def load_store():
  """Load the store from a JSON file, or initialize it if not present."""
  if store_path.exists():
    with open(store_path, 'r') as f:
      return json.load(f)
  else:
    return {}


def save_store(store):
  """Save the updated store back to the JSON file."""
  with open(store_path, 'w') as f:
    json.dump(store, f)


room_keys = ["identifier", "name", "visibility", "kind"]

def update_store(args):
  global last_room_key
  """Update the store based on passed arguments."""
  # Load or initialize the store
  store = load_store()

  if args[0] == "room":
    if args[1] in room_keys:
      store['last_room_key'] = args[1]
      save_store(store)
    elif store.get('last_room_key'):
      key = f"room_{store.get('last_room_key')}"
      store[key] = " ".join(args[1:])
      del store['last_room_key']
      save_store(store)
    return

  if (len(args) > 0):
    store[args[0]] = " ".join(args[1:])
    save_store(store)
  with open("log.txt", "a") as f:
    f.write(" ".join(args) + "\n")


if __name__ == "__main__":
  update_store(sys.argv[1:])
