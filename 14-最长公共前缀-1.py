class Solution(object):
	def cul_chart(self,str_alist,str_blist):
		max_str = ''
		for num in range(len(str_alist)):
			long_str = self.digui(num,str_alist,str_blist)
			if len(long_str) > len(max_str):
				max_str = long_str
		return max_str[0:len(max_str)-1]

	def digui(self,num,str_alist,str_blist,long_str=''):
		long_str += str_alist[num]
		if long_str in str_blist and num<len(str_alist)-1:
			return self.digui(num+1,str_alist,str_blist,long_str)
		else:
			return long_str

if __name__ == '__main__':
	clu = Solution()
	a = 'adfafailgnnaooooooijg'
	b = 'dagfailganbdnaooooooofgadfgaj'
	print(clu.cul_chart(a,b))
