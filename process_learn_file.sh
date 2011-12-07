if [ $# -lt 1 ]; then
    echo 'Usage: process_learn_file <path to flookup binary>';
else
    cat spanish/spanish.txt.learn | awk -F ' ' '{print $1}' | $1 spanish.bin | awk 'NF {print $0}' | python guessforms_reduce.py > spanish_learn.solved;
fi
