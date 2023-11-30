# MCQ-Checker

## Overview

MCQ-Checker is a Python script designed to compare a set of user answers to a provided answer key for multiple-choice questions (MCQs). The script checks the correctness of each answer based on specific criteria and provides a detailed report on incorrect answers.

## Features

- Checks if user answers match the corresponding answer in the key or if the key contains an asterisk '*' for flexibility.
- Considers multiple answers on a single line in the user's file as incorrect.
- Provides a detailed report on incorrect answers, including line-by-line comparison.
- Outputs the total number of incorrect answers.

## Usage

1. Clone the repository:

    ```bash
    git clone https://github.com/your-username/MCQ-Checker.git
    cd MCQ-Checker
    ```

2. Prepare files:

    - Create a file named `user_answers.txt` containing user responses. Each option for a question should be on a separate line. If there are multiple answers for one question, they should be space-separated, but this answer will be considered incorrect.

      Example `user_answers.txt`:
      ```
      A
      B C
      D
      A B
      C
      ```

    - Create a file named `answer_key.txt` containing the correct answers. All correct options for a question can be space-separated, and an asterisk '*' can be used for all correct options.

      Example `answer_key.txt`:
      ```
      C
      *
      A B C
      D
      B D
      ```

3. Run the script:

    ```bash
    python mcq_checker.py
    ```

4. Review the output:

    - The script will display the correctness of each answer, indicating whether it is correct or incorrect.
    - A detailed report of incorrect answers will be provided, showing the user's answer and the correct answer.

## Example

Assuming you have user answers in `user_answers.txt` and the answer key in `answer_key.txt`, run the script:

```bash
python mcq_checker.py
