from pathlib import Path
from uuid import uuid4


class NNNArgMixin:
    @staticmethod
    def nnn_mode__pipe_results_to_stdout() -> str:
        """
        Pipe results to stdout.
        """
        return "-p -"


class TempFilePathMixin:
    @staticmethod
    def new_temp_file_path() -> Path:
        """
        Get the temporary file path.
        """
        short_uuid = str(uuid4())[:8]
        return Path(f"/tmp/nnn-out-{short_uuid}")
