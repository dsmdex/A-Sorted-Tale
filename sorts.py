import random  # Needed to randomly choose a pivot for quicksort

# ----------------------------
# Bubble Sort Implementation
# ----------------------------
def bubble_sort(arr, comparison_function):
  # Keep track of how many swaps occur (just for display)
  swaps = 0

  # This flag will be used to control the while loop
  sorted = False

  # Continue looping until the list is sorted (i.e., no swaps needed in a full pass)
  while not sorted:
    sorted = True  # Assume it's sorted unless we find a pair that needs swapping

    # Loop over each adjacent pair in the list
    for idx in range(len(arr) - 1):
      # Compare the current element and the next one
      # If they are out of order based on the comparison_function, we swap them
      if comparison_function(arr[idx], arr[idx + 1]):
        # Since we found a swap, the list wasn't fully sorted
        sorted = False

        # Swap the elements
        arr[idx], arr[idx + 1] = arr[idx + 1], arr[idx]

        # Count the swap for stats
        swaps += 1

  # Print total number of swaps performed
  print("Bubble sort: There were {0} swaps".format(swaps))

  # Return the now-sorted array
  return arr

# -----------------------------------
# Quicksort Implementation (Recursive)
# -----------------------------------
def quicksort(list, start, end, comparison_function):
  # Base case: if the list has one or zero elements in this slice, do nothing
  if start >= end:
    return

  # Pick a random index between start and end to use as pivot
  pivot_idx = random.randrange(start, end + 1)
  pivot_element = list[pivot_idx]

  # Move the pivot to the end for easier partitioning
  list[end], list[pivot_idx] = list[pivot_idx], list[end]

  # This pointer keeps track of where the "less-than" region ends
  less_than_pointer = start

  # Partition step: move elements less than the pivot to the left
  for i in range(start, end):  # Exclude the end index because that's now the pivot
    # If current element should go before pivot (based on the comparison function),
    # move it to the front of the list (within the "less than" region)
    if comparison_function(pivot_element, list[i]):
      # Swap current element with the one at less_than_pointer
      list[i], list[less_than_pointer] = list[less_than_pointer], list[i]

      # Move the less_than_pointer forward (expanding the "less than" region)
      less_than_pointer += 1

  # Finally, move the pivot element to its final sorted position
  list[end], list[less_than_pointer] = list[less_than_pointer], list[end]

  # Recursively sort the two partitions (left and right of the pivot)
  quicksort(list, start, less_than_pointer - 1, comparison_function)      # Left side
  quicksort(list, less_than_pointer + 1, end, comparison_function)        # Right side
