import os
import pathlib

import fire


def find_rc(rc_name=".examplerc"):

    #sprawdzenie zmiennj srodowiskowej
    var_name = "EXAMPLERC_DIR"
    example_dir = os.environ.get(var_name)
    if example_dir:
        dir_path = pathlib.Path(example_dir)
        config_path = dir_path / rc_name
        print(f"Sprawdzenie evar {config_path}")
        if config_path.exists():
            return config_path.as_posix()

    # Sprawdź bieżący katalog roboczy
    config_path = pathlib.Path.cwd() / rc_name
    if not config_path.exists():
        config_path.touch()
    print(f"Sprawdzenie cwd {config_path}")
    if config_path.exists():
        print(f"Posix: {config_path.as_posix()}, uri: {config_path.as_uri()}")
        return config_path.as_posix()

    # Sprawdzanie katalogu macierzystego użytkownika
    config_path = pathlib.Path.home() / rc_name
    print(f"Sprawdzenie home {config_path}")


if __name__ == "__main__":
    fire.Fire()
