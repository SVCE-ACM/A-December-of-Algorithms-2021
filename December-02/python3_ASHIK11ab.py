def sum_of_squares_digits(number):
  digits_sum = 0
  while number != 0:
    digit = number % 10
    digits_sum += digit**2
    number = number // 10
  return digits_sum

def main():
  num = int(input("n = "))
  # List of numbers for which sum of squares of digits
  # is calculated. Used to find occurrence of cycle.
  calculated = []
  while num != 1:
    calc_sum = sum_of_squares_digits(num)
    # Checking for cycle.
    if calc_sum in calculated:
      print("NO")
      return
    else:
      calculated.append(calc_sum)
    num = calc_sum
  print("YES")


if __name__ == "__main__":
  main()