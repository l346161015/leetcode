class Caculate(object):
  def caculate(self,strs):
    #为空则返回 ‘’
    if not strs:
      return ''
    
    #计算strs中最短字符串
    shortest = min(strs,key=len)
    #用最短字符串去比较
    for x,y in enumerate(shortest):
      for s in strs:
        if s[x] != y:
          return s[:x]
    return shortest

