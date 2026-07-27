class TrieNode:
    """
    Represents a single node in the Trie.
    """
    def __init__(self):
        self.children = {}
        self.is_end = False  # Marks the end of a valid word
        self.suggestion =[]


class Trie:
    """
    A Trie for storing and searching words.
    """
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word,mapping):
        """
        Insert a word into the Trie.
        """
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end = True
        if len(node.suggestion)==0:
            node.suggestion=[mapping]
        else:
            (node.suggestion).append(mapping)

    def search(self, word):
        """
        Search for a word in the Trie.
        Returns True if the word exists, False otherwise.
        """
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end

    def getSuggestion(self, word):
        """
        Search for a word in the Trie.
        Returns True if the word exists, False otherwise.
        """
        node = self.root
        for char in word:
            if char not in node.children:
                return []
            node = node.children[char]
        if node.is_end:
            return node.suggestion
        else:
            return []
    def starts_with(self, prefix):
        """
        Check if any word in the Trie starts with the given prefix.
        """
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True

    def Load_Trie(self, filepath, reverse=False):
        """
        Check if any word in the Trie starts with the given prefix.
        """
        with open(filepath,"r",encoding="utf-8") as f:
            word_list = f.read().split('\n')
        for pair in word_list:
            key,value = pair.split('=')
            if reverse:
                self.insert(value,key)
            else:
                self.insert(key,value)


# # Example Usage
# if __name__ == "__main__":
#     # List of words to store
#     # with open("hn.txt","r",encoding="utf-8") as f:
#     #   word_list = f.read().split('\n')

#     # Initialize the Trie
#     trie = Trie()
#     hin_eng_trie = Trie()

#     # Insert words into the Trie
#     # for pair in word_list:
#     #     key,value = pair.split('=')
#     #     trie.insert(key,value)
#     trie.Load_Trie("hn.txt")
#     hin_eng_trie.Load_Trie("hn.txt",True)
#     # Search for words
#     print("Search Results:")
#     print(f" {trie.search('parwal')}")    # True
#     with open("out.txt","w",encoding="utf-8") as f:
#         print(f" {trie.getSuggestion('parwal')}")    # True
#         f.write(f" {trie.getSuggestion('parwal')}")    # True
#         print(f" {hin_eng_trie.getSuggestion('परव')}")    # True
#         f.write(f" {hin_eng_trie.getSuggestion('परवाल')}")    # True
    
#     # Check for prefixes
#     # print("\nPrefix Results:")
#     # print(f" {trie.starts_with('कर')}")  # True