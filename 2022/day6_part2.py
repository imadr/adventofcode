input_ = "mjqjpqmgbljsphdztnvjfqwrcgsmlb"

i = 0
for i in range(0, len(input_)):
    if len(set(input_[i:i+14])) == 14:
        break
print(i+14)