#!/bin/bash

magenta=$(tput setaf 5)
cyan=$(tput setaf 6)
red=$(tput setaf 1)
reset=$(tput sgr0)

imageName="speedtest-poller"
certificatePath="firebase/certificate.json"
interval="15m"

if [ ! -f $certificatePath ]
then
  echo "${red}Error:${reset} Firebase certificate not found in ${cyan}${certificatePath}${reset}"
  exit
fi

if [ $1 ]
then
  interval=$1
fi

echo "${magenta}[1/2]${reset} Build image ${cyan}$imageName${reset}..."
docker build -t $imageName:latest --build-arg INTERVAL=$interval .

echo "${magenta}[2/2]${reset} Run a container..."
docker run -d --restart on-failure $imageName
