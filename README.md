# AMMOS Instrument Toolkit (AIT) and NASA Core Flight Software (cFS)

## Quickstart

    # Install ait.cfs Python package (in developer mode)
    $ pip install -e . --process-dependency-links

    # Start (and provision, first boot only) the cFS VM
    $ vagrant up

    # Terminal 1 - Boot cFE
    $ vagrant ssh

    vagrant@precise32:~$ ./cfe-run.sh


    # Terminal 2 - Start cFS Ground System
    $ vagrant ssh

    vagrant@precise32:~$ cd cFE/tools/cFS-GroundSystem/
    vagrant@precise32:~$ python GroundSystem.py


    # Terminal 3 - Start AIT GUI
    $ ait-gui

You can enable cFS telemetry output via the AIT GUI or command-line,
e.g.:

    $ ait-cmd-send CFS_TO_OUTPUT_ENABLE 127.0.0.1

You can also send a cFE a CFS_ES_NO_OP command:

    $ ait-cmd-send CFS_ES_NO_OP
