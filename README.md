# SVG Color Purifier 🎨🚿

A lightweight Python utility designed to clean up AI-generated SVGs by forcing "near-black" and "near-white" paths into high-contrast **Pure Black (#000000)** and **Pure White (#FFFFFF)**.

## The Problem

AI image generators and "Image-to-SVG" converters often produce SVGs with hundreds of slightly different hex codes (e.g., `#010102`, `#000000`, `#050505`). While these look "black" to the human eye, they cause significant issues for:

- **3D Printing:** Slicers may interpret different shades as different heights or materials.
- **Laser Cutting:** Different hex codes often trigger different power/speed settings.
- **Plotters/Vinyl Cutters:** Machines might try to "change pens" for shades that should be identical.

## The Solution

This script analyzes the **Luma (brightness)** of every `fill` attribute in your SVG. Using the standard luminance formula:

`Y=0.299R+0.587G+0.114B`

If a color is mathematically closer to white, it is snapped to `#FFFFFF`. If it is closer to black, it is snapped to `#000000`.

## Features

- ✅ **Hex Normalization:** Handles both 3-digit (#000) and 6-digit (#000000) hex codes.
- ✅ **Smart Thresholding:** Uses perceptual brightness to decide the color flip.
- ✅ **Safe Output:** Never overwrites your original file; it creates a new file prefixed with fixed_.

## Installation

No dependencies required! Just a standard Python 3 installation.
```bash
git clone https://github.com/yourusername/svg-cleanup.git
cd svg-cleanup
``` 

## Usage
Simply run the script and pass the path to your SVG file as an argument:
```bash
python3 clean.py your_image.svg
```

**Output:** A new file named fixed_your_image.svg will be generated in your current directory.



