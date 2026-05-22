import os
import re

def convert_imports_in_file(filepath):
    with open(filepath, 'r') as f:
        content = f.read()

    # Determine relative depth
    parts = filepath.split('kubernetes_asyncio/')
    if len(parts) < 2:
        return
        
    subpath = parts[1]
    depth = subpath.count('/')
    
    # If it's a top-level file like api_client.py, depth is 0, so prefix is '.'
    # If it's in client/api/, depth is 2, so prefix is '..'
    prefix = '.' * depth if depth > 0 else '.'
    
    # Simple regex to replace absolute imports
    # from kubernetes_asyncio.client.X import Y -> from ..X import Y
    new_content = re.sub(r'from kubernetes_asyncio\.client\.', f'from {prefix}.', content)
    new_content = re.sub(r'from kubernetes_asyncio\.client ', f'from {prefix} ', new_content)
    new_content = re.sub(r'import kubernetes_asyncio\.client\.(\w+)', r'from ' + prefix + r' import \1', new_content)
    
    if new_content != content:
        with open(filepath, 'w') as f:
            f.write(new_content)

if __name__ == '__main__':
    base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../kubernetes_asyncio'))
    for root, dirs, files in os.walk(base_dir):
        for file in files:
            if file.endswith('.py'):
                convert_imports_in_file(os.path.join(root, file))
