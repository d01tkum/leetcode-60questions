while read line
do
    mkdir $line
done < dirname_list.txt
