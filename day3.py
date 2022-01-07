# with open('data3.txt', 'r', encoding='UTF-8') as file:
#             lines = file.read()
# lines = lines.split('\n')
# answer_g = []
# answer_e = []
# for i in range(len(lines[0])):
#     new_line = []
#     for line in lines:
#         new_line.append(line[i])
#     answer_g.append(max(set(new_line), key=new_line.count))
#     answer_e.append(min(set(new_line), key=new_line.count))
# answer_g = ''.join(answer_g)
# answer_e = ''.join(answer_e)
# gamma = int(answer_g,2)
# epsilon = int(answer_e,2)
# print(gamma*epsilon)

# Part two
def countingOX():
    with open('data3.txt', 'r', encoding='UTF-8') as file:
            lines = file.read()
    lines = lines.split('\n')
    # Construct vertical lines for the first column

    for i in range(12):
        
        vert = []
        for line in lines:
            vert.append(line[i])
        
        
        if vert.count('0') <= len(lines)/2:
            m = '1'
        else:
            m = '0'
        # print(vert.count('0'),len(lines)/2,m)
        new_lines = []
        for line in lines:
            if line[i] == m:
                new_lines.append(line)
        lines = new_lines
        if len(lines) == 1: return int(lines[0],2)
           

def countingC02():
    with open('data3.txt', 'r', encoding='UTF-8') as file:
            lines = file.read()
    lines = lines.split('\n')
    # Construct vertical lines for the first column

    for i in range(12):
        
        vert = []
        for line in lines:
            vert.append(line[i])
        
        
        if vert.count('0') <= len(lines)/2:
            m = '0'
        else:
            m = '1'
        # print(vert.count('0'),len(lines)/2,m)
        new_lines = []
        for line in lines:
            if line[i] == m:
                new_lines.append(line)
        lines = new_lines
        if len(lines) == 1: return int(lines[0],2)

print(countingOX()*countingC02())
        

   
   


