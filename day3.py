with open('data3.txt', 'r', encoding='UTF-8') as file:
            lines = file.read()
lines = lines.split('\n')
answer_g = []
answer_e = []
for i in range(len(lines[0])):
    new_line = []
    for line in lines:
        new_line.append(line[i])
    answer_g.append(max(set(new_line), key=new_line.count))
    answer_e.append(min(set(new_line), key=new_line.count))
answer_g = ''.join(answer_g)
answer_e = ''.join(answer_e)
gamma = int(answer_g,2)
epsilon = int(answer_e,2)
print(gamma*epsilon)

# Part two
