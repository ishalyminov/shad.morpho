#!/bin/bash

if [ $# -ne 1 ]; then
  echo "Usage: $0 <path to foma executable>";
else
  $1 -f make_spanish_bin.foma;
fi
