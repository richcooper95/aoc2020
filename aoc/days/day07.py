from typing import List, Tuple
from collections import defaultdict

from .. import utils

__all__ = ("main")


@utils.display
def process(lines: List[str]) -> Tuple[int]:
  capacity_map = dict() # map a bag to the bags it can contain
  container_map = defaultdict(set) # map a bag to the bags which can contain it

  for line in lines:
    # TODO: improve error handling of badly-formatted entries here
    bag, bag_info = line.split(" bags contain ")
    if "no other" in bag_info:
      # set value to empty list to allow common treatment during later walk
      capacity_map[bag] = []
    else:
      # set the value to a list of tuples containing the count and bag type for
      # all bags it can contain
      capacity_map[bag] = [
        (int(elem[0]), elem[2:elem.index(" bag")])
        for elem in bag_info.split(", ")
      ]
      # add the bag to the entries for all contained bags in the container map
      for b in capacity_map[bag]:
        container_map[b[1]].add(bag)
  
  def _walk_containers(_bag: str):
    containers = set()
    for container in container_map[_bag]:
      containers.add(container)
      containers.update(_walk_containers(container))
    return containers

  def _walk_contained(_bag: str):
    num_bags = 0
    for inner_bag in capacity_map[_bag]:
      num_bags += inner_bag[0]*(1 + _walk_contained(inner_bag[1]))
    return num_bags

  return len(_walk_containers("shiny gold")), _walk_contained("shiny gold")
  

#---------------------------------------------------

def main() -> None:
  process(utils.get_input_list(__name__)) # 213, 38426


if __name__ == "__main__":
  main()
