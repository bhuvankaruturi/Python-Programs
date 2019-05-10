#!/usr/bin/python3

import os,sys

def tail_file(filename, nlines):
    with open(filename) as qfile:
        qfile.seek(0, os.SEEK_END)
        endf = position = qfile.tell()
        linecnt = 0
        while position >= 0:
            qfile.seek(position)
            next_char = qfile.read(1)
            if next_char == "\n" and position != endf-1:
                linecnt += 1

            if linecnt == nlines:
                break
            position -= 1

        if position < 0:
            qfile.seek(0)

        print(qfile.read(),end='')


if __name__ == '__main__':
    filename = sys.argv[1]
    nlines = int(sys.argv[2])
    tail_file(filename, nlines)