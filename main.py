import subprocess, time
def send(to, message):
    script = f"""
    tell application "Messages"
        set svc to 1st service whose service type = iMessage
        set targetBuddy to buddy "{to}" of svc
        send "{message}" to targetBuddy
    end tell
    """
    subprocess.run(["osascript", "-e", script])

def main():
    to = input("Enter the phone number to send messages to (with country code, no formatting): ")
    message = input("Enter the message to send: ")
    numSent = 0
    while True:
        send(to, message)  
        send(to, message) 
        send(to, message) 
        send(to, message) 
        send(to, message) 
        send(to, message) 
        send(to, message) 
        send(to, message)
        send(to, message)
        send(to, message)
        send(to, message)
        send(to, message)
        send(to, message)
        send(to, message)
        send(to, message)
        send(to, message)
        send(to, message)
        send(to, message)
        send(to, message)
        send(to, message)
        send(to, message)
        send(to, message)
        send(to, message)
        send(to, message)
        send(to, message)
        send(to, message)
        send(to, message)
        send(to, message)
        send(to, message)
        send(to, message)
        send(to, message)
        numSent += 30
        print(f"Sent {numSent} messages")
main()