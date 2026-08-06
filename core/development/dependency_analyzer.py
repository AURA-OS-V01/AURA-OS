import re

class DependencyAnalyzer:

    """

    Finds relationships between

    Python modules.

    """

    def __init__(self):

        self.dependencies = {}

    def analyze_file(

        self,

        filename,

        content

    ):

        imports = re.findall(

            r"^(?:from|import)\s+([a-zA-Z0-9_\.]+)",

            content,

            re.MULTILINE

        )

        self.dependencies[filename] = imports

        return {

            "file": filename,

            "dependencies": imports

        }

    def get_graph(self):

        return self.dependencies