N = 4  # Example values for N, S, W, and E
S = 5
W = 4
E = 5

# Sort the list by values in reverse order
sorted_directions = sorted([['N', N], ['S', S], ['W', W], ['E', E]], key=lambda x: x[1], reverse=True)

# Find the highest value
highest_value = sorted_directions[0][1]

# Print the key(s) with the highest value(s)
highest_keys = []

for pair in sorted_directions:
    if pair[1] == highest_value:
        highest_keys.append(pair[0])

for key in highest_keys:
    print(key)
