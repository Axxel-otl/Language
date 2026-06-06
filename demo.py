line = input("> ").strip()
parts = line.split()

if len(parts) == 0:
    exit()

command = parts[0]
args = parts[1:]

text = " ".join(args)

if command == "echo":
    print(text)
else:
    print("Unknown command:", command)
