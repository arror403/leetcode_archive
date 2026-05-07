class Trie {
public:
    vector<string> m;
    Trie() {
        m={};
    }
    
    void insert(string word) {
        m.push_back(word);
    }
    
    bool search(string word) {
        for (auto i:m){
            if (i==word) return true;
        }
        return false;
    }
    
    bool startsWith(string prefix) {
        for (auto i:m){
            if (i.substr(0, prefix.length()) == prefix) {
                return true;
            }
        }
        return false;
        
    }
};

/**
 * Your Trie object will be instantiated and called as such:
 * Trie* obj = new Trie();
 * obj->insert(word);
 * bool param_2 = obj->search(word);
 * bool param_3 = obj->startsWith(prefix);
 */