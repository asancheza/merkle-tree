#!/usr/bin/python

import hashlib

def md5(chunk):
	hash_md5 = hashlib.md5()
	hash_md5.update(chunk)

	return hash_md5.hexdigest()

tree = [ 'a', 'b', 'c', 'd', 'e', 'f' ]

if tree % 2 == 1:
  tree.append(tree[-1])

while (len(tree) > 1):
	new_tree = []

	for i in xrange(len(tree) / 2):
	  new_tree.append(md5(tree[i * 2]) + md5(tree[i * 2 + 1]))

	tree = new_tree

print tree