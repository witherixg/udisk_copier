import os
import time
import shutil
from datetime import datetime

u_disk_start_symbol = "E"
u_disk_path = u_disk_start_symbol+":/"
destination_path = "C:/copied/"
config_path = "C:/ucopier.cfg"
plugging_status = False

def exist_file(abs_name):
    if os.path.exists(abs_name) and os.path.isfile(abs_name):
        return True
    return False

if not exist_file("C:/ucopier.cfg"):
    with open("C:/ucopier.cfg", "w") as f:
        f.write("E\n")
        f.write("C:/copied/")
        f.close()


def main():
    global u_disk_start_symbol, destination_path
    with open("C:/ucopier.cfg", "r") as f:
        u_disk_start_symbol = f.readline().strip('\n')
        get = f.readline().strip('\n')
        if not get[-1] == '/':
            get += '/'
        destination_path = get
        f.close()
    while True:
        copy(u_disk_path, destination_path)
        time.sleep(10)



def create_folders(path):
    split_path = path.split('/')
    if "" in split_path:
        split_path.remove("")
    for i in range(len(split_path)):
        if not os.path.exists("/".join(split_path[0: i + 1])):
            try:
                os.mkdir("/".join(split_path[0: i + 1]))
            except Exception:
                pass


def copy(from_path, to_path):
    global plugging_status

    if not os.path.exists(from_path):
        print("Check failed!")
        plugging_status = False
        return

    if plugging_status:
        print("Waiting...")
        return

    if not os.path.exists(to_path):
        create_folders(to_path)

    if exist_file(from_path + "ignore.mrk"):
        print(f"{from_path} blocked this copying!")
        return

    print("Copying...")
    shutil.copytree(from_path, destination_path + datetime.now().strftime("%Y-%m-%d_%H-%M-%S"))
    print("Completed!")
    plugging_status = True



if __name__ == "__main__":
    main()
