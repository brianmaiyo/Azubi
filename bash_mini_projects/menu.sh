#!/usr/bin/bash   
#specifies the interpreter to be used

#filename where records will be stored
file_name=records.txt

#function to display the menu options on the terminal
display_function()
{
echo "Welcome to the menu system"
echo "_+_+_+_+_+_+_+_+_+_+_+_+_+"
echo  "Select your preferred option"
echo "1: Add new record"
echo "2: Edit an existing record"
echo "3: Search for specific records"
echo "4: Generate reports"
echo "5: exit"
echo "_+_+_+_+_+_+_+_+_+_+_+_+_+_+"

}
#function to start a new record
add_new_record()
{
echo "Enter your name"
read name
echo "Enter your age"
read age
echo "Enter your phone number"
read number
}
#appending record details to records.txt
echo "$name $age $number" >> "file_name"
echo "Record added successfully"
sleep 2  #pause the script for two seconds
#function to edit an existing record
edit_existing_record()
{
echo "Enter the name of the record to be edited"
read search_record_name

    	available=false # variable available  is set to false
	while read -r name age number; do
	if[[$name==$search_Record_name]]
then
	available=true
	echo "Enter new name"
	read newname
	echo "Enter new age"
	read newage
	echo"Enter nre number"
	read newnumber
#sed is used to replace the existing record with a newone
sed i "s/$name $age $number $newname $newage $newnumber/" "$file_name"
echo "successfully edited the record"
break
fi
done < "$file_name"
if  [[ $available == false]]
echo "record not found"
fi

sleep 2

}
#function to search for specific records
search_for_specific_records()
{


}

#function to generate reports
generate_reports()
{


}

