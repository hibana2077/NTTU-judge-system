#!/bin/bash

# Description: This script is used to judge python code
# Input: --code <code_path> --in <input_path> --ans <ans_path> --out <output_path> --mode <mode> --uid <uid>

random=$RANDOM #random number for temp file
time_output="time_output_$random.txt"
temp_output="temp_$random.txt"
diff_output="diff_$random.txt"

# Initializing flags to check if necessary parameters are provided
code_flag=0
in_flag=0
ans_flag=0
out_flag=0
mode_flag=0
uid_flag=0

while [ "$1" != "" ]; do
    case $1 in
        --code )           shift
                            code=$1
                            code_flag=1
                            ;;
        --in )             shift
                            input=$1
                            in_flag=1
                            ;;
        --ans )            shift
                            ans=$1
                            ans_flag=1
                            ;;
        --out )            shift
                            output=$1
                            out_flag=1
                            ;;
        --mode )           shift
                            mode=$1
                            mode_flag=1
                            ;;
        --uid )            shift
                            uid=$1
                            uid_flag=1
                            ;;
        * )                 echo "未知的標誌"
                            exit 1
    esac
    shift
done

# Checking if all necessary parameters are provided
if [ $code_flag -eq 0 ] || [ $in_flag -eq 0 ] || [ $ans_flag -eq 0 ] || [ $out_flag -eq 0 ] || [ $mode_flag -eq 0 ] || [ $uid_flag -eq 0 ]; then
    echo "缺少必要的參數"
    exit 1
fi

/usr/bin/time -v python3 $code < $input > $temp_output 2> $time_output

diff $mode $temp_output $ans > $diff_output

#out.yaml
echo "judge_result:" > $output
echo "  uid: $uid" >> $output
echo "  time_info:" >> $output

#read time output
while IFS= read -r line
do
    if [[ $line == *"Elapsed (wall clock) time (h:mm:ss or m:ss):"* ]]; then
        temp_var=$(echo $line | cut -d ":" -f 2)
        echo "    wall_clock_time: $temp_var" >> $output
    fi
    if [[ $line == *"Maximum resident set size (kbytes):"* ]]; then
        temp_var=$(echo $line | cut -d ":" -f 2)
        echo "    max_memory: $temp_var" >> $output
    fi
    if [[ $line == *"User time (seconds):"* ]]; then
        temp_var=$(echo $line | cut -d ":" -f 2)
        echo "    user_time: $temp_var" >> $output
    fi
    if [[ $line == *"System time (seconds):"* ]]; then
        temp_var=$(echo $line | cut -d ":" -f 2)
        echo "    system_time: $temp_var" >> $output
    fi
done < "$time_output"

#read diff output
echo "  diff_info:" >> $output

if grep -q 'differ' "$diff_output"; then
    echo "    diff: 1" >> $output
else
    echo "    diff: 0" >> $output
fi

# Clean up the temporary files
rm $time_output $temp_output $diff_output
