from core.development.dependency_analyzer import (

    DependencyAnalyzer

)

def test_dependency():

    analyzer = DependencyAnalyzer()

    result = analyzer.analyze_file(

        "agent.py",

        """

from core.memory import Memory

import tools.search

        """

    )

    print("Dependency Analyzer Test")

    print("-----------------------")

    print(result)

if __name__ == "__main__":

    test_dependency()