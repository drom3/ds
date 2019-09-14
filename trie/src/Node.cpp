//
// Original Author: Daniel R.
//

#include "Node.hpp"

Node::Node(const char& key, bool state, int numKeys) {
    this->_key = key;
    this->_state = state;
    this->_capacity = numKeys;
    this->_size = 0;
    this->_key_set = new Node*[this->_capacity];

    // set all pointers in array to nullptr
    for (int i = 0; i < this->_capacity; ++i) {
        this->_key_set[i] = nullptr;
    }
}

Node::~Node() {
    // iterate through array of pointers
    for (int i = 0; i < this->_capacity; ++i) {
        // check if a pointer to a trie exist
        if (this->_key_set[i] != nullptr) {
            delete this->_key_set[i];
        }
    }
    // clean up
    delete[] this->_key_set;
    this->_key_set = nullptr;
}

void Node::add(int key, Node* node) {
    if (node != nullptr) {
        this->_key_set[key] = node;
        this->_size += 1;
    }
}

bool Node::remove_branch(int key) {
    if (key < 0 || key >= this->_capacity) {
        return false;
    }
    if (this->_key_set[key] != nullptr) {
        delete this->_key_set[key];
        this->_key_set[key] = nullptr;
        this->_size -= 1;
        return true;
    }
    return false;
}

bool Node::is_empty() {
    return this->_size == 0;
}

bool Node::is_empty_at(int key) {
    return this->_key_set[key] == nullptr;
}

int Node::size() {
    return this->_size;
}

int Node::get_capacity() {
    return this->_capacity;
}

bool Node::get_state() {
    return this->_state;
}

void Node::set_state(bool state) {
    this->_state = state;
}

char Node::get_key() {
    return this->_key;
}

Node* Node::get_node(int key) {
    return this->_key_set[key];
}

int Node::_match(const char& letter) {
    // based on LOWERCASE values of the alphabet.
    // only: 'a'...'z'
    return int(letter)-97;
}
