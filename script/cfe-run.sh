#!/bin/sh

trap 'kill -9 $(jobs -pr)' SIGINT SIGTERM EXIT

cd ${HOME}/cFE

source setvars.sh
cd build/cpu1/exe

echo "Send UDP telemetry to 127.0.0.1:1235 to have it multiplexed to"
echo "two destinations:"
echo
echo "    1.  The gateway running this VM (10.0.2.2:1236), and"
echo "    2.  localhost (127.0.0.1:1236)"
echo
echo "Destination (1) allows AIT running outside the VM to receive"
echo "telemetry, while (2) allows the cFS Python Ground System running in"
echo "the VM to receive telemetry."
echo
${HOME}/udp-mux.py 127.0.0.1:1235 10.0.2.2:1236 127.0.0.1:1236 &
PID=$!

trap "kill -9 $PID" INT TERM

echo
sleep 1

echo "Starting cFS.  Ctrl-C to exit."
echo "Logging cFS console messages to ${LOG}."
sudo ./core-linux.bin
