class Solution:
    def reformatDate(self, date: str) -> str:
        date_ = date.split()
     
        
        monthList = {'Jan': '01', 'Feb': '02', 
                     'Mar': '03', 'Apr': '04', 
                     'May': '05', 'Jun': '06', 
                     'Jul': '07', 'Aug': '08', 
                     'Sep': '09', 'Oct': '10', 
                     'Nov': '11', 'Dec': '12'}
        
        day = date_[0][:-2] 
        month = date_[1] 
        year = date_[2]
        
        if int(day) < 10: 
            day = '0' + day
        
        return ''.join(f'{year}-{monthList[month]}-{day}') 
        
        