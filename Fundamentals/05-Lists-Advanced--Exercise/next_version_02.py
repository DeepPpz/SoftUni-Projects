software_version = list(map(int, input().split('.')))

if software_version[2] == 9:
    if software_version[1] == 9:
        software_version[0] += 1
        software_version[1] = 0
        software_version[2] = 0
    else:
        software_version[1] += 1
        software_version[2] = 0
else:
    software_version[2] += 1

print(*software_version, sep='.')
