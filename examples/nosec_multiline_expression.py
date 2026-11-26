import random

test_list_with_a_very_long_name = [1, 6, 3, 10, 21, 31, 50, 49, 20, 100]
a = random.sample(
    test_list_with_a_very_long_name,
    random.randint(0, len(test_list_with_a_very_long_name)),
)  # nosec
print(a)
