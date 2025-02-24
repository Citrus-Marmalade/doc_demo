import os
import shutil
import subprocess
import webbrowser
import time
import argparse

parser = argparse.ArgumentParser(description='Generate and optionally view Sphinx documentation.')
parser.add_argument('-v', '--view', action='store_true', help='View the generated documentation in a web browser')

# Define the docs directory
docs_dir = 'docs'

# Clean the docs directory
if os.path.exists(docs_dir):
    shutil.rmtree(docs_dir)
os.makedirs(docs_dir)

# Regenerate the Sphinx documentation
subprocess.run(['sphinx-build', '-b', 'html', '.', docs_dir])

# Open the generated documentation in a web browser
index_path = os.path.join(docs_dir, 'index.html')
args = parser.parse_args()

if args.view:
    webbrowser.open(f'file://{os.path.abspath(index_path)}')