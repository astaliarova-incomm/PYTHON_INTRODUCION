import random

# Step 1: Create a list of random number of dicts (2 to 10)
list_of_dicts = []
for _ in range(random.randint(2, 10)):
    # Generate a random number of keys (letters) for each dict
    num_keys = random.randint(1, 5)
    keys = random.sample('abcdefghijklmnopqrstuvwxyz', num_keys)

    # Create a dictionary with random keys and values (0-100)
    new_dict = {key: random.randint(0, 100) for key in keys}
    list_of_dicts.append(new_dict)

# Print the generated list of dicts
print("List of dicts:")
print(list_of_dicts)

# Step 2: Create one common dict based on the rules specified
common_dict = {}
for i, d in enumerate(list_of_dicts, start=1):
    for key, value in d.items():
        # Check if the key is already in the common_dict
        if key in common_dict:
            # If the current value is greater, update the value and rename the key
            if value > common_dict[key]:
                common_dict[f"{key}_{i}"] = value
                del common_dict[key]
        else:
            # If the key is not in common_dict, add it as is
            common_dict[key] = value

# Print the common dict
print("\nCommon dict:")
print(common_dict)