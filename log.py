import random
import datetime
import string
import math

LOG_MESSAGE = tuple([
    "[INFO] - Connection established.",
    "[ERROR] - File not found.",
    "[ERROR] - Database connection failed.",
    "[WARNING] - Invalid input received.",
    "[INFO] - Task completed successfully.",
    "[WARNING] - Server overloaded.",
    "[INFO] - Authentication failed.",
    "[INFO] - Permission denied.",
    "[ERROR] - Critical system error.",
    "[WARNING] - Resource limit exceeded.",
    "[ERROR] - Server timeout occurred.",
    "[WARNING] - Disk space running low.",
    "[ERROR] - Database query failed.",
    "[INFO] - Configuration file loaded.",
    "[WARNING] - Network connection unstable.",
    "[ERROR] - Application crashed unexpectedly.",
    "[INFO] - Backup completed successfully.",
    "[WARNING] - Memory usage high.",
    "[ERROR] - Permission denied for user.",
    "[INFO] - New user registered.",
    "[WARNING] - Software update available.",
    "[WARNING] - CPU temperature exceeding threshold.",
    "[ERROR] - Server crashed due to memory leak.",
    "[ERROR] - HTTP request failed with status code 404.",
    "[WARNING] - Server response time exceeding threshold.",
    "[INFO] - Database backup completed."
])


def fake_log_generator():

    if random.random() < 0.1:
        write_data(fake_log_message() if random.random()
                   > 0.1 else user_logging())

    return


logged_user = []


def user_logging():

    if len(logged_user) != 0 and random.random() > 0.4:
        msg = "User logged out successfully."
        user = random.choice(logged_user)

        logged_user.remove(user)

    else:
        msg = "User logged in successfully."
        user = generate_random_word(random.randint(5, 10))

        logged_user.append(user)

    return f"[INFO] {user} {msg}"


def generate_random_word(length):
    letters = string.ascii_lowercase  # lowercase letters
    return ''.join(random.choice(letters) for _ in range(length))


def fake_log_message():
    return random.choice(LOG_MESSAGE)


def line_count():
    with open('system_file.txt', 'r') as f:
        return len(f.readlines())


def write_data(message):

    def timestamp(): return str(datetime.datetime.fromtimestamp(
        math.floor(datetime.datetime.now().timestamp() + cycle)))

    # Open the file for writing
    with open('system_file.txt', 'a') as f:
        f.write(timestamp() + " - " + message + "\n")

    # The file is automatically closed when the 'with' block ends


cycle = 0

if __name__ == "__main__":

    while line_count() < 1000:
        fake_log_generator()
        cycle += 1
