def word_match(words) :
    ctr = 0
    lst = []
    for word in words :
        if len(word)  > 1  and word[0]== word[-1]:
            ctr = ctr + 1
            lst.append(word)

    print("List of word with first and last character same\n", lst  )
    return ctr 

count = word_match(["abc",'tat',"lmn",'tan','quacq'])

print("number of words having the first and last character same =" , count )


        


    