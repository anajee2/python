def quiz_2(file_name):
    data_split = {}
    file1 = open(file_name, "r")
    text = file1.readlines()
    # z = "".join(text)
    for line in text:
        data = line.split()

        for i in data:
            if "key:" in i:
                print(data.index("key:"))
                data_split[data[1] + data[2]] = data[0]
            if "value:" in i:
                print(data.index("value:"))
                data_split.update()
    print(data_split)


quiz_2('q2.txt')
