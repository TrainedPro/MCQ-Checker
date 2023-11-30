def read_answer_key(file_path):
    with open(file_path, 'r') as file:
        # Split each line into a list of answers
        answer_key = [line.strip().split() for line in file]
    return answer_key

def check_answers(file1_answers, file2_answers):
    count = 1
    wrong = 0
    for user_answer, answer_key in zip(file1_answers, file2_answers):
        # Check if there are multiple answers in file1 (considered wrong)
        if len(user_answer) > 1:
            result = "incorrect"
        else:
            # Check if any answer or '*' in file2 matches the corresponding answer in file1
            if '*' in answer_key:
                result = "correct"
            elif user_answer[0] in answer_key:
                result = "correct"
            else:
                result = "incorrect"

        if result == "incorrect":
            print(f"{str(count).rjust(3)}. {result}: {user_answer} != {answer_key}")
            wrong += 1
        count += 1

    return wrong

def main():
    user_file = "user_answers.txt"
    answer_file = "answer_key.txt"

    # Read answer keys from both files
    print()
    user_answers = read_answer_key(user_file)
    key_answers = read_answer_key(answer_file)

    # Check and print the correctness of each answer
    num = check_answers(user_answers, key_answers)

    print(f"\nTotal Incorrect: {num}")

if __name__ == "__main__":
    main()
