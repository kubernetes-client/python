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
    prefix = '.' * (depth + 1)
    
    # 1. from kubernetes_asyncio.X.Y import Z to from ..X.Y import Z
    new_content = re.sub(r'from kubernetes_asyncio\.(\w+)\.', r'from ' + prefix + r'\1.', content)
    
    # 2. from kubernetes_asyncio.X import Y to from ..X import Y
    new_content = re.sub(r'from kubernetes_asyncio\.(\w+) ', r'from ' + prefix + r'\1 ', new_content)
    
    # 3. from kubernetes_asyncio import X to from .. import X
    new_content = re.sub(r'from kubernetes_asyncio import ', f'from {prefix} import ', new_content)
    
    # 4. import kubernetes_asyncio.X to from .. import X
    new_content = re.sub(r'^import kubernetes_asyncio\.(\w+)$', r'from ' + prefix + r' import \1', new_content, flags=re.MULTILINE)

    # 5. Inline usage: kubernetes_asyncio.X.Y to X.Y
    new_content = re.sub(r'kubernetes_asyncio\.(\w+)\.', r'\1.', new_content)
    
    if new_content != content:
        with open(filepath, 'w') as f:
            f.write(new_content)

if __name__ == '__main__':
    base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../kubernetes_asyncio'))
    for root, dirs, files in os.walk(base_dir):
        for file in files:
            if file.endswith('.py'):
                convert_imports_in_file(os.path.join(root, file))
