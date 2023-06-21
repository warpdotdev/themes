import argparse
import os
from pathlib import Path
from typing import Any

import yaml


def get_all_input_files(
    input_dir: str,
) -> list[str]:
    """Parameters
    ----------
    input_dir :

    Returns
    -------

    """
    filenames: Any = next(os.walk(input_dir), (None, None, []))[2]
    return list(filter(lambda f: (f.endswith(("yaml", "yml"))), filenames))


def ensure_output_dir(
    output_dir: str,
) -> None:
    """Parameters
    ----------
    output_dir :
    """
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)


def add_color_to_dict(
    output: dict[str, str],
    obj: dict[str, str],
    key: str,
    prefix: str | None = None,
) -> None:
    """Parameters
    ----------
    output :
    obj :
    key :
    prefix :
    """
    if not prefix:
        prefix = ""
    output[f"{prefix}{key}"] = obj[key]


def get_color_dict(
    input_dir: str,
    file_name: str,
) -> dict[str, str]:
    """Parameters
    ----------
    input_dir :
    file_name :

    Returns
    -------

    """
    file = open(os.path.join(input_dir, file_name))
    loaded_theme = yaml.safe_load(file)
    output: dict[str, str] = {}
    add_color_to_dict(output, loaded_theme, "accent")
    add_color_to_dict(output, loaded_theme, "foreground")
    add_color_to_dict(output, loaded_theme, "background")

    normal_colors = loaded_theme["terminal_colors"]["normal"]
    for color in normal_colors:
        add_color_to_dict(output, normal_colors, color)

    bright_colors = loaded_theme["terminal_colors"]["bright"]
    for color in bright_colors:
        add_color_to_dict(output, bright_colors, color, "br")

    return output


def file_name_to_display(
    file_name: str,
) -> str:
    """Parameters
    ----------
    file_name :

    Returns
    -------

    """
    file_name = Path(file_name).with_suffix("").name

    split = file_name.split("_")
    output = []
    for s in split:
        output.append(s.capitalize())
    return " ".join(output)


def gen_svg_for_theme(
    color_dict: dict[str, str],
    svg_template: str,
) -> str:
    """Parameters
    ----------
    color_dict :
    svg_template :

    Returns
    -------

    """
    output = svg_template

    for key, value in color_dict.items():
        if isinstance(value, str):
            output = output.replace(f"{{{key}}}", value)
    return output


def main() -> None:
    """ """
    parser = argparse.ArgumentParser(
        description="Generate README.md with embedded SVG previews.",
    )
    parser.add_argument(
        "input_dir",
        type=str,
        help="Directory from which to read in all Warp themes.",
    )
    parser.add_argument(
        "--output_dir",
        type=str,
        help="Where to save README.md",
        default="",
    )
    parser.add_argument(
        "--svg_path",
        type=str,
        help="Path to svg template file.",
        default="scripts/preview.svg",
    )
    parser.add_argument(
        "--intro_file",
        type=str,
        help="What should go on top of README.md.",
        default="README-intro.md",
    )
    args = parser.parse_args()

    input_dir: str = args.input_dir
    output_dir: str
    if output_dir := args.output_dir:
        ensure_output_dir(output_dir=output_dir)
    else:
        output_dir = input_dir

    filenames = get_all_input_files(input_dir=input_dir)
    markdown = ["|Theme name | Preview|", "| --- | --- |"]
    svg = open(args.svg_path).read()
    svg_dir = os.path.join(output_dir, "previews")
    os.makedirs(svg_dir, exist_ok=True)

    for input_file in sorted(filenames):
        print(f"Generating for {input_file}")
        cell = f"|**[{file_name_to_display(input_file)}]({input_file})**:|"
        color_dict = get_color_dict(output_dir, input_file)
        theme_svg = gen_svg_for_theme(color_dict, svg)
        theme_svg_path = os.path.join(svg_dir, f"{input_file}.svg")
        with open(theme_svg_path, "w") as svg_out:
            svg_out.write(theme_svg)
        cell += f"<img src='previews/{input_file}.svg' width='300'>|"
        markdown.append(cell)

    output_str = "\n".join(markdown)
    with open(os.path.join(output_dir, "README.md"), "w") as output:
        output.write(output_str)


if __name__ == "__main__":
    main()
