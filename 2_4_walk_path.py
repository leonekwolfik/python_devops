import os
import fire


def walk_path(parent_path):
    for parent_path, directories, files in os.walk(parent_path):
        print(f"Sprawdzanie: {parent_path}")
        for file_name in files:
            file_path = os.path.join(parent_path, file_name)
            last_access = os.path.getatime(file_path)
            size = os.path.getsize(file_path)
            print(f"Plik: {file_path}")
            print(f"\tostani dostęp: {last_access}")
            print(f"\trozmiar: {size}")


if __name__ == "__main__":
    fire.Fire()
/Volumes/Work/python_devops/main.py/Volumes/Work/python_devops/main.py