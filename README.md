# Log Analyzer

A small Python script I made to go through login logs and find accounts or IPs with lots of failed login attempts.

The idea is to spot possible brute-force attempts by looking for repeated failed logins.

I made this while learning more about cybersecurity and SOC/blue team stuff.

## What it does

The script reads the log line by line and looks for failed logins.

It keeps track of how many times each username and IP appears. If something reaches the threshold (currently 3), it gets flagged.

## Why I made it

It's a really basic example of how security monitoring can work.

If the same account or IP keeps failing to log in, it could be someone trying to brute-force a password.

## Run it

You don't need to install anything, just Python 3.

```bash
python log_reader.py
```

Make sure `sample_login_log.txt` is in the same folder.

## Example

Example log entry:

```text
2026-09-10 08:15:41 LOGIN_FAILED user=admin ip=203.0.113.44
```

Example output:

```text
User 'admin' has 5 failed login attempts.

IP address '203.0.113.44' has 5 failed login attempts.
```

## What I learned

* Using dictionaries to keep track of counts
* The difference between brute-force attacks and password spraying

## Things I could add

* Use actual log files instead of the sample one
