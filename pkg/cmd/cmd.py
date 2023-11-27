import os
print("Type 'EXIT' to exit CMD")
pr = ">"
while True:
    o = input(f"CMD{pr} ")
    if not o.lower() == "exit":
        os.system(o)
    else:
        break
