import os
import concurrent.futures

# Create a hash table to store the unique lines of text
lines = {}

# Define a function that reads the lines of a text file and adds the unique lines to the global hash table
def process_file(file):
    # Open the file, read all the lines, and close the file
    with open(file, 'r') as f:
        file_lines = f.readlines()
        f.close()

    # Iterate over the lines of text in the file
    for line in file_lines:
        # If the line is not already in the hash table, add it
        if line not in lines:
            lines[line] = True

# Use a concurrent.futures.ThreadPoolExecutor to run the process_file function concurrently
with concurrent.futures.ThreadPoolExecutor() as executor:
    # Iterate over the files in the folder and submit them to the executor
    for file in os.listdir():
        # Check if the file is a .txt file
        if file.endswith('.txt'):
            executor.submit(process_file, file)

# Open the output file in write mode
with open('output.txt', 'w') as f:
    # Write each line to the output file
    for line in lines:
        f.write(line)
    # Close the file
    f.close()