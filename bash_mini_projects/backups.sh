#!/bin/bash

# Source file and backup directory
record_file="records.txt"
backup_directory="backups"

# Function to create a backup
create_backup() {
  # Create the backup directory if it doesn't exist
  if [[ ! -d $backup_directory ]]; then
    mkdir $backup_directory
  fi

  # Generate a backup filename with timestamp
  backup_filename="$backup_directory/backup_$(date +'%Y%m%d_%H%M%S').txt"

  # Copy the record file to the backup filename
  cp $record_file $backup_filename

  echo "Backup created: $backup_filename"
}

# Main program
clear
echo "Personal Record Backup"
echo "----------------------"

echo "1. Create backup now"
echo "2. Schedule regular backups"

read choice

case $choice in
  1)
    create_backup
    ;;
  2)
    echo "Enter the backup frequency (in hours):"
    read backup_frequency

    while true; do
      create_backup
      sleep $((backup_frequency * 3600)) # Convert hours to seconds
    done
    ;;
  *)
    echo "Invalid choice!"
    ;;
esac
