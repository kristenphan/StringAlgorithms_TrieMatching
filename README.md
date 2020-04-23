# Suffix Tree: Trie Matching

__Repository Description:__
<br/>
This repository stores the work as part of the Data Structures and Algorithms specialization courses by University California of San Diego. Course URL: https://www.coursera.org/specializations/data-structures-algorithms. Code in this repository is written by myself, Kristen Phan.
<br/>
<br/>
__Disclaimer__: 
<br/>
If you're currently taking the same course, please refrain yourself from checking out this solution as it will be against Coursera's Honor Code and won’t do you any good. Plus, once you're worked your heart out and was able to solve a particularly difficult problem, a sense of confidence you gained from such experience is priceless :)"
<br/>
<br/>
__Assignment Description:__
<br/>
Problem Introduction
Given a string Text and Trie(Patterns), we can quickly check whether any string from Patterns matches a
prefix of Text. To do so, we start reading symbols from the beginning of Text and see what string these
symbols “spell” as we proceed along the path downward from the root of the trie, as illustrated in the
pseudocode below. For each new symbol in Text, if we encounter this symbol along an edge leading down
from the present node, then we continue along this edge; otherwise, we stop and conclude that no string in
Patterns matches a prefix of Text. If we make it all the way to a leaf, then the pattern spelled out by this
path matches a prefix of Text.
<br/>
<br/>
This algorithm is called PrefixTrieMatching.
<br/>
<br/>
PrefixTrieMatching finds whether any strings in Patterns match a prefix of Text. To find whether any
strings in Patterns match a substring of Text starting at position 𝑘, we chop off the first 𝑘 −1 symbols from
Text and run PrefixTrieMatching on the shortened string. As a result, to solve the Multiple Pattern
Matching Problem, we simply iterate PrefixTrieMatching |Text| times, chopping the first symbol off of
Text before each new iteration.
<br/>
<br/>
Task 1: Implement TrieMatching algorithm.
Task 2: Extend TrieMatching algorithm so that it handles correctly cases when one of the patterns is a
prefix of another one.
<br/>
<br/>
Input Format: The first line of the input contains a string Text, the second line contains an integer 𝑛,
each of the following 𝑛 lines contains a pattern from Patterns = {𝑝1, . . . , 𝑝𝑛}.
<br/>
<br/>
Constraints: 1 ≤ |Text| ≤ 10 000; 1 ≤ 𝑛 ≤ 5 000; 1 ≤ |𝑝𝑖| ≤ 100 for all 1 ≤ 𝑖 ≤ 𝑛; all strings contain only
symbols A, C, G, T; no 𝑝𝑖 is a prefix of 𝑝𝑗 for all 1 ≤ 𝑖 ̸= 𝑗 ≤ 𝑛.
<br/>
<br/>
Output Format: All starting positions in Text where a string from Patterns appears as a substring in
increasing order (assuming that Text is a 0-based array of symbols).
<br/>
<br/>
Time Limits: Python - 7 seconds
<br/>
<br/>
Memory Limit. 512Mb.
<br/>
<br/>
