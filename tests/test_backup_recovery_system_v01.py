from core.deployment.backup_recovery_system_v01 import (

    BackupRecoverySystem

)

def test_backup_recovery():

    system = BackupRecoverySystem()

    result = system.create_backup(

        "AURA Workspace Data",

        "Daily Snapshot",

        "Completed"

    )

    print("Backup Recovery Test")

    print("--------------------")

    print(result)

if __name__ == "__main__":

    test_backup_recovery()