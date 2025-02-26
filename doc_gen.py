import os
import shutil
import subprocess
import webbrowser
import time
import argparse

parser = argparse.ArgumentParser(description='Generate and optionally view Sphinx documentation.')
parser.add_argument('-v', '--view', action='store_true', help='View the generated documentation in a web browser')

# Define the docs directory
docs_dir = '_build'

# Regenerate the Sphinx documentation
subprocess.run(['make', 'html'])

# add nojekyll in build root folder.
with open(os.path.join(docs_dir, '.nojekyll'), 'w') as f:
    pass

# Open the generated documentation in a web browser
webbrowser.open(f'file://{os.path.abspath(os.path.join(docs_dir, "html", "index.html"))}')