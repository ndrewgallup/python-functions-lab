# 1
def sum_to(number):
  sum = 0
  for n in range(1, number + 1):
    sum += n
  return sum

print(sum_to(8))


# 2
arr = [1,2,3,4,0]
def largest(nums):
  nums.sort()
  return nums[-1]
print(largest(arr))


# 3
def occurrences(str, str1):
  count = 1
  for n in str:
    if n == str1:
      count += 1
      return count 
print(occurrences('woo wee', 'e'))


# 4 
def product(*args):
  product = 1
  for arg in args:
    product *= arg
  return product 
print(product(5, 3, -1))


