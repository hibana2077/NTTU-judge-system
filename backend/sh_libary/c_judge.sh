#!/bin/bash

# Description: This script is used to judge python code
# Input: --code <code_path> --in <input_path> --ans <ans_path> --out <output_path> --mode <mode> --uid <uid>
# Run sh: sh c_judge.sh --code <code_path> --in <input_path> --ans <ans_path> --out <output_path> --mode <mode> --uid <uid>

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

gcc $code -o $code.out

/usr/bin/time -v ./$code.out < $input > $temp_output 2> $time_output

diff $mode $temp_output $ans > $diff_output

#out.yaml
echo "judge_result:" > $output
echo "  uid: $uid" >> $output
echo "  time_info:" >> $output

#read time output
while IFS= read -r line; do
  case "$line" in
    *"Elapsed (wall clock) time (h:mm:ss or m:ss):"*)
      temp_var=$(echo $line | sed -n 's/.*h:mm:ss or m:ss): //p')
      echo "    wall_clock_time: $temp_var" >> $output
      ;;
    *"Maximum resident set size (kbytes):"*)
      temp_var=$(echo $line | cut -d ":" -f 2-)
      echo "    max_memory: $temp_var" >> $output
      ;;
    *"User time (seconds):"*)
      temp_var=$(echo $line | cut -d ":" -f 2-)
      echo "    user_time: $temp_var" >> $output
      ;;
    *"System time (seconds):"*)
      temp_var=$(echo $line | cut -d ":" -f 2-)
      echo "    system_time: $temp_var" >> $output
      ;;
  esac
done < "$time_output"

#read diff output
echo "  diff_info:" >> $output

#if not none file -> has diff
if [ -s $diff_output ]; then
  echo "    has_diff: true" >> $output
  echo "    diff_content: " >> $output
  while IFS= read -r line; do
    echo "        $line\n" >> $output
  done < "$diff_output"
else
  echo "    has_diff: false" >> $output
fi

# Clean up the temporary files
rm $time_output $temp_output $diff_output $code.out