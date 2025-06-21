#!/usr/bin/env python3
# ABOUTME: Generates llms.txt file for LLM consumption with GitHub raw links
# ABOUTME: Creates structured overview of all API endpoints for efficient LLM access

import json
import os

def generate_llms_txt(endpoint_files, repo_url, version):
    """Generate llms.txt with GitHub raw links to all endpoint files."""
    
    # GitHub raw URL pattern
    base_raw_url = repo_url.replace('github.com', 'raw.githubusercontent.com') + '/main'
    
    llms_content = f"""# MonKey Office Connect JSON-API Referenz {version}

> Strukturierte API-Dokumentation für MonKey Office Connect, optimiert für Large Language Models. Enthält alle Endpunkte, Datenstrukturen und Funktionen der JSON-API.

## Vollständige API-Referenz
- [Original HTML]: {base_raw_url}/docs/{version}/moapi.html

## API-Endpunkte

Die API ist in folgende Hauptbereiche unterteilt:

"""
    
    # Sort files by title for better organization
    sorted_files = sorted(endpoint_files, key=lambda x: x.get('title', ''))
    
    for file_info in sorted_files:
        title = file_info.get('title', 'Untitled')
        filename = file_info.get('filename', '')
        
        if filename and title != 'Untitled':
            file_url = f"{base_raw_url}/docs/{version}/endpoints/{filename}"
            llms_content += f"- [{title}]: {file_url}\n"
    
    return llms_content

if __name__ == "__main__":
    # Load endpoint files
    with open('endpoint_files.json', 'r', encoding='utf-8') as f:
        endpoint_files = json.load(f)
    
    # Generate llms.txt
    repo_url = "https://github.com/tkaufmann/monkeyoffice-api-docs"
    version = "v22.1.1"
    
    llms_content = generate_llms_txt(endpoint_files, repo_url, version)
    
    # Write llms.txt to version directory
    output_path = f"docs/{version}/llms.txt"
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(llms_content)
    
    print("✓ Generated llms.txt")
    print(f"  {len(endpoint_files)} endpoints included")
    print(f"  File size: {len(llms_content)} characters")