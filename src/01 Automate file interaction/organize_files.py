''' Organize files  into subdirectories 
    
    Output:
    Created a subdirectory: src\01 Automate file interaction\\Documents
    Created a subdirectory: src\01 Automate file interaction\\Images
    Created a subdirectory: src\01 Automate file interaction\\Audio
    Created a subdirectory: src\01 Automate file interaction\\Videos
'''
import os
from pathlib import Path

SUBDIRS = {
    "Documents": ['.pdf','.rtf','.txt', '.xlsx'],
    "Audio":['.m4a','.m4b','.mp3'],
    "Videos": ['.mov','.avi','.mp4'],
    "Images": ['.jpg','.jpeg','.png']
}

# Select directory
def select_subdirectory(file_type):
    for folder_name, values_list in SUBDIRS.items():
        for value in values_list:
            if file_type == value:
                return folder_name
    # If file type is not in the list put it in the Other folder
    return 'Mixed'

def create_subdirectories(directory_path):
    ''' Create subdirectories and organize the files based on the file type'''
    for item in os.scandir(directory_path):
        # Create Path object
        path_object = Path(item)

        # Extract file extension and relative path to the folder where subfolders
        # are going to be created.
        file_extension = path_object.suffix
        parent_directory_path = path_object.parents[1]

        # Select subdirectory name
        subdir_name= select_subdirectory(file_extension)
        
        # Create a new Path object for the subdirectory
        subdir_path = parent_directory_path / subdir_name

        if not subdir_path.is_dir():
            print(f"Created a subdirectory: {subdir_path}")
            subdir_path.mkdir()

        # Move the file to the new location, depending on its file type
        path_object.rename(subdir_path.joinpath(path_object.name))


if __name__== '__main__':
    directory_path = ".\\src\\01 Automate file interaction\\Mixed"
    create_subdirectories(directory_path)


# def organizeDirectory():
#     for item in os.scandir():
#         if item.is_dir():
#             continue
#         filePath = Path(item)
#         filetype = filePath.suffix.lower()
#         directory = pickDirectory(filetype)
#         directoryPath = Path(directory)
#         if directoryPath.is_dir() != True:
#             directoryPath.mkdir()
#         filePath.rename(directoryPath.joinpath(filePath))

# organizeDirectory()