import os
import json 
from datetime import datetime

class FileManager:


    def create_file(self,filename):
        try:
            with open(filename,'x') as f:
                print(f"File: {filename} created successfully!!!")
        except FileExistsError:
            print(f"File:{filename} already exists!!!")
        except Exception as e:
            print("An Unknown Error Occurred!!!")


    def view_files(self):
        files=os.listdir()
        if not files:
            print("No Files Found!!!")
        else:
            print("Files in Directory:- ")
            for file in files:
                print(file)


    def delete_file(self,filename):
        try :
            os.remove(filename)
            print(f"File {filename} Deleted Successfully!!!")
        except FileNotFoundError:
            print(f"File {filename} Not Exists!!!")
        except Exception as e:
            print("An Unknown Error Occurred!!!")


    def read_file(self,filename):
        try:
            with open(filename,'r') as f:
                content=f.read()
                print(f"Content of {filename} is \n {content}")
        except FileNotFoundError:
            print(f"File:{filename} already exists!!!")
        except Exception as e:
            print("An Unknown Error Occurred!!!")  


    def edit_file(self,filename):                 #11
        try:
            with open(filename,"a") as f:
                content=input("Enter the Data to be added :-")
                f.write(content+"\n")
                print(f"Content Added to {filename }successfully")
        except FileNotFoundError :
            print("File Dosen't Exist!!!")

        except Exception as e:
            print("An Unknown Error Occurred!!!")


    def copy_file(self, source, destination):
        try:
            with open(source, 'r') as f1:
                content = f1.read()

            with open(destination, 'w') as f2:
                f2.write(content)

            print(f"File {source} copied to {destination} successfully!!!")

        except FileNotFoundError:
            print(f"File {source} does not exist!!!")

        except Exception as e:
            print("An Unknown Error Occurred!!!")

    
    def search_files(self,filename):
        try:
            files= os.listdir()
            if filename in files:
                print(f"File {filename} found successfully!!!")
            else :
                print(f"File {filename} not found")

        except FileNotFoundError :
            print(f"File {filename} does not exist!!!")
        except Exception as e:
            print("Unexpected error occurred!!!")

    
    def file_info(self,filename):
        try:
            if not os.path.isfile(filename):
                print(f"File {filename} does not exist!!!")
                return
            if not os.path.isfile(filename):
                raise ValueError("The given path is not a file.")

            name = os.path.basename(filename)
            extension = os.path.splitext(filename)[1]
            size = os.path.getsize(filename)
            location = os.path.abspath(filename)

            creation_time = os.path.getctime(filename)
            modification_time = os.path.getmtime(filename)

            print("\n========== FILE INFORMATION ==========")
            print("File Name      :", name)
            print("Extension      :", extension)
            print("Size           :", size, "bytes")
            print("Location       :", location)
            print("Created        :", datetime.fromtimestamp(creation_time))
            print("Last Modified  :", datetime.fromtimestamp(modification_time))
            print("======================================")

        except FileNotFoundError as e:
            print("Error:", e)

        except ValueError as e:
            print("Error:", e)

        except PermissionError:
            print("Error: You do not have permission to access this file.")

        except OSError as e:
            print("OS Error:", e)


    def sort_files(self):
        try:
            files=[]
            for file in os.listdir():
                if os.path.isfile(file):
                    files.append(file)
            if not files:
                print("No files found!!!")
                return
            files.sort()
            print("Sorted Files:-")
            for file in files:
                print(file)
        except Exception as e:
            print("An Unknown error occurred!!!")


    def list_files(self):

        try:
            files = os.listdir()

            if not files:
                print("No Files Found!!!")
                return

            print("Files in Directory:-")

            for file in files:
                if os.path.isfile(file):
                    print(file)

        except Exception as e:
            print("An Unknown Error Occurred!!!")


    def organize_files(self):
        try:

            categories = {
                "Images": [".jpg", ".jpeg", ".png", ".gif"],
                "Videos": [".mp4", ".mkv", ".avi"],
                "Music": [".mp3", ".wav"],
                "Documents": [".txt", ".pdf", ".docx"],
                "Python": [".py"] }

            for file in os.listdir():

                if os.path.isfile(file) and file.lower()!= "ntuser.dat":

                    extension = os.path.splitext(file)[1].lower()

                    folder = "Others"

                    for category in categories:

                        if extension in categories[category]:
                            folder = category
                            break

                    if not os.path.exists(folder):
                        os.mkdir(folder)

                    destination = os.path.join(folder, file)

                    if not os.path.exists(destination):
                        os.rename(file,destination)
                    else:
                        print(f"{file} already exists in folder!!!")
                    
                      

                    print(f"{file} moved to {folder} successfully!!!")

            print("Files organized successfully!!!")

        except Exception as e:
            print("An Unknown Error Occurred!!!",e )


    def create_folder(self,folname):
        try:
            os.mkdir(folname)          #mkdir = make directory , used to make folders
            print(f"Folder {folname} created successfully!!! ")
        except FileExistsError:
            print(f"Folder Already Exists!!!")
        except Exception as e:
            print(f"An Unknown Error Occurred!!!")


    def delete_folder(self,folname):
        try:
            os.rmdir(folname)
            print(f"Folder {folname} removed successfully!!!")

        except FileNotFoundError:
            print(f"Folder {folname} doesn't exist!!!")

        except Exception as e:
            print("An Unknown Error Occurred!!!")


    def change_directory(self, path):
        try:
            os.chdir(path)
            print(f"Directory changed to {os.getcwd()} successfully!!!")
        except FileNotFoundError:
            print("Directory does not exist!!!")
        except NotADirectoryError:
            print("The given path is not a directory!!!")
        except PermissionError:
            print("Permission denied!!!")
        except Exception as e:
            print("An Unknown Error Occurred!!!")


    def current_directory(self):
        try:
            print("Current Directory:", os.getcwd())
        except Exception as e:
            print("An Unknown Error Occurred!!!")


    def directory_statistics(self):
    
        try:
            files = 0
            folders = 0
            total_size = 0

            for item in os.listdir():
                if os.path.isfile(item):
                    files += 1
                    total_size += os.path.getsize(item)
                elif os.path.isdir(item):
                    folders += 1

            print("\n========== DIRECTORY STATISTICS ==========")
            print("Total Files   :", files)
            print("Total Folders :", folders)
            print("Total Size    :", total_size, "bytes")
            print("==========================================")

        except Exception as e:
            print("An Unknown Error Occurred!!!")



fm = FileManager()

def main():
    while True:
        print("\n========== FILE MANAGER ==========")
        print("1. Create File")
        print("2. View All Items")
        print("3. Delete File")
        print("4. Read File")
        print("5. Copy File")
        print("6. Search File")
        print("7. File Information")
        print("8. Sort Files")
        print("9. List Files Only")
        print("10. Organize Files")
        print("11. Edit Files")
        print("12. Create Folder")
        print("13. Delete Folder")
        print("14. Change Directory")
        print("15. Current Directory")
        print("16. Directory Statistics")
        print("17. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            filename = input("Enter filename: ")
            fm.create_file(filename)

        elif choice == "2":
            fm.view_files()

        elif choice == "3":
            filename = input("Enter filename to delete: ")
            fm.delete_file(filename)

        elif choice == "4":
            filename = input("Enter filename to read: ")
            fm.read_file(filename)

        elif choice == "5":
            source = input("Enter source filename: ")
            destination = input("Enter destination filename: ")
            fm.copy_file(source, destination)

        elif choice == "6":
            filename = input("Enter filename to search: ")
            fm.search_files(filename)

        elif choice == "7":
            filename = input("Enter filename: ")
            fm.file_info(filename)

        elif choice == "8":
            fm.sort_files()

        elif choice == "9":
            fm.list_files()

        elif choice == "10":
            fm.organize_files()

        elif choice=="11":
            filename=input("Enter name of file to edit")
            fm.edit_file(filename)
            

        elif choice == "12":
            folder = input("Enter folder name: ")
            fm.create_folder(folder)

        elif choice == "13":
            folder = input("Enter folder name to delete: ")
            fm.delete_folder(folder)

        elif choice == "14":
            path = input("Enter directory path: ")
            fm.change_directory(path)

        elif choice == "15":
            fm.current_directory()

        elif choice == "16":
            fm.directory_statistics()

        elif choice == "17":
            print("Exiting File Manager...")
            break

        else:
            print("Invalid choice!!!")


if __name__ == "__main__":
    main()




