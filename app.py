
from flask import Flask, render_template, abort
from pathlib import Path
import markdown
import html

app = Flask(__name__, template_folder="templates", static_folder="static")
BASE_DIR = Path(__file__).resolve().parent
README_PATH = BASE_DIR / "readme.md"
MODULE_FILES = [f"module{i}.py" for i in range(1, 6)]

def get_sidebar_items():
    """Return list of sidebar items: readme.md + available modules"""
    items = ["readme.md"]
    items.extend([f for f in MODULE_FILES if (BASE_DIR / f).exists()])
    return items

def read_file(name: str):
    """Read and return file content with metadata"""
    allowed = get_sidebar_items()
    if name not in allowed:
        abort(404)
    
    candidate = BASE_DIR / name
    if not candidate.exists() or not candidate.is_file():
        abort(404)
    
    text = candidate.read_text(encoding='utf-8', errors='replace')
    
    # Markdown for readme, syntax highlight for code
    if name == "readme.md":
        html_content = markdown.markdown(text, extensions=["fenced_code", "tables", "toc"])
        return {"type": "markdown", "content": html_content, "name": name}
    else:
        # Return code in <pre><code> for editor display
        code_html = '<pre><code class="language-python">{}</code></pre>'.format(html.escape(text))
        return {"type": "code", "content": code_html, "name": name}

@app.route('/')
def index():
    sidebar = get_sidebar_items()
    file_data = read_file("readme.md")
    return render_template('index.html', file_data=file_data, sidebar=sidebar, active_file="readme.md")

@app.route('/file/<name>')
def file_view(name):
    sidebar = get_sidebar_items()
    file_data = read_file(name)
    return render_template('index.html', file_data=file_data, sidebar=sidebar, active_file=name)

if __name__ == '__main__':
    app.run(debug=True)