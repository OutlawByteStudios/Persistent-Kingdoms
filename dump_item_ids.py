#!/usr/bin/python -tt

from module_items import *
import argparse
import json

parser = argparse.ArgumentParser(description="Dump item ids with names, for use with the administrator items tool.")
parser.add_argument("output_format", choices=["txt", "json"])
parser.add_argument("output_file", nargs='?', default="admin_item_ids", help="file name without extension")
args = parser.parse_args()

if args.output_format == "txt":
  with open(args.output_file + ".txt", "w") as f:
    for i, item in enumerate(items):
      if (item[1].startswith("INVALID") or "Banner" in item[1]):
        continue
      elif (item[0] == "all_items_end"):
        break
      f.write("{0:3} = {1} ({2})\n".format(i, item[1], item[0]))

elif args.output_format == "json":
  output_items = []

  for i, item in enumerate(items):
    if (item[1].startswith("INVALID") or "Banner" in item[1]):
      continue
    elif (item[0] == "all_items_end"):
      break

    output_items.append({
      "itemID": i,
      "itemName": item[1],
      "itemTextId": item[0]
    })

    with open(args.output_file + ".json", "w") as f:
      f.write(json.dumps(output_items, sort_keys=True, indent=4, separators=(',', ': ')))
