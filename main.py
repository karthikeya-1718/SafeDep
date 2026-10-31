"""SafeDep Workspace Launcher.

Forwards execution to SafeDep/main.py so running `python main.py`
from either the workspace root or the SafeDep folder works seamlessly.
"""

import os
import runpy
import sys

project_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "SafeDep")
if project_dir not in sys.path:
    sys.path.insert(0, project_dir)

if __name__ == "__main__":
    target_main = os.path.join(project_dir, "main.py")
    runpy.run_path(target_main, run_name="__main__")

