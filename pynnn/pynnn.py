# Copyright (c) 2025 Jacky Xie
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

# inspiration from: https://github.com/nk412/pyfzf/blob/master/pyfzf/pyfzf.py
from pathlib import Path
from shutil import which
import os

NNN_RELEASE_URL = "https://github.com/jarun/nnn/releases"

class PyNNN:
    executable_path: Path

    def __init__(self, executable_path: str | Path = None):
        if executable_path:
            self.executable_path = Path(executable_path)
        elif not which("nnn") and not executable_path:
            raise SystemError(
                "nnn executable not found in PATH."
                "Please install nnn binary or provide the path to the executable."
                f"{NNN_RELEASE_URL}"
            )
        else:
            self.executable_path = Path(which("nnn"))


    def __run(self, args: list[str], **kwargs) -> str:
        pass

    def __call__(self, args: list[str], **kwargs) -> str:
        pass

    