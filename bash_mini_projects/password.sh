#!/usr/bin/bash

# Function to generate a random password
generate_password() {
  length=$1

  # Define character sets for password generation
  lowercase="abcdefghijklmnopqrstuvwxyz"
  uppercase="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
  numbers="0123456789"
  special_chars="!@#$%^&*()_-+=~"

  # Combine character sets
  all_chars="$lowercase$uppercase$numbers$special_chars"

  # Generate password
  password=""
  for (( i=0; i<$length; i++ )); do
    random_char=${all_chars:RANDOM%${#all_chars}:1}
# {#all_chars}: The ${#variable} syntax is used to get the length
# of a string stored in the all_chars variable.

#RANDOM % ${#all_chars} calculates the modulus of $RANDOM with the length of all_chars.
# The modulus operation % returns the remainder when $RANDOM is divided by the length of all_chars.
# This ensures that the result is within the valid index range of all_chars.

#${all_chars:RANDOM%${#all_chars}:1} uses substring expansion to extract a single character from all_chars.
# It starts at the index specified by $RANDOM % ${#all_chars} and extracts one character (:1).
    password="$password$random_char"
  done

  echo $password
}

# Main program
clear
echo "Random Password Generator"
echo "_+_+_+_+_+_+_+_+_+_+_+_+_"

echo "Enter the length of the password:"
read password_length

# Call generate_password function with the specified length
generated_password=$(generate_password $password_length)
#This line calls the generate_password() function with the password_length as an argument

echo "Generated Password: $generated_password"
