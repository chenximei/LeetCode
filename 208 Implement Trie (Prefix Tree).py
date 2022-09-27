class Trie(object):
    def __init__(self):
        """
        Initialize your data structure here.
        初始定义一个字典
        """
        self.root = {}
    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: None
        实现：这个操作和构建链表很像。首先从根结点的子结点开始与 word 第一个字符进行匹配，一直匹配到前缀链上没有对应的字符，
        这时开始不断开辟新的结点，直到插入完 word 的最后一个字符，同时还要将最后一个结点isEnd = true;，表示它是一个单词的末尾。
        """
        node = self.root
        for char in word:
            node = node.setdefault(char, {})

        node["end"] = True

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        从根结点的子结点开始，一直向下匹配即可，如果出现结点值为空就返回false，如果匹配到了最后一个字符，那我们只需判断node->isEnd即可。
        """
        node = self.root
        for char in word:
            if char not in node:
                return False
            node = node[char]

        return "end" in node

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        前缀匹配：判断 Trie 中是或有以 prefix 为前缀的单词
       实现：和 search 操作类似，只是不需要判断最后一个字符结点的isEnd，因为既然能匹配到最后一个字符，那后面一定有单词是以它
       为前缀的。
        """
        node = self.root
        for char in prefix:
            if char not in node:
                return False
            node = node[char]

        return True
