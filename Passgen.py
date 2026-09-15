import resources.options as options
import os

def clear_console():
    if os.name == "posix":
        os.system("clear")
    else:
        os.system("cls")

#Setup
manager = options.manager()
clear_console()

try:
    while True:
        clear_console()

        print("1) Show all passwords\n2) Show password for a specific site (specify later)\n3) Create new password\n4) Delete saved password for a specific site (specify later)\n5) Save a backup file\n6) Import credentials from file (specify later)\n7) Exit Passgen")
        choice =  int(input(options.codes.Bold("Choice: ")))
        assert choice in range(1, 8), "Invalid Choice, must be one of the indexes above"

        if choice == 1:
            manager.show_passwds()
            options.waitpoint()
        elif choice == 2:
            url = input("Passwords URL to show:\n")
            manager.show_passwd(url)
            options.waitpoint()
        elif choice == 3:
            manager.new_passwd()
            options.waitpoint()
        elif choice == 4:
            url = input("Passwords URL to delete:\n")
            manager.delete_site(url)
            options.waitpoint()
        elif choice == 5:
            bu_path = f"{input('path/filename with which the backup file will be saved: ')}.lst.old"
            manager.backup(bu_path)
            options.waitpoint()
        elif choice == 6:
            bu_path = input('path/filename to the file with the credentials to replace: ')
            manager.restore(bu_path)
            options.waitpoint()
        elif choice == 7:
            clear_console()
            exit()
except KeyboardInterrupt:
    print(options.codes.Bold("\nProgram interrupted, exiting..."))
    exit()