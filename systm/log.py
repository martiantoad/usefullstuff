from time import gmtime, strftime

log = []
timestamps = []

def add(to_add):
    log.append(to_add)
    timestamps.append(strftime("%H:%M:%S", gmtime()))

def print_log():
    tsc = 0
    for entery in log:
        print timestamps[tsc] + " - " + entery 
        tsc += 1

def give_log():
    formatted_log = []
    tsc = 0
    for entery in log:
        entery_timestamp = [entery, timestamps[tsc]]
        formatted_log.append(entery_timestamp)
    return formatted_log
