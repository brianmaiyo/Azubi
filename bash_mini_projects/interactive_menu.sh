#!/bin/bash

# Function to display the main menu
display_menu() {
  clear
  echo "Welcome to the Record Management System"
  echo "1. Add new record"
  echo "2. Edit existing record"
  echo "3. Search for a record"
  echo "4. Generate report"
  echo "5. Exit"
  echo "Enter your choice:"
}

# Function to add a new record
add_record() {
  clear
  echo "Add New Record"
  echo "-+_+_+_+_+_+_+"

  echo "Enter the name:"
  read name

  echo "Enter the age:"
  read age

  # Save the record to a file or database
  echo "$name,$age" >> records.txt

  echo "Record added successfully!"
  read -n 1 -s -r -p "Press any key to continue..." 
# read -n 1 -s -r -p command is used to read a single character of input in a silent manner,
# preserving backslashes, and displaying a prompt to the user.
}

# Function to edit an existing record
edit_record() {
  clear
  echo "Edit Existing Record"
  echo "---------------------"

  echo "Enter the name to search for the record:"
  read search_name

  # Search for the record in the file or database
  record=$(grep "$search_name" records.txt)
#grep "$search_name" records.txt command searches for the occurrence of the value stored
# in the search_name variable within the records.txt file.
  if [[ -z $record ]]; then #conditional statement in Bash that checks
			    # if the variable record is empty or has a length of zero.
    echo "Record not found!"
  else
    echo "Enter the new name:"
    read new_name

    echo "Enter the new age:"
    read new_age

    # Update the record
    sed -i "s/$search_name,$(echo "$record" | cut -d ',' -f 2)/$new_name,$new_age/" records.txt
#This part extracts the second field from the $record variable by piping it to the cut command.
# It splits the record using , as the delimiter and selects the second field (-f 2).
    echo "Record updated successfully!"
  fi

  read -n 1 -s -r -p "Press any key to continue..."
}

# Function to search for a record
search_record() {
  clear
  echo "Search for a Record"
  echo "--------------------"

  echo "Enter the name to search for:"
  read search_name

  # Search for the record in the file or database
  record=$(grep "$search_name" records.txt)

  if [[ -z $record ]]; then
    echo "Record not found!"
  else
    echo "Record found:"
    echo "$record"
  fi

  read -n 1 -s -r -p "Press any key to continue..."
}

# Function to generate a report
generate_report() {
  clear
  echo "Generate Report"
  echo "----------------"

  # Read and display all records
  if [[ -f "records.txt" ]]; then
    echo "Records:"
    cat records.txt
  else
    echo "No records found!"
  fi

  read -n 1 -s -r -p "Press any key to continue..."
}

# Main program loop
while true; do
  display_menu

  read choice

  case $choice in
    1)
      add_record
      ;;
    2)
      edit_record
      ;;
    3)
      search_record
      ;;
    4)
      generate_report
      ;;
    5)
      echo "Exiting..."
      exit 0
      ;;
    *)
      echo "Invalid choice!"
      ;;
  esac
done
