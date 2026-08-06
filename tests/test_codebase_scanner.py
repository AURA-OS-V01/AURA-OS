from core.development.codebase_scanner import (

    CodebaseScanner

)

def test_scanner():

    scanner = CodebaseScanner(

        "."

    )

    result = scanner.scan()

    print("Codebase Scanner Test")

    print("--------------------")

    print(

        result["files_found"]

    )

if __name__ == "__main__":

    test_scanner()