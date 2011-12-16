#!/bin/bash

if [ $# -ne 1 ]; then
  echo 'Usage: process_learn_file <path to flookup binary>';
else
  tmp_file=$(mktemp);
  python foma_helper.py spanish/spanish.txt.learn $tmp_file;
  cat $tmp_file | python guessforms_reduce.py > spanish_learn.solved;
  rm -f $tmp_file;
  #cat spanish/spanish.txt.learn | awk -F ' ' '{print $1}' | $1 spanish.bin | awk 'NF {print $0}' | python guessforms_reduce.py > spanish_learn.solved;
fi
