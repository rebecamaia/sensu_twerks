#!/bin/bash

INS=$1
RES=`ps axu | grep $INS | grep java | grep -v grep | tr -s " " | cut -d " " -f2`

if [ "${RES:-null}" = null ]; then
  echo "WARNING: JBOSS might not be running for instance $1!"
  exit 2
else
  echo "OK: JBOSS is running for is running for instance $1 with PID $RES"
  exit 0
fi
echo "Unknown: How did I get here?"
exit 3
