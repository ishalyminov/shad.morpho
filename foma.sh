#!/bin/bash

# согласные и гласные
printf "define C [b|c|d|f|g|h|j|k|l|m|n|ñ|p|q|r|s|t|v|w|x|y|z];\n"
printf "define V [a|á|e|é|i|í|ï|j|o|ó|º|u|ú|ü|y];\n"

# определяет вид минимального корня
printf "define Stem [C^<3 V C^<3]+;\n\n"

# блок правил присоединения суфииксов при спряжении
printf "define GuessLexicon Stem [\n"

cat spanish.sfx | cut -d"," -f1,3 | grep V | sort -n | uniq | sed 's/\(.\)/\1 /g' | awk -F "," '{printf "\t\t[\"+V\"]:[\"^\"%s]\t\t|\n", $1}'

cat spanish.sfx | cut -d"," -f1,3 | grep N | sort -n | uniq | sed 's/\(.\)/\1 /g' | awk -F "," '{printf "\t\t[\"+N\"]:[\"^\"%s]\t\t|\n", $1}'

cat spanish.sfx | cut -d"," -f1,3 | grep A | sort -n | uniq | sed 's/\(.\)/\1 /g' | awk -F "," '{printf "\t\t[\"+A\"]:[\"^\"%s]\t\t|\n", $1}'


printf "\t\t[\"+V\"]:0\t\t|\n\t\t[\"+N\"]:0\t\t|\n\t\t[\"+A\"]:0];\n\n"


# блок правил удаления начального суффикса при спряжении
cat spanish.sfx | grep V | sort -n | uniq | sed 's/\(.\)/\1 /g' | head -n 30 | awk -F "," '{if ($2 != " ") {printf "define V%sDeletion %s -> 0 || _ \"^\" [%s];\n", NR, $2, $1}}'



printf "define Cleanup \"^\" -> 0;\n\n"



# объединение всех описанных правил
printf "regex\t\tGuessLexicon .o. \n"

cat spanish.sfx | grep V | sort -n | uniq | sed 's/\(.\)/\1 /g' | head -n 30 | awk -F "," '{if ($2 != " ") {printf "\t\tV%sDeletion .o. \n", NR}}'


printf "\t\tCleanup;"