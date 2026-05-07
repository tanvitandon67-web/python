student_data = {'id1': {'name':'Sara','class': 5 , 'subject': 'coding'},
                'id2': {'name':'Mia','class': 5 , 'subject': 'coding'},
                'id3': {'name':'Sara','class': 5 , 'subject': 'coding'},
                'id4': {'name':'Tanvi','class': 6 , 'subject': 'coding'}
}

result = {}
seenkey = []

for studentid , details in  student_data.items() :
    unique_key = (details['name'],details['class'],details['subject'])
    
    if unique_key not in seenkey :
        seenkey.append(unique_key)

        result[studentid] = details

for k,v in result.items() :
    print(k,v)