def read_answer_key(file_path):
    with open(file_path, 'r') as file:
        # Split each line into a list of answers
        answer_key = [line.strip().split() for line in file]
    return answer_key

def check_answers(file1_answers, file2_answers):
    count = 1
    wrong = 0
    for ans1, ans2 in zip(file1_answers, file2_answers):
        # Check if there are multiple answers in file1 (considered wrong)
        if len(ans1) > 1:
            result = "incorrect"
        else:
            # Check if any answer or '*' in file2 matches the corresponding answer in file1
            if '*' in ans2:
                result = "correct"
            elif ans1[0] in ans2:
                result = "correct"
            else:
                result = "incorrect"

        if result == "incorrect":
            print(f"{str(count).rjust(3)}. {result}: {ans1} != {ans2}")
            wrong += 1
        count += 1

    return wrong

def main():
    file1_path = "/tmp/test.txt"  # Replace with the actual file path for file1
    file2_path = "/tmp/test2.txt"  # Replace with the actual file path for file2

    # Read answer keys from both files
    print()
    file1_answers = read_answer_key(file1_path)
    file2_answers = read_answer_key(file2_path)

    # Check and print the correctness of each answer
    num = check_answers(file1_answers, file2_answers)

    print(f"\nTotal Incorrect: {num}")

if __name__ == "__main__":
    main()
