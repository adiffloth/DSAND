## Request Routing with a Trie

The solution to this problem is implemented as a Trie where the directory structure of the website is represented as nodes in a Trie. Each node also carries a handler to process requests to a particular URL string.

The Router class handles parsing requests, adding handlers as nodes to the Trie and looking up handlers in the Trie.

The RouterTrie is the Trie itself and manages the nodes, insertions and searches among the nodes.

The RouteTrieNode has a dictionary to hold URL path parts and the corresponding children nodes, as well as the name of the handler for that node.

Time complexity: The worst case for lookup is O(n) where n is the depth of the longest valid path.

Space complexity: The worst case is O(n) where n is the number of pages in the site, if the site is completely flat, with only single pages under the root.