#!/usr/bin/env python3
# ABOUTME: Analyzes HTML structure to identify API endpoints and sections
# ABOUTME: Extracts headings and creates structured endpoint mapping

import re
from bs4 import BeautifulSoup
import json

def analyze_html_structure(html_file):
    """Analyze HTML structure to identify endpoints and sections."""
    with open(html_file, 'r', encoding='utf-8') as f:
        html_content = f.read()
    
    soup = BeautifulSoup(html_content, 'html.parser')
    
    # Extract title and version
    title = soup.find('title')
    if title:
        print(f"Title: {title.get_text()}")
    
    # Find all headings to understand structure
    headings = soup.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6'])
    
    endpoints = []
    current_section = None
    
    for heading in headings:
        text = heading.get_text().strip()
        level = int(heading.name[1])
        
        # Skip empty headings
        if not text:
            continue
            
        # Create filename-safe version
        filename = re.sub(r'[^\w\s-]', '', text.lower())
        filename = re.sub(r'[-\s]+', '-', filename).strip('-')
        
        endpoint_info = {
            'title': text,
            'level': level,
            'filename': f"{filename}.md",
            'element_id': heading.get('id', ''),
            'class': heading.get('class', [])
        }
        
        endpoints.append(endpoint_info)
        
        if level <= 2:
            current_section = text
        
        print(f"H{level}: {text} -> {filename}.md")
    
    return endpoints

if __name__ == "__main__":
    endpoints = analyze_html_structure('moapi.html')
    
    # Save structure info
    with open('html_structure.json', 'w', encoding='utf-8') as f:
        json.dump(endpoints, f, indent=2, ensure_ascii=False)
    
    print(f"\nFound {len(endpoints)} headings/endpoints")