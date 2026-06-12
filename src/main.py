import os
import shutil

from copystatic import copystatic

source= "./static"
destination= "./public"

def main():
    if os.path.exists(destination):
        shutil.rmtree(destination)

    copystatic(source, destination)

main()
