import os

class CodebaseScanner:

    """

    Maps the AURA project structure.

    """

    def __init__(self, root):

        self.root = root

    def scan(self):

        structure = []

        for path, dirs, files in os.walk(

            self.root

        ):

            for file in files:

                structure.append(

                    os.path.join(

                        path,

                        file

                    )

                )

        return {

            "root": self.root,

            "files_found": len(structure),

            "files": structure

        }