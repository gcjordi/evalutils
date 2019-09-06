# -*- coding: utf-8 -*-
import os
import shutil
from pathlib import Path
from evalutils.utils import (
    bootstrap_development_distribution,
    convert_line_endings,
)


PROCESSOR_NAME = "{{ cookiecutter.processor_name }}"
IS_DEV_BUILD = {{cookiecutter.dev_build}} == 1

template_dir = Path(os.getcwd())

templated_python_files = template_dir.glob("*.py.j2")
for f in templated_python_files:
    shutil.move(f.name, f.stem)


convert_line_endings()

if IS_DEV_BUILD:
    bootstrap_development_distribution(
        PROCESSOR_NAME, template_dir / "devdist"
    )
