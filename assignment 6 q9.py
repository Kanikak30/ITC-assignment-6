class Validity:
    bracts = [['(','{','['],[')','}',']']]
    
    def __init__(self, str1):
        self.order = str1
        self.valid = 'Valid'
    
    def IsValid(self):
        list1 = list(map(str,self.order))
        #print(list1)
        for i in range(len(list1)):
            if list1[i] in self.bracts[0]: 
                h = self.bracts[0].index(list1[i])
                if list1[i+1] != self.bracts[1][h]: self.valid = 'Invalid.'
            
            
            #else: self.valid = 'No Opening Bracks.'

idk = Validity(input())
idk.IsValid()
print(idk.valid)
