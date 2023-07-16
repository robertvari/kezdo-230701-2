import os


def get_all_files(root_folder: str, file_list: list):
    """
    Find all files in the root folder and all its subfolders.
    root_folder: (str) The folder to start search
    file_list: (list) An empty list to collect files
    """
    
    # check root_folder validity
    assert os.path.isdir(root_folder), f"root_folder must be a directory. {root_folder}"

    # check file_list validity
    assert isinstance(file_list, list), "file_list must be an empty list"

    # get all content in current folder
    folder_content = [os.path.join(root_folder, i) for i in os.listdir(root_folder)]
    
    # collect folders and files in current folder
    subfolders = []
    found_files = []
    for i in folder_content:
        if os.path.isfile(i):
            found_files.append(i)
        else:
            subfolders.append(i)
    
    # add new files to existing file_list
    file_list += found_files


    # step intu subfolders and continue
    for folder in subfolders:
        get_all_files(folder, file_list)