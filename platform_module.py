#!/bin/python

#Using platform to display OS, python version, processor, OS type, username, Java version, version

import platform

print(f"The OS running in this machine is {platform.system()}.")
print(f"The processor in this system is {platform.processor()}.")
print(f"The USername of this system is {platform.uname()}.")
print(f"The Java version available in this system is {platform.java_ver()}.")
print(f"The version is {platform.version()}.")
