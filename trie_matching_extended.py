# python3
import sys


# this function takes in a list of Patterns and returns the trie built from Patterns
# in the form of a dictionary of dictionaries
# note that it's possible to have one pattern as a prefix of another one
# the trie uses a marker (True/ False) to indicate whether a node is the end of a pattern
# example:
# patterns = ['AT', 'A', 'AG']
# output = {0:{'A':[1, True]},
#           1:{'T':[2: True], 'G':[3: True]},
#           2:{},
#           3:{}}
# trie visualized as below
#                 (0) Root
#                  |
#          A-True (1)
#               /     \
#      T-True (2)     (3) G-True
def build_trie(patterns):
    tree = dict()
    tree[0] = {}  # initialize the root node as empty (ie. having no branches yet)
    new_node_id = 1  # id of the next node to be added to the trie
    for pattern in patterns:
        curr_node = 0  # when adding a new pattern to the trie, traverse the trie from root (node 0)
        n = len(pattern)
        for i in range(n):
            let = pattern[i]
            # create a marker pattern_end. marker = True if the current letter is the last letter in a pattern. otherwise False
            pattern_end = i == (n - 1)
            if bool(tree[curr_node]):  # if there are outgoing edges from the current node
                if let in tree[curr_node]:  # if one of the outgoing edges has same letter as the letter in pattern
                    if pattern_end:  # if the current letter is the last letter in pattern, update the marker
                        tree[curr_node][let][1] = True
                    curr_node = tree[curr_node][let][0]  # traverse to the next node

                else:  # no outgoing edges from current node has the same letter as the letter in pattern, add a new node to trie with a pattern_end marker
                    new_node = [new_node_id, pattern_end]
                    tree[curr_node][let] = new_node
                    tree[new_node_id] = {}
                    curr_node = new_node_id
                    new_node_id += 1

            else:  # there is no outgoing edge from curr_node
                # add a new node with node_id pattern_end marker to trie
                new_node = [new_node_id, pattern_end]
                tree[curr_node][let] = new_node
                tree[new_node_id] = {}
                # traverse to new node
                curr_node = new_node_id
                new_node_id += 1

    return tree


# this function takes in a subtext of the original Text, the index of the first letter of subtext in Text,
# a trie representing Patterns to be searched in Text,
# and an empty list result to store all starting positions in Text where a string from Patterns appears as a substring
# in increasing order (assuming that Text is a 0-based array of symbols)
# the function updates result when a match in found in subtext
# example:
# Text =   'ACATA'
#           01234 <--- index of letters in Text
#
# subtext = 'ATA'
# sub_text_start_pos = 2
# trie = {0:{'A':[1, True]},
#         1:{'T':[2: True], 'G':[3: True]},
#         2:{},
#         3:{}}
# trie visualized as below
#                  (0) Root
#                   |
#           A-True (1)
#                /     \
#       T-True (2)     (3) G-True
# result = [2]
def prefix_matching(subtext, subtext_start_pos, trie, result):
    curr_node = 0  # keep track of the current node being traversed on trie. start with the root (node 0)
    # if the root has not outgoing edges, the trie is empty --> there is no match
    if not bool(trie[curr_node]):
        return

    for i in range(len(subtext)):
        let = subtext[i]
        if bool(trie[curr_node]):  # if there are outgoing edges from current node
            if let in trie[curr_node]:  # if one of the edges has the same letter as the letter in subtext
                # retrieve the pattern_end marker that indicates whether the current node stores the last letter of one or more pattern in trie
                pattern_end = trie[curr_node][let][1]
                if pattern_end:  # if True, append the starting position to result
                    result.append(subtext_start_pos)
                # and traverse to next node
                curr_node = trie[curr_node][let][0]
                continue

            else:  # none of the outgoing edges from curr_node has the same letter as the letter in pattern. no match found in subtext
                return

        else:
            # there is no outgoing edge from curr_node, meaning we've reached a leaf in trie and a match has been found.
            # append the starting position to result
            result.append(subtext_start_pos)
            return

    # once we've reached the end of subtext, check if we've also reached a leaf of trie
    # if yes, a match is found. append the starting position of the match to result
    if not bool(trie[curr_node]):
        result.append(subtext_start_pos)
        return


# this function is a wrapper function to find all matches of Patterns in Text
# the function creates multiple substrings from Text (ie. substring  = text[i:] with i is the index of the first letter in the substring)
# finds matches of Patterns in the substrings
# and returns the starting positions of the matches found Text
# note that it's possible to have one pattern as a prefix of another one
# if more than one pattern appears starting at position 𝑖, output 𝑖 once
def trie_matching(text, patterns):
    result = []
    trie = build_trie(patterns)
    for i in range(len(text)):
        prefix_matching(text[i:], i, trie, result)

    return sorted(list(set(result)))  # eliminate duplicate starting positions and return results in ascending order


# this program reads the input comprised of Text a n Patterns to be searched for in Text
# and returns all starting positions in Text where a string from Patterns appears as a substring in increasing order (assuming that Text is a 0-based array of symbols)
# note that it's possible to have one pattern as a prefix of another one
# example:
# input (and how to interpret input):
# ACATA <---- Text
# 3  <---------- n = number of patterns
# AT <---------- pattern to be searched for in Text
# A  <---------- pattern to be searched for in Text
# AG <---------- pattern to be searched for in Text
# output: 0 2 4
if __name__ == '__main__':
    text = sys.stdin.readline().strip()
    n = int(sys.stdin.readline().strip())
    patterns = []
    for i in range(n):
        patterns += [sys.stdin.readline().strip()]

    ans = trie_matching(text, patterns)

    sys.stdout.write(' '.join(map(str, ans)) + '\n')
