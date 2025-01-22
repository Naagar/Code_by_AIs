import os
import random

# Function to get image file names and split them into two lists
def split_image_names(folder_path, output_file_80, output_file_20):
    # List of common image extensions
    image_extensions = ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff', '.webp']
    
    # Get list of all files in the folder
    all_files = os.listdir(folder_path)
    
    # Filter the files that are images based on extensions
    image_files = [file for file in all_files if any(file.lower().endswith(ext) for ext in image_extensions)]
    
    # Sort the image files
    image_files.sort()
    
    # Shuffle the image files to randomize them
    random.shuffle(image_files)
    
    # Calculate the split index (80% for training, 20% for testing)
    split_index = int(len(image_files) * 0.8)
    
    # Split into two lists (80% and 20%)
    image_files_80 = image_files[:split_index]
    image_files_20 = image_files[split_index:]
    
    # Write the 80% list to output_file_80
    with open(output_file_80, 'w') as f80:
        for image in image_files_80:
            f80.write(image + '\n')
    
    # Write the 20% list to output_file_20
    with open(output_file_20, 'w') as f20:
        for image in image_files_20:
            f20.write(image + '\n')

# Example usage
folder_path = 'path/to/your/folder'  # Specify your folder path here
output_file_80 = 'image_names_80.txt'  # Output text file for the 80% list
output_file_20 = 'image_names_20.txt'  # Output text file for the 20% list

split_image_names(folder_path, output_file_80, output_file_20)
print(f"Image names have been split and saved into {output_file_80} and {output_file_20}")
