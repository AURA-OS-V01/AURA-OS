from core.security.audit_logging_system_v01 import (

    AuditLoggingSystem

)

def test_audit_logging():

    system = AuditLoggingSystem()

    result = system.record_event(

        "admin_user",

        "Created workspace",

        "Security"

    )

    print("Audit Logging Test")

    print("------------------")

    print(result)

if __name__ == "__main__":

    test_audit_logging()