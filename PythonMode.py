data = []
data1 = []
repeat = True
while repeat:
    data.append(int(input("Enter a number: ")))
    if input("To stop, type 'n'. Otherwise, type anything else: ") == "n":
        repeat = False
for i in range(len(data)):
    data1.append(data.count(data[i]))
for i in range(len(data)):
    if data.count(data[i]) == max(data1):
        mode = data[i]
        break
if data.count(mode) == data1.count(max(data1)):
    print("The mode of your data is "+str(mode)+".")
else:
    print("Your data is multimodal.")
