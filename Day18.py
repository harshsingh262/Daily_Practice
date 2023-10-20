import shutil
source = "path/main.py"
destination = "path/main2.py"
dest = shutil.copy(source, destination)
print("Destination path: ",dest)