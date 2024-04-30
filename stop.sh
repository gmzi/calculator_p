#!/bin/bash

stop_servers(){
    port_8000=8000
    process_ID=$(lsof -i :"${port_8000}" -t -s)
    echo "process_ID: $process_ID"

    if [[ -n "$process_ID" ]]; then
        echo "Process ID being killed: $process_ID"
        kill "$process_ID"
        echo "Killed process with ID $process_ID."
    else
        echo "No process on port_8000 $port_8000" 
    fi

    port_3000=3000
    process_ID=$(lsof -i :"${port_3000}" -t -s)
    echo "process_ID: $process_ID"
    if [[ -n "$process_ID" ]]; then
        echo "Process ID being killed: $process_ID"
        kill "$process_ID"
        echo "Killed process with ID $process_ID."
    else 
        echo "No process on port_3000 $port_3000"
    fi

    exit 0
}

stop_servers