from PIL import Image
import os

# Define the directory containing the images
directory = r'C:\Users\luixh\Documents\SpartaGlobal\Github\python_learning\pictures'

# Define the target resolution
target_resolution = (600, 600)  # Width x Height

# Loop through all files in the directory
for filename in os.listdir(directory):
    # Check if the file is an image (e.g., PNG, JPG, etc.)
    if filename.endswith(('.png', '.jpg', '.jpeg', '.gif')):
        # Open the image
        filepath = os.path.join(directory, filename)
        im = Image.open(filepath)

        # Save the image with the target resolution and original extension
        output_filename = os.path.splitext(filename)[0] + '-600' + os.path.splitext(filename)[1]
        output_filepath = os.path.join(directory, output_filename)
        im.save(output_filepath, dpi=target_resolution)

        print(f"{filename} converted to {output_filename} with resolution {target_resolution}")