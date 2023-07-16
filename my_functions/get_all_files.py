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
    assert len(file_list) == 0, "file_list must be an empty list"

    