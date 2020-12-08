#!/usr/bin/env python3


class Computer:

    def __init__(self):
        self.accumulator = 0
        self.pointer = 0
        self.ops = {
            'acc': lambda v: (self.accumulator + v, self.pointer + 1),
            'jmp': lambda v: (self.accumulator, self.pointer + v),
            'nop': lambda v: (self.accumulator, self.pointer + 1)
        }
        self.visited = set()

    def exec_op(self, op, arg):
        acc = self.accumulator
        self.accumulator, self.pointer = self.ops[op](arg)
        if self.pointer in self.visited:
            return acc
        self.visited.add(self.pointer)

    def reboot(self):
        self.accumulator = 0
        self.pointer = 0
        self.visited = set()


def run():
    with open('input.txt') as fh:
        instructions = [line.strip() for line in fh]

    c = Computer()
    v = None
    while v is None:
        op, arg = instructions[c.pointer].split()
        v = c.exec_op(op, int(arg))
        if v:
            print(v)  # first answer

    mod = len(instructions)
    try:
        while True:
            for i in range(mod - 1, 0, -1):
                if instructions[i][:3] in ('nop', 'jmp'):
                    mod = i
                    old = instructions[mod]
                    instructions[mod] = ('nop' if old[:3] == 'jmp' else 'jmp') + old[3:]
                    break
            c.reboot()
            v = None
            while v is None:
                op, arg = instructions[c.pointer].split()
                v = c.exec_op(op, int(arg))
            instructions[mod] = old
    except IndexError:
        print(c.accumulator)  # second answer


if __name__ == '__main__':
    run()
