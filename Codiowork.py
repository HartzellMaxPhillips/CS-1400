with open("myanmar.txt", "r" ) as input_file:
  text = input_file.readlines()
  for line in text:
    for char in range(len(line)):
        if line[char] == "B":
            if line[char:char+5] == "Burma":
                print("Found Burma")