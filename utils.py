def most_frequent(arr, n):
  maxCount = 0
  element_having_max_freq = 0
  for i in range(0, n):
    count = 0
    for j in range(0, n):
      if(arr[i] == arr[j]):
        count += 1
    if(count > maxCount):
      maxCount = count
      element_having_max_freq = arr[i]

  return element_having_max_freq