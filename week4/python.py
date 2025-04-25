# Part 1: File Read & Write Challenge

# Step 1: Read the original file
try:
    with open("input.txt", "r") as file:
        content = file.read()

    # Step 2: Modify the content (e.g., make it uppercase)
    modified_content = content.upper()

    # Step 3: Write to a new file
    with open("output.txt", "w") as new_file:
        new_file.write(modified_content)

    print("Content successfully modified and written to 'output.txt'.")

except FileNotFoundError:
    print("The file 'input.txt' does not exist.")
except Exception as e:
    print(f"An error occurred: {e}")




# Part 2: Error Handling Lab

filename = input("Enter the filename to read: ")

try:
    with open(filename, "r") as file:
        content = file.read()
        print("\nFile Content:\n")
        print(content)

except FileNotFoundError:
    print("Error: File not found. Please check the filename and try again.")
except PermissionError:
    print("Error: You don't have permission to read this file.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
