# input for submarine

class submarine():

    def __init__(self, depth = 0, horizontal = 0, aim = 0):
        self._depth = depth
        self._horizontal = horizontal
        self._aim = aim

    def get_aim(self):
        return self._aim

    def get_depth(self):
        return self._depth

    def get_horizontal(self):
        return self._horizontal

    def change_position(self, command, x):

        if command.lower() == 'up':
            # self._depth = self.get_depth()-x
            self._aim = self.get_aim()-x

        if command.lower() == 'down':
            # self._depth = self.get_depth()+x
            self._aim = self.get_aim()+x

        elif command.lower() == 'forward':
            self._horizontal = self.get_horizontal()+x
            self._depth = self.get_depth()+(self.get_aim()*x)

       
        

if __name__ == '__main__':
    with open('data2.txt', 'r', encoding='UTF-8') as file:
            lines = file.read()
    lines = lines.split('\n')
    new_list = []
    for line in lines:
        line = (line.split(' '))
        new_list.append(line)
    sub = submarine()
    for line in new_list:
        command = line[0]
        x = int(line[1])
        sub.change_position(command,x)

    print(sub.get_depth()*sub.get_horizontal())