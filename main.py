import typer
import json
import os
from typing import List, Optional

app = typer.Typer()

@app.command()
def generate_sections(
    sections_to_generate: List[str] = typer.Option(["*"], "--sections", "-s", help="Sections to generate (e.g. events, awards)"),
    tags_to_generate: List[str] = typer.Option(["*"], "--tag", "-t", help="Tags to filter content (e.g. AI, Python)")
):
    """Generate .tex files for specified sections based on tags"""
    
    os.makedirs("build", exist_ok=True)

    # Split comma-separated values if present
    sections_to_generate = [
        section.strip().lower() 
        for sections in sections_to_generate 
        for section in sections.split(',')
    ]
    tags_to_generate = [
        tag.strip().lower() 
        for tags in tags_to_generate 
        for tag in tags.split(',')
    ]
    # aways keep the relevants
    tags_to_generate.append("relevant")
    if "*" in sections_to_generate:
        sections_to_generate = [
            "events",
            "awards",
            "projects",
            "attachments",
        ]

    # Load sections data
    try:
        with open("sections/index.json", "r") as f:
            sections_data = json.load(f)
    except FileNotFoundError:
        typer.echo("Error: sections/index.json not found")
        raise typer.Exit(1)

    # Process each requested section
    for section in sections_to_generate:
        if section in ["awards", "attachments"]:
            import shutil
            shutil.copy(f"sections/{section}.tex", f"build/{section}.tex")
            continue
    
        if section not in sections_data:
            typer.echo(f"Warning: Section '{section}' not found in index.json")
            continue

        # Filter items by tags
        filtered_items = []
        for item in sections_data[section]:
            # Include item if no tags specified or if any specified tag matches item's tags
            item_tags = item.get("tags", [])
            if "*" in tags_to_generate or not tags_to_generate:
                should_include = True
            else:   
                should_include = any(tag in item_tags for tag in tags_to_generate)
            if should_include:
                filtered_items.append(item)

        # Generate .tex content
        tex_content = f"% Auto-generated {section} section\n\n"
        for item in filtered_items:
            with open(f"sections/{section}/{item['file']}", "r") as f:
                tex_content += f.read()

        # Create and write .tex file
        filename = f"build/{section}.tex"
        try:
            with open(filename, "w") as f:
                f.write(tex_content)
            typer.echo(f"Generated {filename}")
        except Exception as e:
            typer.echo(f"Error writing {filename}: {str(e)}")

    # Build latex file
    os.system("latexmk -pdf -outdir=build main.tex")
    # Clean up build files
    os.system("latexmk -c")
    os.system("rm -rf build")
# Run the app
if __name__ == "__main__":
    app()
