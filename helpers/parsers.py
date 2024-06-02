import re

def extract_code_explanation(input_string, marker="|assistant|"):
    # Check if the marker is in the input string
    if marker in input_string:
        # Split the string at the marker and return the second part
        return input_string.split(marker, 1)[1].strip()
    else:
        # If the marker is not found, return an empty string or handle as needed
        return ""

def extract_code_type1(input_string):
    # Define the regex pattern to match text between \begin{code} and \end{code}
    pattern = r'\\begin\{code\}(.*?)\\end\{code\}'
    
    # Use re.search to find the first occurrence of the pattern
    match = re.search(pattern, input_string, re.DOTALL)
    
    # Check if a match is found and return the captured group
    if match:
        return match.group(1)
    else:
        return None

def extract_code_type2(input_string):
    pattern = r'```(.*?)```'
    match = re.search(pattern, input_string, re.DOTALL)
    if match:
        return match.group(1).strip()
    else:
        return ""

print(extract_code_type2('''#!/bin/bash

# Get current CPU usage
cpu_usage=$(sar -u 1 1 | awk '/^Average:/{print 100 - $NF}')

# Threshold for CPU usage (80%)
threshold=80

# Check if CPU usage exceeds the threshold
if (( $(echo "$cpu_usage > $threshold" | bc -l) )); then
    # Log a warning message to system.log
    logger -p warning "CPU usage exceeds 80% - Current CPU usage: $cpu_usage%"
fi
 '''))