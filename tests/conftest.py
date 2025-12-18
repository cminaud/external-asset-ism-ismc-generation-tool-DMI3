import os
import sys
import pytest


@pytest.fixture(scope="session", autouse=True)
def add_project_root_to_sys_path():
    current_file_path = os.path.abspath(__file__)
    current_path = os.path.dirname(current_file_path)
    project_root = os.path.abspath(os.path.join(current_path, ".."))
    sys.path.append(project_root)
