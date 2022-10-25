import os 

# Directory 
base_path = "C:/Users/xbbn1vc/Desktop/"
directory = "Python_Pune"
sub_directory = "os"

print("Current working directory ", os.getcwd())
os.chdir('../')
print("After : Current working directory ", os.getcwd())
new_path = os.path.join(base_path, directory)
os.chdir(new_path)
print("Now : Current working directory ", os.getcwd())


"""
The list of mode constants are below:

octal 0o400   :::  makes the file readable by owner.
octal 0o200   :::  makes the file writable by owner.
octal 0o100   :::  makes the file executable or searchable by owner.
octal 0o40   :::  makes the readable by group.
octal 0o20   :::  makes the file writable by group.
octal 0o10   :::  makes the file executable or searchable by group.
octal 0o4   :::  makes the file readable by others.
octal 0o2   :::  makes the file writable by others.
octal 0o1   :::  makes the file executable or searchable by others.
"""

more_depth = "a\\b"
new_path = os.path.join(base_path, directory,sub_directory,more_depth)
# os.mkdir(new_path,mode = 0o666) 

os.makedirs(new_path,mode = 0o666) 
print(f"{new_path} created") 

print("directories in the path ",os.listdir(base_path) )

