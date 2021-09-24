import yaml
from dataclasses import dataclass
from typing import Dict, List, Optional
import re
import argparse
import os
from pathlib import Path

def get_all_input_files(input_dir: str) -> List[str]:
    filenames = next(os.walk(input_dir), (None, None, []))[2]
    files = filter(lambda f: (f.endswith("yaml") or f.endswith("yml")), filenames)
    return list(files)

def ensure_output_dir(output_dir: str):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

def to_query_param(obj: Dict, key: str, prefix: Optional[str] = None) -> str:
    if prefix:
        return f"{prefix}{key}={obj[key]}"
    return f"{key}={obj[key]}"

def get_query_string(input_dir: str, file_name: str) -> str:
    file = open(os.path.join(input_dir, file_name), 'r')
    loaded_theme = yaml.safe_load(file)
    output = []
    output.append(to_query_param(loaded_theme, "accent"))
    output.append(to_query_param(loaded_theme, "foreground"))
    output.append(to_query_param(loaded_theme, "background"))

    normal_colors = loaded_theme["terminal_colors"]["normal"]
    for color in normal_colors.keys():
        output.append(to_query_param(normal_colors, color))

    bright_colors = loaded_theme["terminal_colors"]["bright"]
    for color in bright_colors.keys():
        output.append(to_query_param(bright_colors, color, "br"))

    return "&".join(output)

def file_name_to_display(file_name: str) -> str:
    file_name = Path(file_name).with_suffix('').name

    split = file_name.split("_")
    output = []
    for s in split:
        output.append(s.capitalize())
    return " ".join(output)

SVG_PATH = "./preview.svg"

def main():
    parser = argparse.ArgumentParser(description='Generate README.md with embedded SVG previews.')
    parser.add_argument('input_dir', type=str, help='Directory from which to read in all Warp themes.')
    parser.add_argument('output_dir', type=str, help='Where to save README.md')
    args = parser.parse_args()

    ensure_output_dir(args.output_dir)

    filenames = get_all_input_files(args.input_dir)
    markdown = []
    markdown.append("|Theme name | Preview|")
    markdown.append("| --- | --- |")
    for input_file in filenames:
        print(f"Generating for {input_file}")
        cell = f"|**{file_name_to_display(input_file)}**:|"
        query_string = get_query_string(args.input_dir, input_file)
        cell += f"<img src='{SVG_PATH}?{query_string}' width='200'>|"
        markdown.append(cell)

    output_str = "\n".join(markdown)
    with open(os.path.join(args.output_dir,"README.md"), 'w') as output:
        output.write(output_str)

if __name__ == "__main__":
    main()
