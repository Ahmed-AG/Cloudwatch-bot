import sys

def get_rand_number_of_fields(rand_upper_bound):

    return 0

def get_count_fields(fields_file):

    return 0

def get_rand(rand_upper_bound):

    return 0

def get_full_field_name(fields_file):

    return 0

def read_file(file_name):

    return 0

def generate_fields(fields_file, max_fields):
    for j in [1:number_of_fields]; do
            # randomly selecting the fields
            field_number = get_rand(rand_upper_bound)
            full_field_name = get_full_field_name(fields_file)
            short_field_name = get_short_field_name(full_field_name)

            prompt +="$short_field_name, "
            completion += "$full_field_name, "
        
        limit = get_rand(1000)
        prompt+=" with a limit of $limit"
        # echo "prompt= $prompt"
        completion+=" | sort @timestamp desc | limit $limit ###"

    return 0,0
def generate_question(number_of_questions):
    # generate what
    # generate who
    # generate orders
    return 0,0

def generate_actions(number_of_actions):

    return 0,0

def generate_conditions():
    return 0,0
def generate_sort():
    return 0,0
def generate_limit():
    return 0,0
def generate_ip():
    return 0,0


if __name__ == "__main__":
    number_of_examples = sys.argv[1]
    fields_file = read_file(sys.argv[2])

    rand_upper_bound = get_count_fields(fields_file)
    for i in [1:number_of_examples]: 
        number_of_fields = get_rand(rand_upper_bound)
        
        # Generate fields function
        fields_prompt, fields_completion = generate_fields(fields_file, max_fields)
        question_prompt, question_completion = generate_question()
        conditions_prompt, conditions_completion = generate_conditions()
        sort_prompt, sort_completion = generate_sort()
        limit_prompt, limit_completion =  generate_limit()

        prompt = "${question_prompt} ${fields_prompts} with a limit of ${limit}"
        completion = "fields @timestamp, ${fields_completion} | limit ${limit}"
        training_line= "{\"prompt\":\"$prompt ->\",\"completion\":\" $completion\"}"
        
        print(training_line)


