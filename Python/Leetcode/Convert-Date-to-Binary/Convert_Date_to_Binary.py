class Solution:
    def convertDateToBinary(self, date: str) -> str:
        year, month, day = date.split('-')
 
        year = self.getBinary(int(year))
        month = self.getBinary(int(month))
        day = self.getBinary(int(day))
        return year + "-" + month + "-" + day
    
    def getBinary(self, num):
        binary = ""
        new_num = 0
        count = 0
        i = 1
        
        while new_num <= num:
            new_num = 2 ** i
            i += 1
            count += 1
        new_num = 0

        for i in range(count-1, -1, -1):
            new_num += (2 ** i)
            if  new_num <= num:
                binary += "1"
            else:
                new_num -= (2 ** i)
                binary += "0"

        return binary