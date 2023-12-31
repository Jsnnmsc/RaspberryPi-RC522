import signal
import time
import MFRC522
import RPi.GPIO as GPIO

MIF = MFRC522.MFRC522()


def Scan():
    global status
    # Use MI_OK to check status is going well
    # If not it will looping until MI_OK to check status is True
    # Because when Mifare is error the value is "2", Good is "0"
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

# Turn UID into Heximal
UIDorigin = str(hex(uid[0])[2:].zfill(2)) + str(hex(uid[1])[2:].zfill(2)) + \
    str(hex(uid[2])[2:].zfill(2)) + str(hex(uid[3])[2:].zfill(2))

print(uid)
print(f"Your UID(hex) is {UIDorigin}")
