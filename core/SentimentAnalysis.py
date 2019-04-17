# -*- coding: utf-8 -*-

def sentimentAnalyser():
    pass



def main():
	p = [{'zero hello': "('Hey', 2)"}, {'zero hello': "('Hey', 2)"}]
	# parent_dict = list(parent_dict)
	# print(parent_dict)
	for dict_item in p:
		print("IN FOR")
		for key, value in dict_item.items():
			print(key)
			print(value)

main()