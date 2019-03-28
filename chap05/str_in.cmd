>>> 'Jan' in '01 Jan 1838' 
True 
>>> 'Feb' in '01 Jan 1838' 
False 
>>> date = input('DD MTH YYYY 형식으로 날짜를 입력하세요: ') 
DD MTH YYYY 형식으로 날짜를 입력하세요: 24 Feb 2013
>>> 'Jan' in date
False 
>>> date = input('DD MTH YYYY 형식으로 날짜를 입력하세요: ') 
DD MTH YYYY 형식으로 날짜를 입력하세요: 03 Jan 2002
>>> 'Jan' in date 
True 
>>> 'a' in 'abc' 
True
 >>> 'A' in 'abc' 
False 
>>> '' in 'abc' 
True
>>> '' in '' 
True 