def find_intersection(necklase_A, necklase_B):
  candidate_stones = ""
  # Maintain small string as first for performing intersection.
  if len(necklase_A) > len(necklase_B):
    (necklase_A, necklase_B) = (necklase_B[:], necklase_A[:])

  for stone in necklase_A:
    if stone in necklase_B and stone not in candidate_stones:
      candidate_stones += stone
  return candidate_stones

def get_input():
  """ Parses the string input and returns list of necklases. """
  arr = input("arr = ")
  arr = arr[1:len(arr)-1]
  arr = arr.replace(' ', '').split(',')
  arr = [ele[1:len(ele)-1] for ele in arr]
  return arr

def main():
  necklases = get_input()
  facelifts = ""
  index = 0
  while index < len(necklases) - 1:
    facelifts = find_intersection(necklases[index], necklases[index+1])
    if len(facelifts) < 0:
      break
    index += 1
  print(len(facelifts))


if __name__ == "__main__":
  main()