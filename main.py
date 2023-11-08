import logging as lg

lg.basicConfig(level=lg.DEBUG,
               filename="logs.log",
               filemode="w",
               format="%(asctime)s: %(levelname)s -- %(message)s")

lg.debug("1")

try:
    print(10/0)
except Exception:
    lg.exception("exception exception exception exception exception exception exception exception exception exception")

with open('logs.log') as file:
    lines = file.readlines()

for i in range(len(lines)):
    print(f"{i + 1}[{i}]: " + lines[i])
