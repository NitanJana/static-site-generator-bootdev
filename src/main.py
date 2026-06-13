import os
import shutil

from block_markdown import markdown_to_html_node
from copystatic import copystatic


def extract_title(markdown: str) -> str:
    lines = markdown.split("\n")
    for line in lines:
        if line.startswith("# "):
            return line[2:]
    return "Untitled"

def generate_page(from_path: str, template_path: str, dest_path: str):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    with open(from_path) as f:
        contents =  f.read()
    with open(template_path) as t:
        template = t.read()
    html = markdown_to_html_node(contents).to_html()
    title = extract_title(contents)
    template = template.replace("{{ Title }}", title)
    template = template.replace("{{ Content }}", html)

    os.makedirs(os.path.dirname(dest_path), exist_ok=True)
    with open(dest_path, "w") as d:
        d.write(template)

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    for item in os.listdir(dir_path_content):
        if os.path.isfile(os.path.join(dir_path_content, item)):
            if item[-3:] == ".md":
                generate_page(os.path.join(dir_path_content, item), template_path, os.path.join(dest_dir_path, ".".join([item[:-3], "html"])))
        else:
            generate_pages_recursive(os.path.join(dir_path_content, item), template_path, os.path.join(dest_dir_path, item))


source= "./static"
destination= "./public"

def main():
    if os.path.exists(destination):
        shutil.rmtree(destination)

    copystatic(source, destination)

    generate_pages_recursive("./content", "./template.html", "./public")

main()
