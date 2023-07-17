#!/usr/bin/bash

# Function to display the menu to the user
display_menu() {
  echo "Menu:"
  echo "1. Greet"
  echo "2. Count from 1 to N"
  echo "3. Exit"
  echo "Enter your choice:"
}

# Function to greet the user
greet() {
  echo "Hello! What's your name?"
  read name
  echo "Nice to meet you, $name!"
}

# Function to count from 1 to N
count_numbers() {
  echo "Enter a number:"
  read number

  if [[ $number =~ ^[0-9]+$ ]]; then	#performs a regular expression check 
					#to ensure that the input is a valid number
    echo "Counting from 1 to $number:"
    for ((i = 1; i <= number; i++)); do
      echo $i
    done
  else
    echo "Invalid input! Please enter a valid number."
  fi
}

# Main program loop
while true; do
  display_menu

  read choice

  case $choice in
    1)
      greet
      ;;
    2)
      count_numbers
      ;;
    3)
      echo "Exiting..."
      exit 0
      ;;
    *)
      echo "Invalid choice!"
      ;;
  esac

  echo "Press Enter to continue..."
  read -r
  clear
done
