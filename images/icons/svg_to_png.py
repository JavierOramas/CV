import os
import cairosvg


def convert_svg_to_png(svg_path, png_path):
    cairosvg.svg2png(url=svg_path, write_to=png_path)


def convert_svgs_in_directory(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".svg"):
                try:
                    print(file)
                    svg_file = os.path.join(root, file)
                    png_file = os.path.splitext(svg_file)[0] + ".png"
                    convert_svg_to_png(svg_file, png_file)
                    os.remove(svg_file)
                    print(f"Converted {svg_file} to {png_file}")
                except:
                    pass
# Example usage
directory = "."
convert_svgs_in_directory(directory)
