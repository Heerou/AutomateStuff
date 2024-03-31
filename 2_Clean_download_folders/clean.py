import os

filePath = '/Users/JULIO/Downloads/mGBA-0.10.3-win32-installer.exe'

print(filePath)
if os.path.isfile(filePath):
    os.remove(filePath)
    print("File deleted")
else:
    print("File does not exist")