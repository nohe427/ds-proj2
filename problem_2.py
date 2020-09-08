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
  if suffix is None or path is None:
    return
  my_paths = list()
  _find_files(suffix, path, my_paths)
  return my_paths

def _find_files(suffix, path, my_paths):
  for dirpath in os.listdir(path):
    filepath = os.path.join(path, dirpath)
    if os.path.isfile(filepath):
      if filepath.endswith(suffix):
        my_paths.append(filepath)
    elif os.path.isdir(filepath):
      _find_files(suffix, filepath, my_paths)

# Test Case 1
print("\n Test 1 - None type file extension")
print(find_files(None, "."))
# Retuns nothing

# Test Case 2
print("\n Test 2 - None type path provided")
print(find_files(".c", None))
# Retuns nothing

# Test Case 3
print("\n Test 3 - Regular input test")
print(find_files(".py", "."))
# returns ['./problem_6.py', './problem_3.py', './problem_4.py', './problem_2.py', './problem_1.py', './problem_5.py']