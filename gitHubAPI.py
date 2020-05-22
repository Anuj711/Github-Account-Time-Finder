from datetime import datetime
from urllib.request import urlopen
import json

# Function will take in a target user name and return how long the account has been open
def userTime(username):
    url = 'https://api.github.com/users/' + username
    resp = urlopen(url)
    reply = json.load(resp)
    timeString = reply['created_at']
    # The [:-1] is to remove the 'Z' at the end of the date time format that is returned
    created = datetime.fromisoformat(timeString[:-1])
    # totalTime calculates the difference between the time we have at the current moment and the time
    # The account was created
    totalTime = datetime.utcnow() - created
    return totalTime

if __name__ == '__main__':
    print("Please enter a desired username")
    user = input()
    print("This user's account is", userTime(user), "old")

