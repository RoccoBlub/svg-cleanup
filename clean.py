import re
import os
import sys

def simplify_svg(file_path):
    if not os.path.exists(file_path):
        print(f"Error: File '{file_path}' not found.")
        return

    # Get the filename and set output path to the current directory
    file_name = os.path.basename(file_path)
    output_path = os.path.join(os.getcwd(), "fixed_" + file_name)

    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    def process_color(match):
        # Extract the hex value
        hex_val = match.group(1).lstrip('#')

        # Expand short hex like #000 to #000000
        if len(hex_val) == 3:
            hex_val = ''.join([c*2 for c in hex_val])

        try:
            r = int(hex_val[0:2], 16)
            g = int(hex_val[2:4], 16)
            b = int(hex_val[4:6], 16)

            # Calculate brightness (Luma)
            brightness = (r * 0.299 + g * 0.587 + b * 0.114)

            # If bright (>128), make it white. If dark, make it black.
            new_color = "#FFFFFF" if brightness > 128 else "#000000"
            return f'fill="{new_color}"'
        except:
            return match.group(0)

    # Replace all fill="#xxxxxx" or fill="#xxx"
    new_content = re.sub(r'fill="(#?[a-fA-F0-9]{3,6})"', process_color, content)

    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(new_content)

    print(f"Done! Created: {output_path}")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        simplify_svg(sys.argv[1])
    else:
        print("Usage: python3 clean.py path/to/your/file.svg")
