# Function to find union of two arrays
def find_union(a, b):
    union_set = set(a) | set(b)
    return list(union_set)

# Example input
a = [1, 2, 3, 2, 1]
b = [3, 2, 2, 3, 3, 2]

# Function call
result = find_union(a, b)

print(sorted(result))
