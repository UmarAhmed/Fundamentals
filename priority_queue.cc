#include "priority_queue.h"


// number of nodes in the heap
int PQ::size() {
    return items.size();
}


// return the value stored at the root
std::string PQ::getMax() {
    if (items.size()) {
        return items[0]->val;
    }
    throw;
}


// Time: O(log n) n = number of items in heap
void PQ::insert(int p, std::string s) {
    Node * fresh  = new Node {p, s};
    items.emplace_back(fresh);
    fixUp(items.size() - 1);
}

// restore ordering property given that all items
// are in order, except possibly item at index k
void PQ::fixUp(int k) {
    int p = (k - 1) / 2;
    while (k &&  (items[k]->key > items[p]->key)) {
        std::swap(items[k], items[p]);
        k = p;
        p = (k - 1) / 2;
    }
}


// restores order property top-down from index k
void PQ::fixDown(int k) {
    int c = 2 * k + 1;
    while (c < items.size()) {
        if (c + 1 < items.size() && items[c + 1]->key > items[c]->key) {
            c += 1;
        }
        if (items[k]->key < items[c]->key) {
            std::swap(items[k], items[c]);
            k = c;
            c = 2 * c + 1;
        } else {
            break;
        }
    }
}


// delete root
std::string PQ::deleteMax() {
    std::string result = items[0]->val;
    std::swap(items[0], items[items.size()]);
    items.pop_back();
    fixDown(0);
    return result;
}


// converts array into properly ordered heap
void PQ::heapify(int k) {
    if (k >= items.size()) {
        return;
    }
    heapify(2 * k + 1);
    heapify(2 * k + 2);
    fixDown(k);
}

