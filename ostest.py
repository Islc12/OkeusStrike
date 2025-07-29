import platform
system = platform.system()

if system != 'Linux':
    print(f"{system} is not Linux")

# this needs to be added as a check before sudo.
