#!/bin/bash

# согласные и гласные
printf "define C [b|c|d|f|g|h|j|k|l|m|n|ñ|p|q|r|s|t|v|w|x|y|z];\n"
printf "define V [a|á|e|é|i|í|ï|j|o|ó|º|u|ú|ü];\n"

# определяет вид минимального корня
printf "define Stem [C^<3 V C^<3]+;\n\n"

# блок правил присоединения суфииксов при спряжении
printf "define GuessLexicon Stem [\n"

cat spanish.V | cut -d"," -f4 | sort | uniq | sed 's/\(.\)/\1 /g' | awk -F "," '{printf "\t\t[\"+V\"]:[\"^\" %s]\t\t|\n", $1}'
cat spanish.N | cut -d"," -f4 | sort | uniq | sed 's/\(.\)/\1 /g' | awk -F "," '{printf "\t\t[\"+N\"]:[\"^\" %s]\t\t|\n", $1}'
cat spanish.A | cut -d"," -f4 | sort | uniq | sed 's/\(.\)/\1 /g' | awk -F "," '{printf "\t\t[\"+A\"]:[\"^\" %s]\t\t|\n", $1}'


printf "\t\t[\"+V\"]:0\t\t|\n\t\t[\"+N\"]:0\t\t|\n\t\t[\"+A\"]:0];\n\n"


# блок правил удаления начального суффикса при спряжении
cat spanish.V | sed 's/\(.\)/\1 /g' | awk -F "," '{printf "define V%sDeletion %s -> %s || _ \"^\" [%s];\n", NR, $2, $3, $4}'
cat spanish.N | sed 's/\(.\)/\1 /g' | awk -F "," '{printf "define N%sDeletion %s -> %s || _ \"^\" [%s];\n", NR, $2, $3, $4}'
cat spanish.A | sed 's/\(.\)/\1 /g' | awk -F "," '{printf "define A%sDeletion %s -> %s || _ \"^\" [%s];\n", NR, $2, $3, $4}'


printf "define Cleanup \"^\" -> 0;\n\n"



# объединение всех описанных правил
printf "regex\t\tGuessLexicon .o. \n"

cat spanish.V | sed 's/\(.\)/\1 /g' | awk -F "," '{printf "\t\tV%sDeletion .o.\n", NR}'
cat spanish.N | sed 's/\(.\)/\1 /g' | awk -F "," '{printf "\t\tN%sDeletion .o.\n", NR}'
cat spanish.A | sed 's/\(.\)/\1 /g' | awk -F "," '{printf "\t\tA%sDeletion .o.\n", NR}'


printf "\t\tCleanup;\n"