import pandas as pd

data = []
filter_key = ['section', 'network']

with open('revamp-20250608014502.txt', 'r',encoding='utf-8') as file:
    lines = file.read().strip().split('\n')
#print(lines)

for i in range(0, len(lines), 1):
    if lines[i].__contains__(filter_key[0]) and lines[i].__contains__(filter_key[1]):
        # The find() method returns the index of first occurrence of the substring (if found). If not found, it returns -1.
        start = lines[i].find('{')
        #print(start)
        end = lines[i].find('}', start)
        #print(end)

        if start != -1 and end != -1:
            value = lines[i][start + 1:end]# value holds the data inside {}
            print(value)
            #data.append(value)
            row = {}
            #if value.__contains__(""):
            pairs = value.split(", '")# split on ",'" to handle- 'Network'=> 'LTE,LTE', 'device'=> 'vivo'
            print(pairs)
            for pair in pairs:
                # Spliting into  key and value pair using =>
                if '=>' in pair:
                    key_part, value_part = pair.split('=>')
                    # remove "'"  from key and value
                    key = key_part.replace("'", "")

                    value_of_key = value_part.replace("'", "")

                    row[key] = value_of_key


            data.append(row)


#print(data)
df = pd.DataFrame(data)
df = df.fillna('')
df=df.astype('str') # converting into str so that leading zero in mobileNo remains the same
#print(df)
df.to_excel('revamp_updated1.xlsx', index=False)







'''line = "hello{text}"
#The find() method returns the index of first occurrence of the substring (if found). If not found, it returns -1.
start = line.find('{')
print(start)
end = line.find(')', start)
print(end)

if start != -1 and end != -1:
    value = line[start+1:end]
    print("Value inside brackets:", value)
else:
    print("Brackets not found properly.")
'''