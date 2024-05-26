def reversed(input_file, output_file):
    with open(input_file, "r", encoding="utf-8") as input, \
        open(output_file, "w", encoding="utf-8") as output:
            for line in input:
                if line == "":
                    print(line, file=output)
                elif (line[-1] == '\n'):
                    print(line[-2::-1], file=output)
                else:
                    print(line[::-1], file=output)

reversed("plik", "out")