from uuid import uuid4

from datetime import datetime

class BackupRecoverySystem:

    """

    Manages AURA backup and recovery records.

    """

    def __init__(self):

        self.backups = []

    def create_backup(

        self,

        name,

        backup_type,

        status

    ):

        backup = {

            "id": str(uuid4()),

            "name": name,

            "backup_type": backup_type,

            "status": status,

            "created":

                datetime.utcnow().isoformat()

        }

        self.backups.append(backup)

        return backup

    def get_backups(self):

        return self.backups