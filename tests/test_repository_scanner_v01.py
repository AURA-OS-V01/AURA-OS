from tools.repository_scanner_v01 import (

    RepositoryScanner

)

def test_repository_scanner():

    scanner = RepositoryScanner()

    result = scanner.scan(

        "."

    )

    print("Repository Scanner Test")

    print("----------------------")

    print(result["status"])

    print("Files found:",

          len(result["files"]))

if __name__ == "__main__":

    test_repository_scanner()