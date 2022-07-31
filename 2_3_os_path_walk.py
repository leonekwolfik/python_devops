import fire
import os


def walk_path(parent_path):
    print(f"Sprawdzanie: {parent_path}")
    childs = os.listdir(parent_path)  # zwraca zawartości katalogu

    for child in childs:
        child_path = os.path.join(parent_path, child)  # konstrukcja pełnej ścieżki
        if os.path.isfile(child_path):
            last_access = os.path.getatime(child_path)
            size = os.path.getsize(child_path)
            print(f"Plik: {child_path}")
            print(f"\tostani dostęp: {last_access}")
            print(f"\trozmiar: {size}")
        elif os.path.isdir(child_path):
            walk_path(child_path)


if __name__ == "__main__":
    fire.Fire()
