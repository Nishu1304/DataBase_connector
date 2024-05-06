import os
from pathlib import Path

package_name = 'mongodb_connect'

list_of_files = [
    '.github/workflows/ci.yaml',
    'src/__init__.py',
    f'src/{package_name}/__init__.py',
    f'src/{package_name}/mongo_crud.py',
    'test/__init__.py',
    'test/unit/__init__.py',
    'test/unit/test_unit.py',
    'test/integration/__init__.py',
    'test/integration/test_int.py',
    'init_setup.sh',
    'requirements.txt',
    'requirements_dev.txt',
    'setup.py',
    'setup.cfg',
    'pyproject.toml',
    'tox.ini',
    'experiment/experiments.ipynb'
]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)

    # Check if the file doesn't exist or is empty
    if not filepath.exists() or filepath.stat().st_size == 0:
        # Open the file with 'w' mode to write content to it
        with open(filepath, 'w') as f:
            # Write some content to the file (e.g., 'Hello, world!')
            pass

