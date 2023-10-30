def recusia_max(numbers):
  if len(numbers) == 1:
    return numbers [0]
  else:
      new_lst = recusia_max(numbers[1:])
      if numbers[0] > new_lst:
        return numbers[0]
      else:
        return new_lst


  

print(recusia_max([1,2,3]))

