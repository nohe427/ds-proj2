import os

def find_files(suffix, path):
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
  my_paths = list()
  for dirpath in os.listdir(path):
    filepath = os.path.join(path, dirpath)
    if os.path.isfile(filepath):
      if filepath.endswith(suffix):
        my_paths.append(filepath)
    elif os.path.isdir(filepath):
      for files in find_files(suffix, filepath):
        my_paths.append(files)
  return my_paths

# This is the function invocation.  Comment out if necessary.
# Problem statement ambigious on if this is requeired in submission.
print(find_files(".c", "."))