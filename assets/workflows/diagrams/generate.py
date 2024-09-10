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

    # dark background color
    diagram = diagram.replace('style.fill: "#fcf9fa"', 'style.fill: "#161416"')
    # white title text color
    diagram = diagram.replace('style.font-color: "black"', 'style.font-color: "white"')

    # replace all fill colors depending on the state of the task:
    lookup = {
        "HoneyDew": ("#265429", "#C7E6C9"),  # computed
        "LavenderBlush": ("#A37200", "#FFE099"),  # queued
        "PaleTurquoise": ("#3E7079", "#AED0D5"),  # running
        "Salmon": ("#A31800", "#FF9785"),  # failed
    }

    for task_color, replace_colors in lookup.items():
        fill_color, stroke_color = replace_colors
        diagram = diagram.replace(
            f"style.fill: {task_color}",
            f'style.fill: "{fill_color}"\n  style.stroke: "{stroke_color}"\n  style.font-color: "white"',
        )

    # replace dependency edges with another color
    dependency_edges = re.findall(
        r"(([0-9a-zA-Z-]+ <- [0-9a-zA-Z-]+): \{.*)\n", diagram
    )
    for edge, relation in dependency_edges:
        diagram = diagram.replace(
            edge, relation + ': {style: {stroke: "#F97F76"; stroke-dash: 3}}'
        )

    # make subtask edges white
    subtask_edges = re.findall(r"([0-9a-zA-Z-]+ -> [0-9a-zA-Z-]+)\n", diagram)
    for edge in subtask_edges:
        diagram = diagram.replace(edge, edge + ": {style.stroke: white}")

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
