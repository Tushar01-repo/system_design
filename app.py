
from flask import Flask, render_template, abort
from pathlib import Path
import markdown
import html
import os

app = Flask(__name__, template_folder="templates", static_folder="static")
BASE_DIR = Path(__file__).resolve().parent

# Define all folders to scan
CONTENT_FOLDERS = [
    "classes_and_objects",
    "solid_principles",
    "abstract_factory",
    "builder_pattern",
    "facade_pattern",
    "chain_of_responsibility",
    "strategy_design_pattern"
]

def get_sidebar_structure():
    """Return folder structure with files from all content folders"""
    structure = []
    
    for folder_name in CONTENT_FOLDERS:
        folder_path = BASE_DIR / folder_name
        
        if folder_path.exists() and folder_path.is_dir():
            # Get all files in this folder
            files = sorted([f for f in os.listdir(folder_path) if os.path.isfile(folder_path / f)])
            
            if files:  # Only add if folder has files
                # Group files by type
                readme_files = [f for f in files if f.endswith('.md')]
                py_files = [f for f in files if f.endswith('.py')]
                
                structure.append({
                    "folder": folder_name.replace('_', ' ').title(),
                    "folder_key": folder_name,
                    "files": {
                        "markdown": readme_files,
                        "python": py_files
                    }
                })
    
    return structure

def get_all_files():
    """Get a flat list of all available files with their folders"""
    files = {}
    structure = get_sidebar_structure()
    
    for item in structure:
        for file_type, file_list in item["files"].items():
            for file in file_list:
                # Use folder/filename as key to avoid conflicts
                file_key = f"{item['folder_key']}/{file}"
                files[file_key] = item["folder_key"]
    
    return files

def read_file(folder_key: str, name: str):
    """Read and return file content from specific folder"""
    folder_path = BASE_DIR / folder_key
    file_path = folder_path / name
    
    if not file_path.exists() or not file_path.is_file():
        abort(404)
    
    text = file_path.read_text(encoding='utf-8', errors='replace')
    
    # Markdown for readme, syntax highlight for code
    if name.endswith('.md'):
        html_content = markdown.markdown(text, extensions=["fenced_code", "tables", "toc"])
        return {"type": "markdown", "content": html_content, "name": name}
    else:
        # Return code in <pre><code> for editor display
        code_html = '<pre><code class="language-python">{}</code></pre>'.format(html.escape(text))
        return {"type": "code", "content": code_html, "name": name}

@app.route('/')
def index():
    sidebar_structure = get_sidebar_structure()
    
    # Load first markdown file from first folder
    first_file = None
    first_folder = None
    
    for section in sidebar_structure:
        if section["files"]["markdown"]:
            first_file = section["files"]["markdown"][0]
            first_folder = section["folder_key"]
            break
    
    if first_file and first_folder:
        file_data = read_file(first_folder, first_file)
        active_file = f"{first_folder}/{first_file}"
    else:
        file_data = {"type": "markdown", "content": "<h1>No files found</h1>", "name": ""}
        active_file = ""
    
    return render_template('index.html', 
                         file_data=file_data, 
                         sidebar=sidebar_structure, 
                         active_file=active_file)

@app.route('/file/<folder>/<name>')
def file_view(folder, name):
    sidebar_structure = get_sidebar_structure()
    file_data = read_file(folder, name)
    
    return render_template('index.html', 
                         file_data=file_data, 
                         sidebar=sidebar_structure, 
                         active_file=f"{folder}/{name}")

if __name__ == '__main__':
    app.run(debug=True)