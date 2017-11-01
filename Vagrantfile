# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure("2") do |config|
  # Every Vagrant development environment requires a box. You can
  # search for boxes at https://vagrantcloud.com/search.
  config.vm.box = "hashicorp/precise32"

  # Forward X11 Connections
  config.ssh.forward_x11 = true

  # Forward Default AIT command port (UDP/3075) to
  # cFS Command Ingest (CI) Application port (UDP/1234)
  config.vm.network "forwarded_port", guest: 1234, host: 3075, host_ip: "127.0.0.1", protocol: 'udp'

  config.vm.provision "file", source: "script/cfe-run.sh", destination: "cfe-run.sh"
  config.vm.provision "file", source: "script/udp-mux.py", destination: "udp-mux.py"

  config.vm.provision "shell", inline: <<-SHELL
    chmod a+x cfe-run.sh
    chmod a+x udp-mux.py
  SHELL

  config.vm.provision "shell", inline: <<-SHELL
    apt-get update
    apt-get install -y git make
    apt-get install -y python-qt4 pyqt4-dev-tools python-qt4-dev python-zmq
    apt-get install -y libicu48
  SHELL

  config.vm.provision "shell", privileged: false, inline: <<-SHELL
    git clone https://github.com/nasa/cFE.git
    cd cFE
    git submodule init
    git submodule update
  SHELL

  config.vm.provision "shell", privileged: false, inline: <<-SHELL
    cd cFE
    source setvars.sh
    cd build/cpu1
    make config
    make
  SHELL

  config.vm.provision "shell", privileged: false, inline: <<-SHELL
    cd ${HOME}/cFE/tools/cFS-GroundSystem
    patch < /vagrant/script/patch/RoutingService.py.patch

    cd ${HOME}/cFE/tools/cFS-GroundSystem/Subsystems/cmdUtil
    patch < /vagrant/script/patch/cmdUtil.c.patch
    make
  SHELL
end
