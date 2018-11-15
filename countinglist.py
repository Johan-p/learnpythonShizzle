def count(sequence, item):
  result = 0
  for x in sequence:
    if x == item:
      result = result + 1
  return result