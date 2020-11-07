def dupLet(line):
    return line[0] + ''.join(line[i] for i in range(1,len(line)) if line[i]!=line[i-1])
print(dupLet('PPYYYTTHON'))
print(dupLet('PPyyythonnn'))