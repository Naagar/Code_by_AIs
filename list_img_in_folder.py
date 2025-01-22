import os

# Function to get image file names
def get_image_names(folder_path, output_file):
    # List of common image extensions
    image_extensions = ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff', '.webp']
    
    # Get list of all files in the folder
    all_files = os.listdir(folder_path)
    
    # Filter the files that are images based on extensions
    image_files = [file for file in all_files if any(file.lower().endswith(ext) for ext in image_extensions)]
    
    # Sort the list of image files
    image_files.sort()
    
    # Write the sorted image names into the output text file
    with open(output_file, 'w') as f:
        for image in image_files:
            f.write(image + '\n')

# Example usage
folder_path = 'path/to/your/folder'  # Specify your folder path here
output_file = 'image_names.txt'  # Output text file where image names will be saved

get_image_names(folder_path, output_file)
print(f"Image names have been written to {output_file}")
