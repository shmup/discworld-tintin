#!/usr/bin/env python3

import json
import time
import curses

filepath = 'store.json'
interval = 0.1
highlight_duration = 1
ignore_keys = ['last_room_key', 'capname', 'login', 'role', 'room_identifier']


def read_json_file(filepath):
  with open(filepath, 'r') as file:
    return json.load(file)


def compare_json(old_data, new_data):
  return {
      key: value
      for key, value in new_data.items()
      if old_data.get(key) != value and key not in ignore_keys
  }


def render_screen(stdscr, data, changes):
  sorted_keys = [key for key in sorted(data) if key not in ignore_keys]
  max_length = max(len(f"{key}: {data[key]}") for key in sorted_keys) + 1

  for idx, key in enumerate(sorted_keys):
    line = f"{key}: {data[key]}".ljust(max_length)
    stdscr.addstr(idx, 0, line, curses.color_pair(1) if key in changes else 0)

  stdscr.clrtobot()
  stdscr.refresh()


def monitor_json(filepath, interval):
  curses.wrapper(main, filepath, interval)


def main(stdscr, filepath, interval):
  curses.curs_set(0)
  stdscr.nodelay(True)
  curses.start_color()
  curses.init_pair(1, curses.COLOR_YELLOW, curses.COLOR_BLACK)

  old_data = read_json_file(filepath)
  render_screen(stdscr, old_data, {})
  while True:
    if stdscr.getch() == ord('q'):
      break
    time.sleep(interval)
    new_data = read_json_file(filepath)
    changes = compare_json(old_data, new_data)
    render_screen(stdscr, new_data, changes)
    if changes:
      time.sleep(highlight_duration)
      render_screen(stdscr, new_data, {})
    old_data = new_data


if __name__ == "__main__":
  monitor_json(filepath, interval)
