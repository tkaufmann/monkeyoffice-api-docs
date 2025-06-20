# MonKey Office Connect JSON-API Documentation

LLM-optimized documentation for MonKey Office Connect JSON-API, structured for efficient machine consumption.

## 🚀 Quick Start for LLMs

**Entry Point:** [`llms.txt`](https://raw.githubusercontent.com/tkaufmann/monkeyoffice-api-docs/main/llms.txt)

This lightweight file (3.3KB) provides direct links to all API endpoints, allowing LLMs to access only the relevant documentation sections.

## 📁 Structure

```
docs/
└── v22.1.1/
    ├── api-reference.md      # Complete API documentation
    ├── moapi.html           # Original HTML source
    └── endpoints/           # Individual endpoint files
        ├── adressen.md
        ├── firmen.md
        ├── verkaufsbelege.md
        └── ... (18 endpoints total)
```

## 🎯 Purpose

**Problem:** Large HTML documentation files consume excessive LLM tokens and lack version control.

**Solution:** 
- **Lightweight Access:** llms.txt provides overview + direct links to specific endpoints
- **Version Control:** Each API version gets its own directory and Git tag
- **LLM-Optimized:** Structured Markdown files for efficient parsing

## 🔗 API Endpoints

The API covers these main areas:
- **Firmen** (Companies)
- **Adressen** (Addresses) 
- **Artikel und Leistungen** (Products & Services)
- **Verkaufsbelege** (Sales Documents)
- **Einkaufsbelege** (Purchase Documents)
- **Buchungen** (Bookings)
- **Debitoren/Kreditoren** (Debtors/Creditors)
- And more...

Each endpoint file contains:
- Data structures
- Available functions/methods
- Parameters and return values
- Examples

## 🔄 Version Management

- **Current Version:** v22.1.1 (June 2025)
- **Git Tags:** Each version tagged (e.g., `v22.1.1`)
- **Immutable:** Published versions remain unchanged
- **New Versions:** Added as separate directories

## 🛠️ Automation Scripts

Included Python scripts for processing new API versions:

- `analyze_html.py` - Extract structure from HTML
- `split_markdown.py` - Split into endpoint files  
- `generate_llms_txt.py` - Create LLM entry point

## 📝 Usage Examples

### For LLMs
1. Load `llms.txt` for overview
2. Access specific endpoint via direct GitHub raw link
3. Process only relevant sections

### For Developers
```bash
# Clone repository
git clone https://github.com/tkaufmann/monkeyoffice-api-docs.git

# View specific endpoint
curl https://raw.githubusercontent.com/tkaufmann/monkeyoffice-api-docs/main/docs/v22.1.1/endpoints/firmen.md
```

## 🔄 Contributing New Versions

When a new API version is released:

1. Run automation scripts with new HTML file
2. Create new version directory
3. Update llms.txt  
4. Commit with version tag
5. Push to GitHub

## 📊 Token Efficiency

- **Before:** Loading complete HTML (~643KB)
- **After:** Loading llms.txt overview (3.3KB) + relevant endpoint (~10-50KB)
- **Savings:** 90%+ token reduction for targeted queries

---

**Original API Version:** 22.1.1 (16.06.25)  
**Documentation Generated:** 2025-06-20