'''
# Method 1:

# Open a file in write mode
file = open("test.txt", "w")

# Write content to the file
file.write("Hi, How are you doing?\n")
file.write("It's been a pleasure to meet you.\n")
file.write("Hope to see you soon!")

# Close the file
file.close()

print("File created and content written successfully.")

'''
# Method 2

# File name
filename = "test.txt"

# Content to write
content = "Hello, this is a sample python file.\n We are writing contents to this file."

# Open file using 'with' to ensure it closes automatically
with open(filename, "w") as file:
    file.write(content)


print(f"Content written to {filename} successfully.")




# Read from the file
with open(filename, "r") as file:
    content = file.read()

# Print the content
print(content)



