# Interactive program to collect and update personal details

# Step 1: Collect user input
name = input("Enter your name: ")
age = int(input("Enter your age: "))
address = input("Enter your address: ")

# Step 2: Store details in a list
personal_details = [name, age, address]

# Step 3: Print details with labels
print("\n--- Personal Details ---")
print(f"Name: {personal_details[0]}")
print(f"Age: {personal_details[1]}")
print(f"Address: {personal_details[2]}")

# Step 4: Ask how many years to add
years_to_add = int(input("\nEnter how many years to add to your age: "))

# Step 5: Update the age in the list
personal_details[1] += years_to_add

# Step 6: Display updated information in a formatted sentence
print(f"\nAfter {years_to_add} years, {personal_details[0]} will be {personal_details[1]} years old and will still live at {personal_details[2]}.")
