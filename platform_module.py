#!/usr/bin/python3

import platform

#Using platform to display OS, python version, processor, username, Java version, version

sys = platform.system()
processor = platform.processor()
uname = platform.uname()
java_version = platform.java_ver()
version = platform.version()

print(f"The OS running in this system is {sys}.")
print(f"The processor in this system is {processor}.")
print(f"The username of this system is {uname}.")
print(f"The Java version available in this system is {java_version}.")
print(f"The version is {version}.")
