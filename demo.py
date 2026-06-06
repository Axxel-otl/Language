line = input("> ").strip()
parts = line.split()

if len(parts) == 0:
    exit()

command = parts[0]
args = parts[1:]

text = " ".join(args)

if command == "say":
    print(text)
else:
    print("Unknown command:", command)
