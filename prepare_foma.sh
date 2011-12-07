if [ $# -lt 1]; then
    echo 'Usage: prepare_foma.sh <path to foma executable>';
else
    $1 -f make_spanish_bin.foma;
fi
