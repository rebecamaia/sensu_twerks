#!/bin/bash

INS=$1
RES=`ps axu | grep $INS | grep java | grep -v grep | cut -d " " -f3`

if [ "${RES:-null}" = null ]; then
  echo "WARNING: JBOSS might not be running for instance $1!"
  exit 0
else
  echo "OK: JBOSS is running for is running for instance $1 with PID $RES"
  exit 1
fi
echo "Unknown: How did I get here?"
exit 3
