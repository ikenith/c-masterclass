#!/usr/bin/env bash
PORT=8123
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"
echo "================================================================="
echo " C Programming Masterclass: Unit 1 Educational Website"
echo " Live Server Address: http://localhost:${PORT}"
echo " Directory: ${DIR}"
echo "================================================================="
python3 -m http.server ${PORT} --directory "${DIR}"
