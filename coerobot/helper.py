from datetime import datetime

def log(*args):
    time = datetime.now().strftime("[%H:%M:%S]")
    message = list(args)
    print(time + ' ' + ''.join(str(word) for word in message))
