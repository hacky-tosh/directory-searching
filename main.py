import glob
import shutil
import os 


#Ashutosh Sahu
# www.ashu.codes

path = input("Enter the path of the directory : \n")

destination_folder = input("Enter the path of the destination folder : \n")

exte = input("Enter the file extension without . \n")




files = glob.glob(path + f"/**/*.{exte}", recursive = True)

for ele in files:
    shutil.move(ele, destination_folder)

print("All transferd has been successfully completed")
print(f"total {len(files)} files found")

