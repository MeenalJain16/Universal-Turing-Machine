import xml.etree.ElementTree as ET
print('----UNIVERSAL TURING MACHINE----\n')
x='yes'
while(x=='y' or x=='yes'):
    x='no'
    op_no=int(input("Enter a number for operation to be performed:\n1. Reverse String\n2. Full Adder\n3. XOR Operation\n4. Other \n"))
    if(op_no==1):
        datafile='reverse.xml'
    if(op_no==2):
        datafile='ADR.xml'
    if(op_no==3):
        datafile='turing_XOR.xml'
    if(op_no==4):
        datafile=input('Enter name of file with .xml extension:\n')
    
    tree = ET.parse(datafile)
    root = tree.getroot()

    for child in root:
        if child.tag == 'IOTape' :
            problem = child.get("format")
            blank = child.get("blank")
            input_str = child.text
            input_str = input_str.replace(' ','').replace('\n','').replace('\t','')
            head = input_str.index('>')
            input_str = input_str.replace('>','')
        elif child.tag == 'ProgramTape':
            delta = child.text
            delta = delta.replace(' ','').replace('\n','').replace('\t','').replace("(","('").replace(")","')").replace(",","','").replace("')','","'),")
            prog_tape = eval(delta)
            halt = child.get("halt")
            state = child.get("start")
            left = child.get("left")
            right = child.get("right")

    tape = [input_str[k] for k in range(len(input_str))]
    if (1):
        while (state != halt):
            if head in list(range(len(tape))):
                delta_key = tuple([state, tape[head]])
                if delta_key in prog_tape.keys():
                    delta_value = prog_tape[delta_key]
                    state = delta_value[0]
                    tape[head] = delta_value[1]
                    print('HEAD-->',head)
                    print(''.join(tape))                
                    if right in delta_value[2]:
                        head+=1
                    elif left in delta_value[2]:
                        head-=1
            elif head <= list(range(len(tape)))[0]:
                tape.insert(0,blank)
                head = 0
            else :
                tape.append(blank)
    print("Do you wish to perform another operation: 'yes' or 'no'\n")
    x = input()
