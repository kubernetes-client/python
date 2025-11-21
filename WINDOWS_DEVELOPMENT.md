```markdown

\# Windows Development Guide



This guide helps Windows developers contribute to the Kubernetes Python Client.



---



\## 🧰 Prerequisites



\- Python 3.8+ (Recommended: Python 3.11+)

\- Git for Windows

\- PowerShell or Command Prompt



---



\## ⚙️ Setup for Windows Development



\### 1. Clone and setup the repository:



```bash

git clone https://github.com/your-username/kubernetes-client-python.git

cd kubernetes-client-python

python setup-windows-dev.py

```



\### 2. Install in development mode:



```bash

pip install -e .

pip install -r test-requirements.txt

```



\### 3. Run tests:



```bash

python -m pytest kubernetes/base/watch/watch\_test.py -v

```



---



\## 🐞 Known Windows Issues and Solutions



\### 🔗 Symlink Directories

\- \*\*Problem:\*\* `kubernetes/config` and `kubernetes/watch` are symlinks that don't work on Windows.

\- \*\*Solution:\*\* Run `python setup-windows-dev.py` to create proper directory copies.



\### ❌ Missing Imports

\- \*\*Problem:\*\* Some test files were missing `import json`.

\- \*\*Solution:\*\* Fixed in the codebase.



\### 🔒 Permission Errors

\- \*\*Problem:\*\* Temporary file creation fails with `PermissionError`.

\- \*\*Solution:\*\* Tests now handle Windows permissions gracefully.



---



\## 🤝 Contributing



When contributing from Windows:



1\. Always run the setup script first.

2\. Test your changes locally.

3\. Include Windows-specific considerations in your PRs.

```



