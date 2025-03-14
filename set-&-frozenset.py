# Set (Mutable, Unordered, No Duplicates)
numbers = {1, 2, 3, 4, 4, 5}
numbers.add(6)
print(numbers)  # {1, 2, 3, 4, 5, 6}

# Frozenset (Immutable Set)
frozen_numbers = frozenset({10, 20, 30, 40})
# frozen_numbers.add(50)  # This will raise an error
print(frozen_numbers)  # frozenset({10, 20, 30, 40})
