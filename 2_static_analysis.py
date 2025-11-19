import subprocess, sys

file = sys.argv[1]
print("[+] Running static analysis on:", file)

print("\n--- Extracted Strings ---")
strings = subprocess.run(["strings", file], capture_output=True, text=True)
print(strings.stdout)

print("\n--- Suspicious Indicators ---")
suspicious_keywords = ["http", "https", ".php", "upload", "exe", "cmd", "powershell"]
for line in strings.stdout.splitlines():
    for keyword in suspicious_keywords:
        if keyword.lower() in line.lower():
            print("[!] Found Indicator:", line)
