from pathlib import Path
import re
import subprocess
from tempfile import NamedTemporaryFile


_LIGHT_THEME = """
classes: {
    optional: { style: {opacity: 0.8; stroke-dash: 5 }}
    queued: { style: {fill: "#FFF0F5"; stroke: "#504448"; font-color: "#000000" }}
    running: { style: {fill: "#AFEEEE"; stroke: "#0e5253"; font-color: "#000000" }}
    computed: { style: {fill: "#F0FFF0"; stroke: "#3f4b40"; font-color: "#000000" }}
    failed: { style: {fill: "#FA8072"; stroke: "#4a1511"; font-color: "#000000" }}
    skipped: { style: {fill: "#fcf3ae"; stroke: "#877e3c"; font-color: "#000000" }}
    subtask-edge: { style: {stroke: "#170206" }}
    dependency-edge: { style: {stroke-dash: 3; stroke: "#9B1A47" }}
    diagram-title: { near: top-center; shape: text; style: {font-size: 30; font-color: "#170206" }}
}

style.fill: "#FCF9FA"

vars: {
  d2-config: {
    layout-engine: dagre
    theme-id: 102
    sketch: true
    pad: 10
  }
}
""".strip()

_DARK_THEME = """
classes: {
    optional: { style: {opacity: 0.8; stroke-dash: 5 }}
    queued: { style: {fill: "#A37200"; stroke: "#fcc76f"; font-color: "#FFFFFF" }}
	running: { style: {fill: "#3E7079"; stroke: "#b1e5ef"; font-color: "#FFFFFF" }}
	computed: { style: {fill: "#265429"; stroke: "#b7ebb8"; font-color: "#FFFFFF" }}
	failed: { style: {fill: "#A31800"; stroke: "#f78d79"; font-color: "#FFFFFF" }}
	skipped: { style: {fill: "#c6b63c"; stroke: "#ffed67"; font-color: "#FFFFFF" }}
    subtask-edge: { style: {stroke: "#F4F1F4" }}
    dependency-edge: { style: {stroke-dash: 3; stroke: "#F97F76" }}
    diagram-title: { near: top-center; shape: text; style: {font-size: 30; font-color: "#F4F1F4" }}
}

style.fill: "#161416"

vars: {
  d2-config: {
    layout-engine: dagre
    theme-id: 102
    sketch: true
    pad: 10
  }
}
"""


def generate_svg(diagram: str, output_file: Path) -> None:
    """Generates an SVG file from a diagram string using d2."""

    with NamedTemporaryFile(suffix=".d2") as tmp_file:
        Path(tmp_file.name).write_text(diagram)
        print("Generating", output_file.name)
        subprocess.run(["d2", tmp_file.name, str(output_file)])
        fix_svg_width_height(output_file)


def generate_light_and_dark_svgs(diagram_file: Path, output_dir: Path):
    """Generates both light and dark SVGs for a diagram."""

    diagram = diagram_file.read_text()
    output_file = output_dir / diagram_file.with_suffix(".svg").name
    dark_output_file = output_dir / diagram_file.with_suffix(".dark.svg").name

    light_diagram = _LIGHT_THEME + "\n" + diagram
    dark_diagram = _DARK_THEME + "\n" + diagram
    generate_svg(light_diagram, output_file)
    generate_svg(dark_diagram, dark_output_file)


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
