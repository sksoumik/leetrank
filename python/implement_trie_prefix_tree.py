# https://leetcode.com/problems/implement-trie-prefix-tree/

# A trie (pronounced as "try") or prefix tree is a tree data structure used to 
# efficiently store and retrieve keys in a dataset of strings. There are various 
# applications of this data structure, such as autocomplete and spellchecker.

# Implement the Trie class:

# Trie() Initializes the trie object.
# void insert(String word) Inserts the string word into the trie.
# boolean search(String word) Returns true if the string word is in the trie 
# (i.e., was inserted before), and false otherwise.
# boolean startsWith(String prefix) Returns true if there is a previously inserted 
# string word that has the prefix prefix, and false otherwise.

# Input
# ["Trie", "insert", "search", "search", "startsWith", "insert", "search"]
# [[], ["apple"], ["apple"], ["app"], ["app"], ["app"], ["app"]]
# Output
# [null, null, true, false, true, null, true]

# Explanation
# Trie trie = new Trie();
# trie.insert("apple");
# trie.search("apple");   // return True
# trie.search("app");     // return False
# trie.startsWith("app"); // return True
# trie.insert("app");
# trie.search("app");     // return True


class Trie:
    def __init__(self):
        self.root = {}

    def insert(self, word: str) -> None:
        """
        For each character in the word, we create a new node if it doesn't exist, and then we move to
        the next node. At the end of the word, we add a "#" to indicate that this is the end of the word.
        """
        node = self.root
        for char in word:
            node = node.setdefault(char, {})
        node["#"] = "#"

    def search(self, word: str) -> bool:
        """
        We start from the root node and traverse the trie until we reach the end of the word. 
        
        If we reach the end of the word and the last node we visited is a leaf node, then the word
        exists in the trie. 
        
        If we reach the end of the word and the last node we visited is not a leaf node, then the word
        does not exist in the trie.
        """
        node = self.root
        for char in word:
            if char not in node:
                return False
            node = node[char]
        return "#" in node

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for char in prefix:
            if char not in node:
                return False
            node = node[char]
        return True


if __name__ == "__main__":
    trie = Trie()
    trie.insert("apple")
    print(trie.search("apple"))  # True
    print(trie.search("app"))  # False
    print(trie.startsWith("app"))  # True
    trie.insert("app")
    print(trie.search("app"))  # True


