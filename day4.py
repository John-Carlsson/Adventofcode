with open('data4.txt', 'r', encoding='UTF-8') as file:
         lines = file.read()
lines = lines.split('\n')

numbers = lines[0].split(',') # Numbers to be drawn

def check_win(board,drawn_numbers):
    for line in board:
        w = 0
        for num in line:
            if num in drawn_numbers: 
                w += 1
            else:
                break
            if w == 5: return 'win'
    
    for i in range(len(board)):
        w = 0
        
        for line in board:
            if line[i] in drawn_numbers: 
                w += 1
            else:
                break
            if w == 5: return 'win'

boards = [[]]
b = 0
i = 0
# Create the boards
for line in lines[1:]:
    if not line: continue
    listt = line.split()

    boards[b].append(listt)
    i += 1
    if i == 5:
        i = 0
        b += 1
        boards.append([])
boards.pop()

drawn_numbers = numbers[:5]
won = False
for i in range(5,len(numbers)):
    # Nåt som kollar om någon bricka vunnit
    b = 0
    for board in boards:
        if check_win(board,drawn_numbers) == 'win': 
            print('Board',b, 'won')
            won = True
            break
        b += 1

    if won == True: break
    drawn_numbers.append(numbers[i]) # Dra ett nytt nummer

unmarked_sum = 0
for line in boards[b]:
    for num in line:
        if num not in drawn_numbers:
            unmarked_sum += int(num)

print(unmarked_sum*int(drawn_numbers[-1]))


############### PART 2 ################

def check_win_last(board,drawn_numbers):
    for line in board:
        w = 0
        for num in line:
            if num in drawn_numbers: 
                w += 1
            else:
                break
            if w == 5: return 'win'
    
    for i in range(len(board)):
        w = 0
        
        for line in board:
            if line[i] in drawn_numbers:
                w += 1
            else:
                break
            if w == 5: return 'win'

drawn_numbers = numbers[:5]
winners = set()
for i in range(5,len(numbers)):
    b = 0
    for board in boards:
        if check_win(board,drawn_numbers) == 'win':
            winners.add(b)
            
        b += 1
    if len(boards) == 1: break
    drawn_numbers.append(numbers[i]) # Dra ett nytt nummer


print(winners[-1])
unmarked_sum = 0
for line in boards[0]:
    for num in line:
        if num not in drawn_numbers:
            unmarked_sum += int(num)

print(unmarked_sum*int(drawn_numbers[-1]))