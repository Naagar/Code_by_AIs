import os
import shutil

# Function to copy images and labels to the new folders based on filenames from a text file
def copy_files_based_on_list(filenames_file, images_folder, labels_folder, train_images_folder, train_labels_folder):
    # Read the list of filenames from the text file
    with open(filenames_file, 'r') as file:
        filenames = [line.strip() for line in file.readlines()]
    
    # Ensure the destination directories exist
    os.makedirs(train_images_folder, exist_ok=True)
    os.makedirs(train_labels_folder, exist_ok=True)
    
    # Loop through each filename in the list
    for filename in filenames:
        image_file = f"{filename}.png"  # Assuming image filenames are .png
        label_file = f"{filename}.txt"  # Assuming label filenames are .txt
        
        # Construct full paths for the image and label
        image_source = os.path.join(images_folder, image_file)
        label_source = os.path.join(labels_folder, label_file)
        
        # Construct full paths for the destination folders
        image_dest = os.path.join(train_images_folder, image_file)
        label_dest = os.path.join(train_labels_folder, label_file)
        
        # Check if the image and label files exist, then copy them
        if os.path.exists(image_source) and os.path.exists(label_source):
            shutil.copy(image_source, image_dest)
            shutil.copy(label_source, label_dest)
            print(f"Copied {image_file} and {label_file} to the destination folders.")
        else:
            print(f"Warning: {image_file} or {label_file} does not exist in the source folder.")

# Example usage
filenames_file = 'image_names_80.txt'  # The text file containing the filenames (without extensions)
images_folder = 'images'  # The folder where the images are stored
labels_folder = 'labels'  # The folder where the label files are stored
train_images_folder = 'train_images'  # The destination folder for the training images
train_labels_folder = 'train_labels'  # The destination folder for the training labels

copy_files_based_on_list(filenames_file, images_folder, labels_folder, train_images_folder, train_labels_folder)
print("Files have been copied successfully.")
