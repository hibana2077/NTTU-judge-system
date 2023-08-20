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