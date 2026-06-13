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


source= "./static"
destination= "./public"

def main():
    if os.path.exists(destination):
        shutil.rmtree(destination)

    copystatic(source, destination)

    generate_page("./content/index.md", "./template.html", "./public/index.html")

main()
