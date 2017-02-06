#!/bin/bash
#
# Usage: source makePlots.sh

for file in 1_1_{1,2,3,5,6,7,9,11,13,15}
do
	python3 analyze_csvFiles.py $file
done
