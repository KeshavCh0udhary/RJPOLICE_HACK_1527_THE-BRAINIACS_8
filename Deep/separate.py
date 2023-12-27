import os
import shutil

def separate_files(input_file, label_folders):
    """Separates files based on labels in an input file.

    Args:
        input_file (str): Path to the input file containing filenames and labels.
        label_folders (dict): Dictionary mapping labels to destination folder paths.
    """

    with open(input_file, 'r') as file:
        for line in file:
            filename, label = line.strip().split()
            source_path = os.path.join('data', filename)  # Assuming data files are in the 'data' folder

            if label in label_folders:
                destination_path = os.path.join(label_folders[label], filename)
                shutil.copy(source_path, destination_path)
                print(f"Moved '{filename}' to '{destination_path}'.")
            else:
                print(f"Unknown label '{label}' for file '{filename}'. Skipping.")

# Example usage
input_file_path = 'C:\\Users\\HP\\Downloads\\Input'
label_folders = {'label1': 'spoof', 'label2': 'bona-fide'}  # Map labels to folder names

# Create folders if they don't exist
for folder in label_folders.values():
    os.makedirs(folder, exist_ok=True)

# Separate files
separate_files(input_file_path, label_folders)
