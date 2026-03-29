import smtplib
import csv
import time
import logging
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders


SENDER_EMAIL    = "ousmane@speakhire.org"
SENDER_PASSWORD = "csvb dggr wres zvyy"   # Gmail App Password (NOT your real password)
SMTP_SERVER     = "smtp.gmail.com"
SMTP_PORT       = 587
CSV_FILE        = "alumni_outreach.csv" # Export your Google Sheet as CSV
ATTACHMENT_PATH = "cheers4careers.jpeg"  # Set to None if no attachment
DELAY_SECONDS   = 0.5                   # Pause between sends to avoid spam flags
LOG_FILE        = "email_log.txt"
SKIPPED_FILE    = "skipped_no_email.txt"  # Tracks alumni with missing emails

# ── Column names as they appear in your exported CSV header row ───────────────
COL_NAME  = "Full Name"
COL_EMAIL = "Email Address"



logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


def build_email(name):
    first_name = name.strip().split()[0] if name.strip() else "there"
    subject = "You're Invited! 🥂 #Cheers4Careers – This Saturday!"
    body = f"""Hey {first_name}! 👋

Hope you're doing great! I wanted to personally invite you to #Cheers4Careers, \
a networking event hosted by SpeakHire Alumni Board this Saturday — a perfect opportunity to \
connect with fellow professionals, explore career opportunities, and celebrate \
your journey so far! 🚀

📅 Date: Saturday, March 28, 2026
⏰ Time: 1:00 – 3:00 PM EST
📍 Queens Museum, Theater on the 2nd Floor
   Flushing Meadows Corona Park, Queens, NY

Spots are limited — register in advance using the flyer attached! 🎟️

Would love to see you there. Come network, connect, and cheer on your career! 🥂✨

#Cheers4Careers #SpeakHire
"""
    return subject, body



def send_email(server, name, recipient_email):
    subject, body = build_email(name)

    msg = MIMEMultipart()
    msg["From"]    = SENDER_EMAIL
    msg["To"]      = recipient_email
    msg["Subject"] = subject
    msg.attach(MIMEText(body, "plain"))

    if ATTACHMENT_PATH:
        with open(ATTACHMENT_PATH, "rb") as f:
            part = MIMEBase("application", "octet-stream")
            part.set_payload(f.read())
            encoders.encode_base64(part)
            part.add_header(
                "Content-Disposition",
                f'attachment; filename="{ATTACHMENT_PATH}"'
            )
            msg.attach(part)

    server.sendmail(SENDER_EMAIL, recipient_email, msg.as_string())



def main():
    sent, failed, skipped = 0, 0, 0

    skipped_records = []

    with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
        server.starttls()
        server.login(SENDER_EMAIL, SENDER_PASSWORD)
        print("✅ Logged in. Starting email blast...\n")

        with open(CSV_FILE, newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)

            for row in reader:
                name  = row.get(COL_NAME, "").strip()
                email = row.get(COL_EMAIL, "").strip()

                # Skip rows with no email
                if not email or "@" not in email:
                    print(f"  ⚠️  Skipped (no email) → {name}")
                    skipped_records.append(name)
                    skipped += 1
                    continue

                try:
                    send_email(server, name, email)
                    print(f"  ✅ Sent → {name} <{email}>")
                    logging.info(f"SENT | {name} | {email}")
                    sent += 1
                except Exception as e:
                    print(f"  ❌ Failed → {name} <{email}> | {e}")
                    logging.error(f"FAILED | {name} | {email} | {e}")
                    failed += 1

                time.sleep(DELAY_SECONDS)

    # Save skipped names to a separate file for follow-up
    with open(SKIPPED_FILE, "w", encoding="utf-8") as sf:
        sf.write("Alumni with no email on file:\n")
        sf.write("\n".join(skipped_records))

    print(f"\n📊 Done!")
    print(f"   ✅ Sent:    {sent}")
    print(f"   ❌ Failed:  {failed}")
    print(f"   ⚠️  Skipped: {skipped} (saved to {SKIPPED_FILE})")
    print(f"   📝 Full log: {LOG_FILE}")

if __name__ == "__main__":
    main()

