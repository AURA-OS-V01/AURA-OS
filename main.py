
from core.runtime.aura_runtime_manager import (

    AURARuntimeManager

)

from core.runtime.aura_control_center import (

    AURAControlCenter

)

from core.console.aura_console import (

    AURAConsole

)

def main():

    runtime = AURARuntimeManager()

    boot = runtime.boot()

    dashboard = AURAControlCenter()

    dashboard.render(

        boot

    )

    console = AURAConsole(

        runtime.missions

    )

    console.start()

if __name__ == "__main__":

    main()

