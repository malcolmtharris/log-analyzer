log_file = open("sample_login_log.txt", "r")

failed_attempts = {}
ip_counts = {}

for line in log_file:
    if "FAILED" in line:
        parts = line.split()
        user_part = parts[3]
        username = user_part.split("=")[1]

        ip_part = parts[4]
        ip = ip_part.split("=")[1]

        if username in failed_attempts:
            failed_attempts[username] += 1
        else:
            failed_attempts[username] = 1

        if ip in ip_counts:
            ip_counts[ip] += 1
        else:
            ip_counts[ip] = 1

threshold = 3

for username in failed_attempts:
    count = failed_attempts[username]
    if count >= threshold:
        print(f"User '{username}' has {count} failed login attempts.")

for ip in ip_counts:
    count = ip_counts[ip]
    if count >= threshold:
        print(f"IP address '{ip}' has {count} failed login attempts.")