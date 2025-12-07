import os
import python_minifier

print('Minifying scripts for production.')

SCRIPTS_DIR = "./src"
OUTPUT_DIR = "./dist"

# Make sure the output directory exists
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Loop over all .py files in SCRIPTS_DIR
for filename in os.listdir(SCRIPTS_DIR):
    if filename.endswith(".py"):
        input_path = os.path.join(SCRIPTS_DIR, filename)
        output_path = os.path.join(OUTPUT_DIR, filename)  # keeps original name

        # Read the original file
        with open(input_path, "r", encoding="utf-8") as f:
            src = f.read()

        # Minify using python-minifier
        minified = python_minifier.minify(
            src,
            remove_literal_statements=True,  # removes docstrings
            rename_locals=True               # rename local variables/functions
        )

        # Write minified file
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(minified)

        print(f"Minified: {filename} -> {output_path}")

print("All scripts minified!")
