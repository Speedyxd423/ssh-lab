# ssh-lab
A controlled SSH honeypot and brute forcer lab built in Python. Simulates credential attacks locally for educational purposes.

# SSH Lab — Honeypot & Brute Forcer

A controlled local lab simulating SSH brute force attacks and detection. Built in Python using Paramiko. Run both tools on your own machine to see how credential attacks work and how honeypots log them.

## Files
- `honeypot.py` — fake SSH server that logs every login attempt
- `brute_forcer.py` — attempts passwords from a wordlist against a target
- `wordlist.txt` — list of passwords to test

## Requirements
```bash
pip3 install paramiko colorama
```

## Usage

**Step 1 — Start the honeypot in one terminal:**
```bash
python3 honeypot.py
```

**Step 2 — Run the brute forcer in a second terminal:**
```bash
python3 brute_forcer.py
```
Enter `127.0.0.1` as the target IP, `wordlist.txt` as the wordlist, and any username.

**Step 3 — Check the log file** generated in the same folder to see every captured attempt.

## How it works
The honeypot listens on port 2222 and accepts SSH connections via Paramiko. Every login attempt is logged with IP, username and password then rejected. The brute forcer tries each password from the wordlist and reports success or failure.

⚠️ For educational and authorised use only. Only run against systems you own.
