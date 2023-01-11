#! /bin/bash
fields_file=$1
count_fields=$(grep -c '' $fields_file)
# echo $count_fields
upper_bound=$(expr $count_fields)

# for field in $(cat $fields_file)
# do
#     full_field_name=$field
#     short_field_name=$(echo $field|rev | cut -d'.' -f1 |rev)
#     echo "$short_field_name,$short_field_name" >> /tmp/fields.csv
# done

# Generate 10 random numbers and add them to the array
# Loop: Number of queries
for i in {1..250}; do
    # Loop: Number of fields mentioned in a query
    number_of_fields=$((RANDOM % upper_bound + 1))
    prompt="Show me the fields "
    completion="fields @timestamp, "
    for j in $(seq 1 $number_of_fields); do
        # randomly selecting the fields
        field_number=$((RANDOM % upper_bound + 1))
        full_field_name=$(awk "NR == $field_number" $fields_file)
        # echo $full_field_name
        short_field_name=$(echo $full_field_name|rev | cut -d'.' -f1 |rev)
        # echo $short_field_name
        prompt+="$short_field_name, "
        completion+="$full_field_name, "
    done
    limit=$((RANDOM % 100 + 1))
    prompt+=" with a limit of $limit"
    # echo "prompt= $prompt"
    completion+=" | sort @timestamp desc | limit $limit ###"
    # completion+="@message | sort @timestamp desc | limit $limit ###"
    # echo "completion= $completion"
    training_line="{\"prompt\":\"$prompt ->\",\"completion\":\" $completion\"}"
    echo $training_line
    # exit
done
#   array+=($((RANDOM % 100 + 1)))

# # Print the array
# echo ${array[@]}

echo 