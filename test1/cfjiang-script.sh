#!/bin/bash

for file in *
do
    
    counter=0

    while read line
    do
	
	isEvenNo=$( expr $counter % 2 )

	if [ $isEvenNo -ne 0 ]
	then
            
            echo $file: $line
       
	fi
	
	(( counter ++ ))
    done < $file
done
