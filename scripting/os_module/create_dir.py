import os

# Directory
directory = "test_dir"

# Parent Directory
parent_directory = "C:/Users/luixh/Documents"

# Path
path = os.path.join(parent_directory, directory)

print(path)
# Create Dir
os.mkdir(path)