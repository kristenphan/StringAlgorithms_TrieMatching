# python3
import sys


# Return the trie built from patterns
# in the form of a dictionary of dictionaries,
# e.g. {0:{'A':1,'T':2},1:{'C':3}}
# where the key of the external dictionary is
# the node ID (integer), and the internal dictionary
# contains all the trie edges outgoing from the corresponding
# node, and the keys are the letters on those edges, and the
# values are the node IDs to which these edges lead.
def build_trie(patterns):
	tree = dict()
	tree[0] = {}  # initialize the root node as empty (ie. having no branches yet)
	node_id = 1  # id of the next node to be added to the trie
	for pattern in patterns:
		# when adding a new pattern to the trie, start from the root ie node 0
		curr_node = 0
		for let in pattern:
			# if there are outgoing edges from the current node,
			# check if one of the outgoing edge has same letter as the letter in pattern
			if bool(tree[curr_node]):
				# if yes, there is no need to add this letter to the trie
				# update curr_node and proceed to the next letter
				if let in tree[curr_node]:
					curr_node = tree[curr_node][let]
				# otherwise, add a new node to the trie,
				# branching from the current node to represent the letter
				else:
					new_node = node_id
					node_id += 1
					tree[curr_node][let] = new_node
					tree[new_node] = {}
					curr_node = new_node
			# if there is no outgoing edge from this node,
			# create a new node with a new node id and letter
			# attach the new node underneath the current node
			# update the current node as the new node and proceed to the next letter in the pattern
			else:
				new_node = node_id
				node_id += 1
				tree[curr_node][let] = new_node
				tree[new_node] = {}
				curr_node = new_node

	return tree


# this function takes in a subtext of the original Text, the index of the first letter of subtext in Text (ie. sub_text_start_pos),
# the trie that stores all Patterns to be searched for in subtext, and result which captures the starting positions of all matches found in Text
# the function traverses through the trie and subtext
# and records in result[] the starting position in the original Text where a string from Patterns appears as a substring
# in an increasing order (assuming that Text is a 0-based array of symbols)
# example:
# Text:     A A T C G T
#           0 1 2 3 4 5 <--- index of letters in Text
#
# subtext:  A T C G T
# subtext_start_pos = 2
# Patterns represented by trie and to be searched for in Text: ATCG, GGGT
# trie visualized as below:
#        (0) Root
#      /    \
#  A (1)    (5) G
#     |      |
#  T (2)    (6) G
#     |      |
#  C (3)    (7) G
#     |      |
#  G (4)    (8) T
# result = [2]
def prefix_matching(subtext, subtext_start_pos, trie, result):
	curr_node = 0 # keep track of the current node being traversed on trie
	# if the root has not outgoing edges, the trie is empty
	# and, therefore, there is no match
	if not bool(trie[curr_node]):
		return

	for i in range(len(subtext)):
		let = subtext[i]
		if bool(trie[curr_node]): # if there are outgoing edges from current node
			# if the letter of the text matches up with the letter in one of the outgoing edges
			# continue to next letter and keep count of the letters that have been matched up
			if let in trie[curr_node]:
				curr_node = trie[curr_node][let]
				#let_count += 1
				continue
			# no match found in subtext
			else:
				return

		# if there are no outgoing edges from the current node,
		# we've reached the leaf and a match for one of the patterns is found in subtext
		# append the starting position of this match to result
		else:
			result.append(subtext_start_pos)
			return


	# once we've reached the end of subtext, check if we've also reached a leaf of trie
	# if yes, a match is found
	# append the starting position of the match to result
	if not bool(trie[curr_node]):
		result.append(subtext_start_pos)
		return


# this function is a wrapper function to find all matches of Patterns in Text
# the function creates multiple substrings from Text (ie. substring  = text[i:] with i is the index of the first letter in the substring)
# finds matches of Patterns in the substrings
# and returns the starting positions of the matches found Text
def trie_matching(text, patterns):
	result = []
	trie = build_trie(patterns)
	for i in range(len(text)):
		prefix_matching(text[i:], i, trie, result)

	return result


# this program reads the input comprised of Text a n Patterns to be searched for in Text
# and returns all starting positions in Text where a string from Patterns appears as a substring in increasing order (assuminng that Text is a 0-based array of symbols)
# example:
# input (and how to interpret input):
# AATCGGGTTCAATCGGGGT <---- Text
# 2 <---------------------- n = number of patterns
# ATCG <------------------- pattern to be searched for in Text
# GGGT < ------------------ pattern to be searched for in Text
# output: 1 4 11 15
if __name__ == '__main__':
	text = sys.stdin.readline ().strip ()
	n = int (sys.stdin.readline ().strip ())
	patterns = []
	for i in range (n):
		patterns += [sys.stdin.readline ().strip ()]

	#text = 'AATCGGGTTCAATCGGGGT'
	#n = 2
	#patterns = ['ATCG', 'GGGT']

	ans = trie_matching(text, patterns)

	sys.stdout.write(' '.join(map(str, ans)) + '\n')
