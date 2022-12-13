from genericpath import exists
from multiprocessing.dummy import current_process
import os


def find_files(suffix, path) -> str:
    """
    Find all files beneath path with file name suffix.
    Note that a path may contain further subdirectories
    and those subdirectories may also contain further subdirectories.
    There are no limit to the depth of the subdirectories can be.
    Args:
      suffix(str): suffix if the file name to be found
      path(str): path of the file system
    Returns:
       a list of paths
    """

    if (isinstance(suffix, str) and isinstance(path, str)):

        if len(suffix) == 0:
            print('Negative Ghostrider - must provide a file extension for searching')
            return -1

        # does path exist
        if os.path.exists(path) == False:
            print('Negative Ghostrider - file path doesn\'t appear to exist')
            return -1

        # initialize a list for storing paths
        path_list_local = []

        if os.path.isdir(path):
            for sub_path in os.listdir(path):
                cur_dir = os.path.join(path, sub_path)
                if os.path.isfile(cur_dir):
                    # determine if file ends in the correct extension
                    if os.path.splitext(sub_path)[1] == suffix:
                        file = cur_dir.split('\\')[-1]
                        path_list_local.append(file)
                else:
                    # if the item is a subdirectory continue down the rabbithole
                    sov = find_files(suffix, cur_dir)
                    if sov:
                        for element in sov:
                            path_list_local.append(element)
        return path_list_local

    else:
        print('Arguments must be strings')
        return -1

print(find_files('.c','.\testdir')) # expect ['a.c', 'b.c', 'a.c', 't1.c']

############ TEST CASES ############ 

# Test Case 1
print('emptyTest', find_files('','')) # expect emptyTest, -1

# Test Case 2
print('typeTest', find_files(5,8)) # expect typeTest, -1

# Test Case 3
print('extTest', find_files('.h','.\testdir')) # expect extTest, ['a.h', 'b.h', 'a.h', 't1.h']

