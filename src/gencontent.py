import os
from block_markdown import markdown_to_html_node
from copystatic import copy_files_recursive


def extract_title(markdown):
    blocks = markdown.splitlines()
    for block in blocks:
        if block.startswith("# "):
            return block[2:].strip()
    raise ValueError("No title found in markdown")

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}...")
    with open(from_path, "r") as f:
        markdown_file = f.read()
    with open(template_path, "r") as f:
        template_file = f.read()
    html_string = markdown_to_html_node(markdown_file).to_html()
    page_title = extract_title(markdown_file)
    updated_template = template_file.replace("{{ Content }}", html_string)
    updated_template = updated_template.replace("{{ Title }}", page_title)
    with open(dest_path, "w") as f:
        f.write(updated_template)
    
def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    for filename in os.listdir(dir_path_content):
        from_path = os.path.join(dir_path_content, filename)
        dest_path = os.path.join(dest_dir_path, filename)
        if os.path.isfile(from_path) and filename.endswith(".md"):
            dest_path = dest_path[:-3] + ".html"
            generate_page(from_path, template_path, dest_path)
        elif os.path.isdir(from_path):
            if not os.path.exists(dest_path):
                os.mkdir(dest_path)
            generate_pages_recursive(from_path, template_path, dest_path)
