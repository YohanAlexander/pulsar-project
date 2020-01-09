import sys, subprocess

def main():

    xspec = subprocess.Popen(["xspec"], stdin=subprocess.PIPE, stdout=subprocess.PIPE,
                        stderr=subprocess.PIPE, universal_newlines=True, bufsize=0)

    with open(f'{sys.argv[1]}', 'r') as text:
        commands = text.readlines()
    
    for line in commands:
        xspec.stdin.write(line)
    
    xspec.stdin.close()

    for line in xspec.stdout:
        print(line)
        
if __name__ == "__main__":
    main()
