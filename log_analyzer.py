"""Count failed login attempts in a sample security log."""
from pathlib import Path

log_file = Path(__file__).with_name("sample.log")
entries = log_file.read_text(encoding="utf-8").splitlines()
failed_attempts = sum("Failed login" in entry for entry in entries)

print(f"Total log entries: {len(entries)}")
print(f"Failed login attempts: {failed_attempts}")
