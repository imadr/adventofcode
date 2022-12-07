input_ = "zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw"

i = 0
for i in range(0, len(input_)):
    if len(set(input_[i:i+4])) == 4:
        break
print(i+4)