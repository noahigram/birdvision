import os
import shutil
import random

# I want to be able to use the same process as in the PyTorch tutorial, so I need folders for train/test. Curently the data is 
# just a folder for each of the 200 species

# Set paths to your dataset and new directories
dataset_dir = 'data/CUB_200_2011/CUB_200_2011/images'  # The folder that contains 200 subfolders
train_dir = 'data/CUB_200_2011/train'  # Path to where the training folder should be created
test_dir = 'data/CUB_200_2011/test'    # Path to where the testing folder should be created

# Define the split ratio (e.g., 80% training, 20% testing)
train_ratio = 0.8

# Create the train and test directories if they don't exist
os.makedirs(train_dir, exist_ok=True)
os.makedirs(test_dir, exist_ok=True)

# Get a list of all species (subfolders)
species_folders = os.listdir(dataset_dir)

for species in species_folders:
    species_path = os.path.join(dataset_dir, species)
    
    if os.path.isdir(species_path):  # Make sure it's a folder
        images = os.listdir(species_path)  # Get list of all images in the species folder
        random.shuffle(images)  # Shuffle the images to randomize the split

        # Determine split index
        split_index = int(len(images) * train_ratio)
        
        # Split images into train and test
        train_images = images[:split_index]
        test_images = images[split_index:]

        # Create species subfolders in training and testing directories
        train_species_dir = os.path.join(train_dir, species)
        test_species_dir = os.path.join(test_dir, species)
        os.makedirs(train_species_dir, exist_ok=True)
        os.makedirs(test_species_dir, exist_ok=True)

        # Move images to their respective folders
        for img in train_images:
            src = os.path.join(species_path, img)
            dst = os.path.join(train_species_dir, img)
            shutil.copyfile(src, dst)

        for img in test_images:
            src = os.path.join(species_path, img)
            dst = os.path.join(test_species_dir, img)
            shutil.copyfile(src, dst)

print("Dataset split into training and testing sets successfully.")
