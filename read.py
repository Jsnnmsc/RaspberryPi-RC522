import signal
import time
import MFRC522
import RPi.GPIO as GPIO


mfrc = MFRC522.MFRC522()

# Pause program for 3 second for placing tag in front of the scanner
print("Please place your tag in front of the scanner in 3 seconds!")
time.sleep(3)

# Read first time to check the status of the tag
(status, TagType) = mfrc.MFRC522_Request(mfrc.PICC_REQIDL)
# Use MI_OK to check status is going well
# If not it will looping until MI_OK to check status is True
# Because when Mifare is error the value is "2", Good is "0"
while status != mfrc.MI_OK:
    (status, TagType) = mfrc.MFRC522_Request(mfrc.PICC_REQIDL)
    print("Rescaning...")
    time.sleep(3)


# Get the UID of the tag
(status, uid) = mfrc.MFRC522_Anticoll()

UIDorigin = str(hex(uid[0])[2:].zfill(2)) + str(hex(uid[1])[2:].zfill(2)) + \
    str(hex(uid[2])[2:].zfill(2)) + str(hex(uid[3])[2:].zfill(2))

print(uid)
print(f"Your UID is {UIDorigin}")
