#!/usr/bin/python -tt

from module_items import *
from module_scene_props import *
from module_skills import *
import process_operations as po
import argparse

parser = argparse.ArgumentParser(description="Dump crafting recipes to a file.")
parser.add_argument("output_format", choices=["txt", "xml", "bal", "csv"])
parser.add_argument("output_file", nargs='?', default="crafting_recipes", help="file name without extension")
parser.add_argument("--pretty", "-p", action="store_true", help="pretty print xml output with newlines and indentation")
args = parser.parse_args()

id_map = po.IdentifierMap()
id_map.load_ids("itm", items, 0)
id_map.load_ids("skl", skills, 0)

def get_id(id_str):
  s = id_str.partition("_")
  return id_map.get_id(s[0], s[2])

class CraftingRecipe:
  pass

class ItemInfo:
  pass

item_craft_times = [None] * len(items)
for scene_prop in scene_props:
  if (len(scene_prop[4]) >= 3 and scene_prop[4][0][0] == ti_on_scene_prop_init and scene_prop[4][1][0] == ti_on_scene_prop_cancel_use and
      scene_prop[4][0][1][1][0] == scene_prop_set_slot and scene_prop[4][0][1][1][2] == slot_scene_prop_item_id):
    item_craft_times[get_id(scene_prop[4][0][1][1][3])] = get_spr_use_time(scene_prop[1])

crafting_recipes = []
for entry in crafting_data:
  item_id = get_id(entry[0])
  item = items[item_id]
  item_info = ItemInfo()
  item_info.identifier = item[0]
  item_info.name = item[1]
  item_info.mesh = item[2][0][0]
  item_info.price = item[5]
  item_info.weight = get_weight(item[6])
  item_info.difficulty = item_difficulties_list[item_id]
  item_info.head_armor = get_head_armor(item[6])
  item_info.body_armor = get_body_armor(item[6])
  item_info.leg_armor = get_leg_armor(item[6])
  item_info.speed = get_speed_rating(item[6])
  item_info.missile_speed = get_missile_speed(item[6])
  item_info.length = item_lengths_list[item_id]
  item_info.swing_damage = get_damage_str(get_swing_damage(item[6]))
  item_info.thrust_damage = get_damage_str(get_thrust_damage(item[6]))

  item_type = item[3] & 0xff
  if item[0] in ("saddle", "horse_armor", "small_mining_pick", "woodcutter_axe", "mining_pick", "repair_hammer",
    "lock_pick", "bucket", "fishing_spear", "fishing_net", "sickle", "scythe", "kitchen_knife",
    "cleaver", "knife", "butchering_knife", "broom", "herding_crook", "surgeon_scalpel", "torch",
    "book_a", "book_b", "book_c", "book_d", "book_e", "book_f", "lyre", "lute", "warhorn", "dart", "die", "wheat_sack"):
    item_info.type = "Tools & Misc"
  elif item_type in (itp_type_bow, itp_type_crossbow, itp_type_thrown, itp_type_arrows, itp_type_bolts):
    item_info.type = "Ranged Weapons & Ammo"
  elif item_type == itp_type_shield:
    item_info.type = "Shields"
  elif  item_type in (itp_type_one_handed_wpn, itp_type_two_handed_wpn, itp_type_polearm):
    item_info.type = "Melee Weapons"
  elif item_type == itp_type_horse:
    item_info.type = "Horses"
  elif item_type in (itp_type_head_armor, itp_type_body_armor, itp_type_foot_armor, itp_type_hand_armor):
    item_info.type = "Armour"
  else:
    print (item[1])

  recipe = CraftingRecipe()
  recipe.crafted_item = item_info
  recipe.skill_names = [skills[get_id(entry[1][i][0])][1] if entry[1][i][0] != -1 else "None" for i in xrange(2)]
  recipe.skill_levels = [entry[1][i][1] for i in xrange(2)]
  recipe.resources_default_cost = 0
  recipe.resource_names = []
  recipe.resource_ids=[]
  for resource in entry[3]:
    if resource == -1:
      continue
    item = items[get_id(resource)]
    recipe.resources_default_cost += item[5]
    recipe.resource_ids.append(item[0])
    recipe.resource_names.append(item[1])
  recipe.average_skill_level = entry[4]
  recipe.max_crafting_reward = (recipe.resources_default_cost +
    (recipe.average_skill_level * craft_skill_gold_reward_multiplier) +
    ((recipe.crafted_item.price * craft_price_gold_reward_percentage) / 100))
  recipe.time = item_craft_times[item_id]
  crafting_recipes.append(recipe)

if args.output_format == "txt":

  with open(args.output_file + ".txt","w") as f:
    for recipe in crafting_recipes:
      skill_list = "None"
      if recipe.skill_names[0] != "None" and recipe.skill_levels[0] > 0:
        skill_list = [recipe.skill_names[0], str(recipe.skill_levels[0])]
        if recipe.skill_names[1] != "None" and recipe.skill_levels[1] > 0:
          skill_list.extend(["/", recipe.skill_names[1], str(recipe.skill_levels[1])])
      f.write("{0:30} {1:25} Time: {2:2} {3}\n".format(recipe.crafted_item.name, ' '.join(skill_list), recipe.time, ', '.join(recipe.resource_names)))

elif args.output_format == "xml":

  import xml.etree.cElementTree as ET
  root = ET.Element("crafting_recipies")
  for recipe in crafting_recipes:
    entry = ET.SubElement(root, "recipe")
    ET.SubElement(entry, "identifier").text = recipe.crafted_item.identifier
    ET.SubElement(entry, "name").text = recipe.crafted_item.name
    ET.SubElement(entry, "mesh").text = recipe.crafted_item.mesh
    ET.SubElement(entry, "price").text = str(recipe.crafted_item.price)
    ET.SubElement(entry, "weight").text = str(recipe.crafted_item.weight)
    ET.SubElement(entry, "difficulty").text = str(recipe.crafted_item.difficulty)
    ET.SubElement(entry, "head_armor").text = str(recipe.crafted_item.head_armor)
    ET.SubElement(entry, "body_armor").text = str(recipe.crafted_item.body_armor)
    ET.SubElement(entry, "leg_armor").text = str(recipe.crafted_item.leg_armor)
    ET.SubElement(entry, "speed").text = str(recipe.crafted_item.speed)
    ET.SubElement(entry, "missile_speed").text = str(recipe.crafted_item.missile_speed)
    ET.SubElement(entry, "length").text = str(recipe.crafted_item.length)
    ET.SubElement(entry, "swing_damage").text = str(recipe.crafted_item.swing_damage)
    ET.SubElement(entry, "thrust_damage").text = str(recipe.crafted_item.thrust_damage)
    temp_skill_list = []
    for name, level in zip(recipe.skill_names, recipe.skill_levels):
      if level <= 0:
        continue
      temp_skill_list.append(name + " " + `level`)
    ET.SubElement(entry, "crafting_skills").text = " / ".join(temp_skill_list) 
    ET.SubElement(entry, "average_skill_level").text = str(recipe.average_skill_level)
    for idx, resource_name in enumerate(recipe.resource_names):
      ET.SubElement(entry, "crafting_resource_" + `idx + 1`).text = resource_name
    ET.SubElement(entry, "resources_default_cost").text = str(recipe.resources_default_cost)
    ET.SubElement(entry, "max_crafting_reward").text = str(recipe.max_crafting_reward)
    ET.SubElement(entry, "time").text = str(recipe.time)
  tree = ET.ElementTree(root)

  def indent(elem, level=0):
    i = "\n" + level*"  "
    if len(elem):
      if not elem.text or not elem.text.strip():
        elem.text = i + "  "
      if not elem.tail or not elem.tail.strip():
        elem.tail = i
      for elem in elem:
        indent(elem, level+1)
      if not elem.tail or not elem.tail.strip():
        elem.tail = i
    else:
      if level and (not elem.tail or not elem.tail.strip()):
        elem.tail = i

  if args.pretty:
    indent(tree.getroot())
  tree.write(args.output_file + ".xml")

elif args.output_format == "bal":

  with open(args.output_file + ".txt","w") as f:
    for recipe in crafting_recipes:
      f.write("%30s T %-2d S %1d P %-5s RC %-4d MR %-5d P/MR %5.2f MR/RC %5.2f P/RC %5.2f MR/(RC*T) %5.2f DR %d\n" % (
        recipe.crafted_item.identifier, recipe.time, recipe.average_skill_level,
        recipe.crafted_item.price, recipe.resources_default_cost, recipe.max_crafting_reward,
        recipe.crafted_item.price / float(recipe.max_crafting_reward),
        recipe.max_crafting_reward / float(recipe.resources_default_cost),
        recipe.crafted_item.price / float(recipe.resources_default_cost),
        recipe.max_crafting_reward / float(recipe.resources_default_cost * recipe.time),
        len(set(recipe.resource_names))))

elif args.output_format == "csv":

  with open(args.output_file + ".csv","w") as f:
    f.write("Type,Item Name,Required Skill(s),Resource 1,Resource 2,Resource 3,Resource 4,Price,Difficulty,Head Armour,Body Armour,Leg Armour,Speed,Swing Damage,Thrust Damage\n")
    for recipe in crafting_recipes:
      f.write("%s,%s," % (recipe.crafted_item.type,recipe.crafted_item.name))
      temp_skill_list = []
      for name, level in zip(recipe.skill_names, recipe.skill_levels):
        if level <= 0:
          continue
        temp_skill_list.append(name + " " + `level`)
      f.write("%s," % (" / ".join(temp_skill_list)))
      for x in range(0, 4):
        f.write("%s," % (("wp-content/uploads/2018/05/" + recipe.resource_ids[x] + ".png") if -len(recipe.resource_names) <= x < len(recipe.resource_names) else ""))
      f.write("%s,%s,%s,%s,%s,%s,%s,%s" % (
        str(recipe.crafted_item.price),
        str(recipe.crafted_item.difficulty),
        str(recipe.crafted_item.head_armor),
        str(recipe.crafted_item.body_armor),
        str(recipe.crafted_item.leg_armor),
        str(recipe.crafted_item.speed),
        str(recipe.crafted_item.swing_damage),
        str(recipe.crafted_item.thrust_damage),
        ))  
      f.write("\n")
