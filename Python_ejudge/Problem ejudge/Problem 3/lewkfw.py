x = (5, 4, 4, 6, 'f')

# Filter out non-integer elements from the tuple
integer_values = tuple(element for element in x if isinstance(element, int))

# Find the minimum value among the integers
min_value = min(integer_values)
print(min_value)