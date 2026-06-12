import os
import shutil

source= "./static"
destination= "./public"

def main():
    if os.path.exists(destination):
        shutil.rmtree(destination)

    copytree(source, destination)

def copytree(source_dir: str, dest_dir: str) -> None :
    if not os.path.exists(dest_dir):
        os.mkdir(dest_dir)

    for item in os.listdir(source_dir):
        from_path = os.path.join(source_dir, item)
        to_path = os.path.join(dest_dir, item)

        if os.path.isfile(from_path):
            shutil.copy(from_path, to_path)
        else:
            copytree(from_path, to_path)

main()
