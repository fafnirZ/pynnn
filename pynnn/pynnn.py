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
from typing import Optional

from pynnn.mixins import NNNArgMixin, TempFilePathMixin

NNN_RELEASE_URL = "https://github.com/jarun/nnn/releases"


PYNNN_DEBUG = os.getenv("PYNNN_DEBUG", None)

class PyNNN(
    NNNArgMixin,
    TempFilePathMixin,
):
    """
    Attributes:
        executable_path (Path): Path to the nnn executable.
        initial_dir (Path): Initial directory for nnn to start in.
    """

    def __init__(
        self,
        executable_path: Optional[str | Path] = None,
        initial_dir: Optional[str | Path] = None,
    ):
        self.__handle_executable_path(
            executable_path=executable_path
        )
        self.__handle_initial_dir(
            initial_dir=initial_dir
        )

    def __handle_executable_path(self, *, executable_path: str | Path):
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
    
    def __handle_initial_dir(self, *, initial_dir: Optional[str | Path]):
        if initial_dir:
            self.initial_dir = Path(initial_dir)
        else:
            self.initial_dir = Path(os.getcwd())
        

    def __make_nnn_command(self) -> tuple[str, Path]:
        flags: str = self.nnn_mode__pipe_results_to_stdout()
        output_file: Path = self.new_temp_file_path()
        output_file_str = str(output_file)
        initial_dir_str = str(self.initial_dir)
        command: str = (
            f"{self.executable_path} {initial_dir_str} {flags} > {output_file_str}"
        )
        if PYNNN_DEBUG:
            print(f"Command: {command}")
        
        return command, output_file

    def __run(self) -> Path:
        # create command
        command, output_file_path = self.__make_nnn_command()

        # execute
        try:
            os.system(command)
            with open(output_file_path, "r") as file:
                results = file.read().strip()
                return Path(results)
        finally:
            if output_file_path.is_file():
                output_file_path.unlink()
                if PYNNN_DEBUG:
                    print(f"Deleted temp file: {output_file_path}")


    def __call__(self) -> Path:
        return self.__run()
