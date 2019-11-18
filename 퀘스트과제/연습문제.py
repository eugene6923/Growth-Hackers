class stock_analysis:
   def __init__(self,code):
       try:
           a = open("D:\\그로스해커스\\파이썬세션데이터\\{0}.csv".format(code),'r')
           self.lines = a.readlines()
       except:
           print("파일명 혹은 경로가 잘못되었습니다")
       else:
           self.len = len(self.lines)
           self.latest_close = int(self.lines[-1].split(',')[4])
           self.latest_open = int(self.lines[-1].split(',')[1])
           self.latest_low = int(self.lines[-1].split(',')[2])
           self.latest_high = int(self.lines[-1].split(',')[3])
   def close_mean(self):
       close = [int(i.split(',')[4]) for i in self.lines[1:]]
       return sum(close)/len(close)
   def close_variance(self):
       close = [int(i.split(',')[4]) for i in self.lines[1:]]
       return sum([(int(i.split(',')[4]) - self.close_mean())**2 for i in self.lines[1:]]) / len(self.lines[1:])
   def close_std(self):
       close = [int(i.split(',')[4]) for i in self.lines[1:]]
       return (self.close_variance())**0.5
   def volume_mean(self):
       close2 = [int(i.split(',')[5].strip()) for i in self.lines[1:]]
       return sum(close2)/len(close2)
   def MA5(self):
       MAC_dict={}
       for i in range(5,self.len):
           MAC_dict[self.lines[i].split(',')[0]]=sum(int(self.lines[i].split(',')[4])for i in range(i-4,i+1))/5
       return MAC_dict

df = pd.read_csv("D:\\그로스해커스\\파이썬세션데이터\\네이버_new.csv", engine = 'python')
df['종가'] = df[['종가']].apply(lambda x: (-1) * x, axis = 1)
df['당일 상승폭'] = (df['종가'] - df['시가'])/df['시가']
print(df[(df['일자'] >= '2013-03-01') & (df['일자'] <= '2013-06-01')]['당일 상승폭'].std())
print(df[df['거래량'] >= 1.5*df['거래량']. mean()]['종가'].mean())
