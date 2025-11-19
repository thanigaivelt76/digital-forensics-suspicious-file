# 🔍 Digital Forensics — Case of the Suspicious File

## Project Description
This repository demonstrates a digital forensics investigation on a suspicious file.  
The goal is to analyze the file like a cyber–forensics expert and determine if it contains malicious content.

## 🎯 Objectives
- Verify file integrity using cryptographic hashes
- Perform static analysis without executing the file
- (Optional) Perform dynamic analysis in an isolated sandbox
- Collect forensic reports as evidence

---

## 📁 Repository Structure
| Folder | Purpose |
|--------|---------|
| `forensic_scripts/` | Scripts used for the investigation |
| `evidence/` | The suspicious file or placeholder |
| `results/` | Reports generated during forensic analysis |

---

## 🚀 Implementation Steps

### 1️⃣ Verify File Integrity (Checksum)
Generate SHA-256 hash to ensure evidence has not been tampered:
2️⃣ Static Analysis (Without Executing)

Detect indicators of compromise by inspecting strings and signatures.

Python script:
python3 forensic_scripts/2_static_analysis.py evidence/suspicious_download.zip > results/static_analysis_report.txt
3️⃣ Dynamic Analysis (Optional & Sandbox Only!)

If executable, run only inside isolated VM / Kali / FlareVM.

- Monitor file system changes
- Monitor network connections (Wireshark)
- Monitor registry / processes (ProcMon)


Log observations in:

results/dynamic_observation_report.txt
🛑 Legal Warning

This project is strictly for cybersecurity learning and research.
Never analyze malware on a production system.


---

## 🧾 SCRIPT — Checksum Verification (`1_checksum_verification.sh`)

```bash
#!/bin/bash
FILE=$1
echo "[+] Calculating SHA-256 hash for $FILE"
sha256sum "$FILE" | tee ../results/hashes.txt
echo "[+] Hash saved in results/hashes.txt"
```bash
sha256sum evidence/suspicious_download.zip | tee results/hashes.txt
