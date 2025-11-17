from pathlib import Path
import re
import os
from tempfile import NamedTemporaryFile


def generate_svg(diagram: str, output_file: Path) -> None:
    """Generates an SVG file from a diagram string using d2."""

    with NamedTemporaryFile(suffix=".d2") as tmp_file:
        Path(tmp_file.name).write_text(diagram)
        print("Generating", output_file.name)
        os.system(f"d2 {tmp_file.name} {output_file}")
        fix_svg_width_height(output_file)


def generate_light_and_dark_svgs(diagram_file: Path, output_dir: Path):
    """Generates both light and dark SVGs for a diagram."""

    diagram = diagram_file.read_text()
    output_file = output_dir / diagram_file.with_suffix(".svg").name
    dark_output_file = output_dir / diagram_file.with_suffix(".dark.svg").name
    generate_svg(diagram, output_file)
    generate_svg(to_dark(diagram), dark_output_file)


def to_dark(diagram: str) -> str:
    """Converts a diagram to dark mode by manipulating colors."""

    color_mapping = {
        # general
        "#000000": "#FFFFFF",
        # main background color
        "#FCF9FA": "#161416",
        # title text, parent->child edge color
        "#170206": "#F4F1F4",
        # dependency edge color
        "#9B1A47": "#F97F76",
        # queued
        "#FFF0F5": "#A37200",
        "#504448": "#fcc76f",
        # running
        "#AFEEEE": "#3E7079",
        "#0e5253": "#B1E5EF",
        # computed
        "#F0FFF0": "#265429",
        "#3F4B40": "#B7EBB8",
        # failed
        "#FA8072": "#A31800",
        "#4A1511": "#F78D79",
    }

    for light_color, dark_color in color_mapping.items():
        diagram = diagram.replace(light_color, dark_color)

    return diagram


def fix_svg_width_height(svg_file: Path):
    """D2 makes SVGs responsive, without a width and height set. That doesn't work when embedding
    into mintlify, since images will have a size of 0x0. This function fixes that by reading the
    SVG and adding the width and height attributes, setting it to the viewBox width and height.
    """
    svg = svg_file.read_text()
    parts = svg.split(">")
    to_fix = parts[1]
    if "width" not in to_fix:
        width, height = re.findall(r'viewBox="\d+ \d+ (\d+) (\d+)"', to_fix)[0]
        to_fix = to_fix + f' width="{width}" height="{height}"'
        parts[1] = to_fix

    svg = ">".join(parts)
    svg_file.write_text(svg)


def main():
    diagrams = sorted(Path(__file__).parent.glob("*.d2"))
    output_dir = Path(__file__).parent / "svg"
    for diagram in diagrams:
        generate_light_and_dark_svgs(diagram, output_dir)


if __name__ == "__main__":
    main()
