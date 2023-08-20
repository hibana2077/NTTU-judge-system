#!/bin/bash
###
 # @Author: hibana2077 hibana2077@gmaill.com
 # @Date: 2023-06-17 16:27:30
 # @LastEditors: hibana2077 hibana2077@gmaill.com
 # @LastEditTime: 2023-08-20 20:15:00
 # @FilePath: /NTTU-new-gen-judge-system/backend/sh_libary/python_judge.sh
 # @Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
### 

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

while IFS= read -r line
do
    if [[ $line == *"differ"* ]]; then
        echo "    diff: 1" >> $output
    else
        echo "    diff: 0" >> $output
    fi
done < "$diff_output"