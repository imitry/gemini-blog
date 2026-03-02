import os
import glob

def replace_in_file(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
    except UnicodeDecodeError:
        return # skip binary or non-utf8 files

    # The order matters here! 
    # Do more specific ones first to avoid double replacements.
    replacements = {
        'gemini-blog': 'gemini-blog',
        'Gemini CLI': 'Gemini CLI',
        'Gemini': 'Gemini',
        'gemini': 'gemini',
        '.gemini/': '.gemini/',
        '.gemini': '.gemini'
    }

    new_content = content
    for old, new in replacements.items():
        new_content = new_content.replace(old, new)
        
    if new_content != content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Updated {filepath}")

def main():
    directory = r"c:\Users\todor\Desktop\gplayground\gemini-blog"
    
    # Supported extensions
    extensions = ['*.md', '*.txt', '*.sh', '*.ps1', '*.py', '*.json', '*.yaml', '*.yml']
    
    # We will search recursively
    for ext in extensions:
        pattern = os.path.join(directory, '**', ext)
        for filepath in glob.glob(pattern, recursive=True):
            if '.git' in filepath:
                continue
            replace_in_file(filepath)
            
    # Also handle files without extension like `LICENSE`
    files = ['LICENSE']
    for filename in files:
        filepath = os.path.join(directory, filename)
        if os.path.exists(filepath):
            replace_in_file(filepath)

if __name__ == '__main__':
    main()
