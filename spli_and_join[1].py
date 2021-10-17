def split_and_join(line):
    Out = line.split();
    Out = "-".join(Out)
    return Out;

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)