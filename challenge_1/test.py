test_list =  list(range(0, 10, 2))

print(enumerate(test_list))
for index, num in enumerate(test_list):
    print(f"index: {index}, num: {num}")

# Test