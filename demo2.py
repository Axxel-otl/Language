delimiters = {'(', ')', '[', ']', '{', '}', '<', '>', '"', "'", '\\', '/', '|', '?', '!', '@', '#', '$', '%', '^', '&', '*', '~', ' ', ';'}
line = input("> ").strip()
state = "COMMAND"
command = ""
text = ""
for c in line:
    if not c in delimiters and state == "COMMAND":
        command += c
        continue

    if state == "TEXT":
        if c == '"':
            state = "FINISHED"
        else:
            text += c

    if c in delimiters:
        match c:
            case '(':
                state = "WAITING"
            case '"':
                state = "TEXT"
print("Command:", command)
if command == "say":
    print(text)
else:
    print("Unknown command:", command)
