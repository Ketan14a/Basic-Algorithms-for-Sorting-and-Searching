from math import log10


def get_digit(number, base, pos):
  return (number // base ** pos) % base

def prefix_sum(array):
  for i in range(1, len(array)):
    array[i] = array[i] + array[i-1]
  return array

def radixsort(l, base=10):
  passes = int(log10(max(l))+1)
  output = [0] * len(l)

  for pos in range(passes):
    count = [0] * base

    for i in l:
      digit = get_digit(i, base, pos)
      count[digit] +=1

    count = prefix_sum(count)

    for i in reversed(l):
      digit = get_digit(i, base, pos)
      count[digit] -= 1
      new_pos = count[digit]
      output[new_pos] = i

    l = list(output)
  return output

data = []

n = int(input("Enter the number of elements to be sorted:"))

print("Enter %s numbers in randomly sorted order:" % str(n))
for i in range(n):
    data.append(int(input()))

sorted = radixsort(data)


print("The sorted list is as follows:-")

for i in range(n):
    print(sorted[i])

