#!/bin/sh

hunspell -m -d spanish -i iso-8859-15 ../spanish/spanish.txt.test.clean > spanish_test.hunspelled
python convert.py ../spanish/spanish.txt.test.clean spanish_test.hunspelled > spanish_test.converted
echo Broken symbols replace in spanish_test.converted needed. Rules are in hand_rewrite
