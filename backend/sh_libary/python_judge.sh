#!/bin/bash

random=$RANDOM
time_output="time_output_$random.txt"
temp_output="temp_$random.txt"
diff_output="diff_$random.txt"

while [ "$1" != "" ]; do
    case $1 in
        --code )           shift
                            code=$1
                            ;;
        --in )             shift
                            input=$1
                            ;;
        --ans )            shift
                            ans=$1
                            ;;
        --out )            shift
                            output=$1
                            ;;
        --mode )           shift
                            mode=$1
                            ;;
        --uid )            shift
                            uid=$1
                            ;;
        * )                 echo "Unknown flag"
                            exit 1
    esac
    shift
done

/usr/bin/time -v python3 $code < $input > $temp_output 2> $time_output

if [ "$mode" = "1" ]; then
    diff -B -w -i $temp_output $output > $diff_output
else
    diff -i "temp.txt" $ans > "diff.txt"
fi
