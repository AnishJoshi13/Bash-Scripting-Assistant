#!/bin/bash

# Check if requirements.txt exists
if [[ ! -f "requirements.txt" ]]; then
    echo "requirements.txt file not found!"
    exit 1
fi

echo "Install all dependencies..."

# Get the number of lines (packages) in requirements.txt
total_packages=$(wc -l < "requirements.txt")
current_package=0
failed_packages=()

# Function to show progress
show_progress() {
    local progress=$((current_package * 100 / total_packages))
    local done=$((progress * 4 / 10))
    local left=$((40 - done))
    local fill=$(printf "%${done}s")
    local empty=$(printf "%${left}s")

    printf "\rInstalling dependencies: [${fill// /#}${empty// /-}] ${progress}%%"
}

# Install each package listed in requirements.txt
while IFS= read -r package
do
    if [[ ! -z "$package" ]]; then
        # Extract the package name without version number
        package_name=$(echo "$package" | cut -d'=' -f1 | cut -d'<' -f1 | cut -d'>' -f1 | cut -d' ' -f1)
        pip install "$package" &> /dev/null
        if [[ $? -ne 0 ]]; then
            failed_packages+=("$package_name")
        fi
        ((current_package++))
        show_progress
    fi
done < "requirements.txt"

# Finish the progress bar
show_progress
echo -e "\nAll dependencies processed."

# Report failed packages
if [[ ${#failed_packages[@]} -ne 0 ]]; then
    echo "The following packages failed to install:"
    for pkg in "${failed_packages[@]}"; do
        echo "- $pkg"
    done
    echo "Hint: Try installing the failed packages separately without using version numbers:"
    for pkg in "${failed_packages[@]}"; do
        echo "pip install $pkg"
    done
else
    echo "All packages installed successfully."
fi
