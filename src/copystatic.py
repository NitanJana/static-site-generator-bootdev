
import os
import shutil


def copystatic(source_dir: str, dest_dir: str) -> None :
    if not os.path.exists(dest_dir):
        os.mkdir(dest_dir)

    for item in os.listdir(source_dir):
        from_path = os.path.join(source_dir, item)
        to_path = os.path.join(dest_dir, item)

        if os.path.isfile(from_path):
            shutil.copy(from_path, to_path)
        else:
            copystatic(from_path, to_path)
