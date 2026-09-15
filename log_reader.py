log_file = open("sample_login_log.txt", "r")

failed_attempts = {}

for line in log_file:
    if "FAILED" in line:
        parts = line.split()
        user_part = parts[3]
        username = user_part.split("=")[1]
        print(username)

        if username in failed_attempts:
            failed_attempts[username] += 1
        else:
            failed_attempts[username] = 1

print(failed_attempts)

threshold = 3

for username in failed_attempts:
    count = failed_attempts[username]
    if count >= threshold:
        print(f"User '{username}' has {count} failed login attempts.")