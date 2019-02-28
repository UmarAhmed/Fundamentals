#include "scapegoat.h"
#include <iostream>
#include <vector>
#include <math.h>

// Find kth smallest item in tree
// 0 <= k < number of items in tree
// O (log n) worst case time
int Scapegoat::selectHelper(Node * root, int k) const {
    // Check for current root
    if (root->left && root->left->size == k) {
        return root->val;
    }
    if (root->left == nullptr && k == 0) {
        return root->val;
    }
    // Recurse on either left or right
    int leftSize = 0;
    if (root->left) {
        leftSize = root->left->size;
        if (leftSize > k) {
            return selectHelper(root->left, k);
        }
    }
    return selectHelper(root->right, k - leftSize - 1);
}

int Scapegoat::select(int k) const {
    return selectHelper(root, k);
}


namespace {
    int log32(int r) {
        double const log23 = 2.4663034623764317;
        int result = 1 + log23 * log(r);
        return result;
    }
}


// Should extract all values in the subtree rooted at root
// using an inorder traversal. Then it should rebuild the 
// subtree as a balanced tree using median + recursion
void Scapegoat::rebuild(Node * root) {


}


// O(log n) amortized time
void Scapegoat::insert(int v) {
    if (root == nullptr) {
        root = new Node {v};
        return;
    }
    std::vector <Node *> stack;
    Node * parent = nullptr;
    Node * current = root;
    bool r = 0;
    // Navigate to leaf where item should be inserted
    while (current) {
        current->size += 1;
        parent = current;
        stack.emplace_back(current);
        if (current->val > v) {
            current = current->left;
            r = 0;
        } else {
            current = current->right;
            r = 1;
        }
    }
    if (r) {
        parent->right = new Node {v};
    } else {
        parent->left = new Node {v};
    }

    // Check if we need to rebuild
    if (stack.size() > log32(root->size)) {
        int i = 0;
        while (3 * stack[i + 1]->size < 2 * stack[i]->size) {
            i += 1;
        }
        // We rebuild the tree at stack[i]
        rebuild(stack[i]);
    }
}


int main() {
    Scapegoat goat;
    goat.insert(2);
    goat.insert(1);
    goat.insert(3);
    std::cout << goat.select(2) << std::endl;
}
