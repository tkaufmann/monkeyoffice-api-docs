#!/usr/bin/env python3
# ABOUTME: Splits large Markdown file into individual endpoint files
# ABOUTME: Creates structured files based on H2 sections for better LLM consumption

import re
import json
import os
from pathlib import Path

def split_markdown_by_sections(markdown_file, output_dir, structure_file):
    """Split markdown file into individual sections based on H2 headings."""
    
    with open(markdown_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    with open(structure_file, 'r', encoding='utf-8') as f:
        structure = json.load(f)
    
    # Find H2 sections (main API modules)
    h2_sections = [item for item in structure if item['level'] == 2]
    
    # Split content by H2 headings
    sections = re.split(r'^## ', content, flags=re.MULTILINE)
    
    files_created = []
    
    # Handle first section (before first H2) - this contains overview/intro
    if sections[0].strip():
        overview_file = Path(output_dir) / "overview.md"
        with open(overview_file, 'w', encoding='utf-8') as f:
            f.write(sections[0].strip())
        files_created.append({"title": "Overview", "filename": "overview.md"})
    
    # Process each H2 section
    for i, section in enumerate(sections[1:], 1):
        if not section.strip():
            continue
            
        # Extract title from first line and add back the ##
        lines = section.split('\n')
        title = lines[0].strip()
        section_content = f"## {section}"
        
        # Create filename-safe version
        filename = re.sub(r'[^\w\s-]', '', title.lower())
        filename = re.sub(r'[-\s]+', '-', filename).strip('-')
        filename = f"{filename}.md"
        
        # Write section to file
        section_file = Path(output_dir) / filename
        with open(section_file, 'w', encoding='utf-8') as f:
            f.write(section_content)
        
        files_created.append({"title": title, "filename": filename})
        print(f"Created: {filename}")
    
    return files_created

if __name__ == "__main__":
    output_dir = "docs/v22.1.1/endpoints"
    os.makedirs(output_dir, exist_ok=True)
    
    files = split_markdown_by_sections(
        "docs/v22.1.1/api-reference.md",
        output_dir,
        "html_structure.json"
    )
    
    # Save file list for llms.txt generation
    with open('endpoint_files.json', 'w', encoding='utf-8') as f:
        json.dump(files, f, indent=2, ensure_ascii=False)
    
    print(f"\nCreated {len(files)} endpoint files in {output_dir}")