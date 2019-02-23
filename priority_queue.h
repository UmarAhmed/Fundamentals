#include <string>
#include <vector>


struct Node {
    int key;
    std::string val;
};


class PQ {
    std::vector<Node*> items;
    void fixUp(int k);
    void fixDown(int k);
public:
    PQ(std::vector<Node*> i): items {i}{}
    void insert(int p, std::string s);
    std::string getMax();
    std::string deleteMax();
    int size();
    void heapify(int k);
};

