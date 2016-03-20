#!/usr/bin/python

import hashlib

"""
Merkle Tree
"""
class Merkle:
	tree = []

	def __init__(self, strings):
		self.tree = strings
		
		if len(self.tree) % 2 == 1:
			self.tree.append(self.tree[-1])

	def md5(self, chunk):
		hash_md5 = hashlib.md5()
		hash_md5.update(chunk)

		return hash_md5.hexdigest()

	def merkle(self):
		while (len(self.tree) > 1):
			new_tree = []

			for i in xrange(len(self.tree) / 2):
				new_tree.append(self.md5(self.tree[i * 2]) + self.md5(self.tree[i * 2 + 1]))

			self.tree = new_tree

		return self.tree

m = Merkle([ 'a', 'b', 'c', 'd', 'e', 'f' ])
print m.merkle()