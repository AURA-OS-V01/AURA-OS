
from core.runtime.aura_runtime_manager import AURARuntimeManager

from core.runtime.aura_control_center import AURAControlCenter

def main():

    runtime = AURARuntimeManager()

    boot = runtime.boot()

    dashboard = AURAControlCenter()

    dashboard.render(boot)

if __name__ == "__main__":

    main()

