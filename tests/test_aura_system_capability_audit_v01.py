from pathlib import Path

CAPABILITIES = {

    "Memory": [

        "core/intelligence/memory"

    ],

    "Research": [

        "core/testing/research_mode_validation_v01.py"

    ],

    "Prediction": [

        "core/intelligence/prediction"

    ],

    "Planning": [

        "core/planning",

        "core/agents/planning"

    ],

    "Strategy": [

        "core/intelligence/strategy"

    ],

    "Decision": [

        "core/decision",

        "core/governance"

    ],

    "Runtime": [

        "core/runtime"

    ],

    "Evolution": [

        "core/evolution"

    ],

    "Self Builder": [

        "core/self_builder"

    ],

    "Code Generation": [

        "core/development/generation"

    ],

    "Testing": [

        "core/testing"

    ],

    "Approval System": [

        "core/evolution/approval",

        "core/governance/approval_gate.py"

    ],

    "Deployment": [

        "core/deployment"

    ]

}

def check_exists(paths):

    for path in paths:

        if Path(path).exists():

            return True

    return False

def run_audit():

    print("\nAURA CAPABILITY AUDIT")

    print("=" * 50)

    found = 0

    total = len(CAPABILITIES)

    for name, paths in CAPABILITIES.items():

        status = check_exists(paths)

        if status:

            found += 1

        print(f"{'✅' if status else '❌'} {name}")

    print("=" * 50)

    print(f"{found}/{total} capability systems detected")

if __name__ == "__main__":

    run_audit()