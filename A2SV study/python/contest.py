list_of_numbers = [2,3,9,2,9]

#This function will count the number of inversions in 
# the given list of numbers
def count_inversions(list_of_numbers): 
  inversion_count = 0

  #Looping through the list with two for loops
  for i in range(len(list_of_numbers)): 
    for j in range(i+1, len(list_of_numbers)): 
        
      # This checks whethuer the values of two consecutive numbers 
      #   are in the wrong order
      if list_of_numbers[i] > list_of_numbers[j]: 
        inversion_count += 1 
        
  #Returning the total count
  return inversion_count 

#Calling the inversion count function and printing the result
result = count_inversions(list_of_numbers)
print(result)