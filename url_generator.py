import sys

def main():
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <filename>")
        sys.exit(1)

    #Get input file
    filename = sys.argv[1]

    count = 0
    res = '      - "{{BaseURL}}/?'
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
            for i in range(len(lines)):
                count+=1
                #For each line in file add to the res
                res+= f'{lines[i].replace('\n','')}=%27%22%20test=fx-{i}&'

                #If count goes greater than limit, move to next line
                if count>35 and i < len(lines) - 1:
                    count = 0
                    res = res[:-1]
                    res += '"\n      - "{{BaseURL}}/?'
        if res.endswith('&'):
            res = res[:-1]
            res+='"\n'

        #Read the base file
        with open('base.yaml', 'r') as file:
            lines = file.readlines()
            for i in range(len(lines)):

                #Replace the line which has {OutputGoesHere}
                if '{OutputGoesHere}' in lines[i]:
                    lines[i] = res
                    #Generate the new output file
                    with open('out.yaml', 'w') as file2:
                        file2.writelines(lines)

    except FileNotFoundError:
        print(f"Error: Unable to open the file '{filename}'")
        sys.exit(1)

if __name__ == "__main__":
    main()