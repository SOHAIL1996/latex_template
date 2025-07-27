#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Software License Agreement (BSD)
#
# @author    Salman Omar Sohail <sorox23@gmail.com>
# @copyright (c) 2024, Salman Omar Sohail, Inc., All rights reserved.

import os
import lorem
import subprocess

TEMPLATE_FILE = "latex_template.tex"
OUTPUT_DIR = "latex_output"
TEMP_TEX_FILE = os.path.join(OUTPUT_DIR, "generated.tex")

# Context for LaTeX template
context = {
    "name": "Salman Omar Sohail",
    "title": "Robot Diagnosis",
    "robot_id": "XXXX-1234",
    "summary": lorem.paragraph() + r"\vspace{0.5cm}" 
                                 +lorem.paragraph(),
    "logo_path": "latex_assets/logo.png"
}

# Dynamic table data
table_data = [
    {"Item": "Laptop", "Quantity": "2", "Price": "$1200"},
    {"Item": "Monitor", "Quantity": "3", "Price": "$300"},
    {"Item": "Keyboard", "Quantity": "5", "Price": "$50"},
    {"Item": "Laptop", "Quantity": "2", "Price": "$1200"},
    {"Item": "Laptop", "Quantity": "2", "Price": "$1200"},
    {"Item": "Monitor", "Quantity": "3", "Price": "$300"},
    {"Item": "Keyboard", "Quantity": "5", "Price": "$50"},
    {"Item": "Laptop", "Quantity": "2", "Price": "$1200"},
    {"Item": "Laptop", "Quantity": "2", "Price": "$1200"},
    {"Item": "Monitor", "Quantity": "3", "Price": "$300"},
    {"Item": "Keyboard", "Quantity": "5", "Price": "$50"},
    {"Item": "Laptop", "Quantity": "2", "Price": "$1200"},
    {"Item": "Laptop", "Quantity": "2", "Price": "$1200"},
    {"Item": "Monitor", "Quantity": "3", "Price": "$300"},
    {"Item": "Keyboard", "Quantity": "5", "Price": "$50"},
    {"Item": "Laptop", "Quantity": "2", "Price": "$1200"},
    {"Item": "Laptop", "Quantity": "2", "Price": "$1200"},
    {"Item": "Monitor", "Quantity": "3", "Price": "$300"},
    {"Item": "Keyboard", "Quantity": "5", "Price": "$50"},
    {"Item": "Laptop", "Quantity": "2", "Price": "$1200"},
    {"Item": "Laptop", "Quantity": "2", "Price": "$1200"},
    {"Item": "Monitor", "Quantity": "3", "Price": "$300"},
    {"Item": "Keyboard", "Quantity": "5", "Price": "$50"},
    {"Item": "Laptop", "Quantity": "2", "Price": "$1200"},
    {"Item": "Laptop", "Quantity": "2", "Price": "$1200"},
    {"Item": "Monitor", "Quantity": "3", "Price": "$300"},
    {"Item": "Keyboard", "Quantity": "5", "Price": "$50"},
    {"Item": "Laptop", "Quantity": "2", "Price": "$1200"},
    {"Item": "Laptop", "Quantity": "2", "Price": "$1200"},
    {"Item": "Monitor", "Quantity": "3", "Price": "$300"},
    {"Item": "Keyboard", "Quantity": "5", "Price": "$50"},
    {"Item": "Laptop", "Quantity": "2", "Price": "$1200"},
    {"Item": "Laptop", "Quantity": "2", "Price": "$1200"},
    {"Item": "Monitor", "Quantity": "3", "Price": "$300"},
    {"Item": "Keyboard", "Quantity": "5", "Price": "$50"},
    {"Item": "Laptop", "Quantity": "2", "Price": "$1200"},
    {"Item": "Laptop", "Quantity": "2", "Price": "$1200"},
    {"Item": "Monitor", "Quantity": "3", "Price": "$300"},
    {"Item": "Keyboard", "Quantity": "5", "Price": "$50"},
    {"Item": "Laptop", "Quantity": "2", "Price": "$1200"},
]


# Escape special LaTeX characters like $
def escape_latex(text):
    return text.replace("$", r"\$")


# Generate dynamic table rows
def generate_table_rows(data):
    rows = []
    for row in data:
        row_tex = f"{escape_latex(row['Item'])} & {escape_latex(row['Quantity'])} & {escape_latex(row['Price'])} \\\\"
        rows.append(row_tex)
    return "\n".join(rows)


# Fill the LaTeX template with context and table data
def fill_template(template_path, output_path, replacements, table_rows):
    with open(template_path, 'r') as file:
        content = file.read()

    content = content.replace("{{table_rows}}", table_rows)

    for key, value in replacements.items():
        content = content.replace(f"{{{{{key}}}}}", value)

    with open(output_path, 'w') as file:
        file.write(content)


# Compile the LaTeX file to PDF
def compile_pdf(tex_path, output_dir):
    subprocess.run(["pdflatex", "-interaction=nonstopmode", "-output-directory", output_dir, tex_path], check=True)


# Clean temporary files
def clean_aux_files(output_dir):
    for ext in [".aux", ".log", ".out", ".toc"]:
        try:
            os.remove(os.path.join(output_dir, "generated" + ext))
        except FileNotFoundError:
            pass


# Main execution
def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    table_rows = generate_table_rows(table_data)
    fill_template(TEMPLATE_FILE, TEMP_TEX_FILE, context, table_rows)
    compile_pdf(TEMP_TEX_FILE, OUTPUT_DIR)
    clean_aux_files(OUTPUT_DIR)
    print(f"✅ PDF generated at: {os.path.join(OUTPUT_DIR, 'generated.pdf')}")


if __name__ == "__main__":
    main()
    
# --------------------------------------- Dependencies
# pip install lorem --break-system-packages
# sudo apt install texlive-latex-base texlive-latex-extra texlive-fonts-recommended
