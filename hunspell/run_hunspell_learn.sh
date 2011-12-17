#!/bin/sh

awk -F ' ' '{print $1}' ../spanish/spanish.txt.learn > spanish_learn.firstcolumn
hunspell -1 -m -d spanish -i iso-8859-15 spanish_learn.firstcolumn > spanish.hunspelled
python convert.py spanish_learn.firstcolumn spanish_learn.hunspelled > spanish_learn.converted
