class pair_element :
    def twosum(self,nums,target) :
        lookup = {}


        for i,num in enumerate(nums) :
            if target - num in lookup :

                return(lookup[target - num], i )
            
            lookup[num] = i

values = int(input("Enter sum of which you waant to make this search : "))
print("index1 = %D , index2 = %D"%pair_element().twosum((10,20,30,40,50,60,70,80,90),values) )


    