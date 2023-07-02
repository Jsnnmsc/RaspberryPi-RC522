import RPi.GPIO as GPIO
import MFRC522
import signal
import time

MIF = MFRC522.MFRC522()


def Scan():
    global status
    while status != MIF.MI_OK:
        (status, TagType) = MIF.MFRC522_Request(MIF.PICC_REQIDL)
        print("Rescaning...Place your tag in front of the scanner...")
        time.sleep(3)


# Pause program for 3 second for placing tag in front of the scanner
print("Please place your tag in front of the scanner in 3 seconds!")
time.sleep(3)

# Read first time to check the status of the tag
(status, TagType) = MIF.MFRC522_Request(MIF.PICC_REQIDL)

Scan()

# Get the UID of the tag
(status, uid) = MIF.MFRC522_Anticoll()

print(f"UID : {uid[0]},{uid[1]},{uid[2]},{uid[3]}")

# Set the default key, its gonna use on authentication with uid
default_key = [0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, ]

Size = MIF.MFRC522_SelectTag(uid)

if status == MIF.MI_OK:

    write_in_data = []

    # Every sector have 16 spaces
    for i in range(0, 16):
        write_in_data.append(0xFF)

    # Authentication with the default_key
    MIF.MFRC522_Auth(MIF.PICC_AUTHENT1A, 0, default_key, uid)

    for i in range(0, 10):
        print(i)
        MIF.MFRC522_Read(i)
