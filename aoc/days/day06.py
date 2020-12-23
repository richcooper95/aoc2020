from typing import List, Tuple

from .. import utils

__all__ = ("main")


@utils.display
def process(lines: List[str]) -> Tuple[int]:
  i = 0
  count_a = 0
  count_b = 0
  while i < len(lines):
    group = []
    while i < len(lines) and lines[i]:
      group.append(set(lines[i]))
      i += 1
    count_a += len(set.union(*group))
    count_b += len(set.intersection(*group))
    i += 1

  return count_a, count_b
  

#---------------------------------------------------

def main() -> None:
  process(utils.get_input_list(__name__)) # 6532, 3427


if __name__ == "__main__":
  main()
