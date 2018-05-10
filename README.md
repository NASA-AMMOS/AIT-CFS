# AMMOS Instrument Toolkit (AIT) and NASA Core Flight Software (cFS)

## Quickstart

    # Install bliss.cfs Python package (in developer mode)
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
    $ bliss-gui

You can enable cFS telemetry output via the AIT GUI or command-line,
e.g.:

    $ bliss-cmd-send CFS_TO_OUTPUT_ENABLE 127.0.0.1

You can also send a cFE a CFS_ES_NO_OP command:

    $ bliss-cmd-send CFS_ES_NO_OP


# Join the Community

The project's [User and Developer Mailing List](https://groups.google.com/forum/#!forum/ait-dev>) is the best way to communicate with the team, ask questions, brainstorm plans for future changes, and help contribute to the project.

This project exists thanks to the dedicated users, contributors, committers, and project management committee members. If you'd like to learn more about how the project is organized and how to become a part of the team please check out the [Project Structure and Governance](https://github.com/NASA-AMMOS/AIT-Core/wiki/Project-Structure-and-Governance>) documentation.

# Contributing

For information on how to contribute please see the [AIT Contributing Guide](https://github.com/NASA-AMMOS/AIT-Core/wiki/Contributing>)
