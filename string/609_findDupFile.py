class Solution:
	def findDuplicate(self, paths):
		file_sys = {}
		res = []
		for path in paths:
			path = path.split(' ')
			for i in path[1:]:
				content = i[i.rfind("(")+1:-1]
				if content in file_sys.keys():
					file_sys[content].append((path[0]+'/'+i[:i.rfind("(")]))
				else:
					file_sys[content]=[(path[0]+'/'+i[:i.rfind("(")])]

		for cont in file_sys.keys():
			if len(file_sys[cont]) > 1:
				res.append(file_sys[cont])
		return res

input_list=["root/a 1.txt(abcd) 2.txt(efgh)", "root/c 3.txt(abcd)", "root/c/d 4.txt(efgh)", "root 4.txt(efgh)"]
Solution().findDuplicate(input_list)