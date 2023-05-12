import os
import pytest
from os_path_scripts import TMP_PATH

@pytest.fixture(scope = 'module',autouse = True)
def set_up_directory():
    if not os.path.exists(TMP_PATH):
        os.mkdir(TMP_PATH)
    yield
    shutil.rmtree(TMP_PATH)