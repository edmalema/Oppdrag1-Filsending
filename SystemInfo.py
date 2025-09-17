import platform

system_info = platform.uname()

print("Du bruker en pc med", system_info.system, "operativsystemet")
print(system_info.machine)

#Mer skal her senere