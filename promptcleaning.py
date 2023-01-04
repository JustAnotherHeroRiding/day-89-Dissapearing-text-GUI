with open("prompts.txt",encoding="utf8") as f:
    data = [line.strip() for line in f if line.strip() != ""]
    
    
#data = [data.split('.')[1].strip() for data in data]

#print(data)