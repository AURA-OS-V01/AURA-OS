from core.integrations.storage.aura_cloud_storage_integration_v01 import (

    AURACloudStorageIntegration

)

def test_cloud_storage_integration():

    storage = AURACloudStorageIntegration()

    provider = storage.connect_provider(

        "Google Drive",

        "aura_business_account"

    )

    file = storage.upload_file(

        provider["id"],

        "client_proposal.pdf",

        "document"

    )

    print(

        "AURA Cloud Storage Integration Test"

    )

    print(provider)

    print(file)

    assert provider["status"] == "connected"

    assert file["status"] == "stored"

if __name__ == "__main__":

    test_cloud_storage_integration()