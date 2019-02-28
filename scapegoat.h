#ifndef _SCAPEGOAT_H_
#define _SCAPEGOAT_H_


class Scapegoat {
    float a = 1.5; // reciprocal of alpha = 2/ 3
    // Augmented nodes contain size of subtree
    struct Node {
        int val;
        Node * left;
        Node * right;
        int size;
        Node(int v): 
            val {v}, left {nullptr}, right {nullptr}, size {1} {} 
        ~Node() {
            delete left;
            delete right;
        }
    };
    Node * root;
    int selectHelper(Node *, int) const;
    void rebuild(Node *);
public:
    Scapegoat(): root {nullptr} {}
    // find node with value v
    bool search(int) const;
    // insert node with value v into tree
    void insert(int);
    // find kth smallest item in tree (0 indexing)
    int select(int) const;

};


#endif

