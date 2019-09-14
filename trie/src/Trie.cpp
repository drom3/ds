//
// Original Author: Daniel R.
//

#include "Trie.hpp"

/**
 * Trie Constructor:
 */
Trie::Trie() {
    this->_size = 0;
    this->_root = new Node('*');
}

/**
 * Destructor:
 *     Clean up all memory used.
 */
Trie::~Trie() {
    delete this->_root;
    this->_root = nullptr;
    this->_size = 0;
}

bool Trie::insert(const std::string& str) {
    // error check
    if (!this->_check_format_and_duplicates(str)) {
        return false;
    }

    // set starting point
    Node* current = nullptr;
    current = this->_root;

    for (auto chr = str.cbegin(); chr != str.cend(); ++chr) {
        // check if finished iterating through string
        bool finished = next(chr) == str.cend();
        // find array index reprsentation
        int i = this->_match(*chr);

        // node doesn't exist, create new node
        if (current->is_empty_at(i)) {
            // add node to key-set
            current->add(i, new Node(*chr, finished));
            if (finished) {
                this->_size += 1;
                break;
            }
        }
        // string already exists
        else if (finished) {
            // change state of node to finished
            current->get_node(i)->set_state(true);
            this->_size += 1;
            break;
        }

        // continue moving through nodes
        current = current->get_node(i);
    }
    // clean up
    current = nullptr;
    return true;
}

bool Trie::contains(const std::string& str) {
    if (str.empty()) {
        return false;
    }
    bool found = false;

    Node* current = nullptr;
    current = this->_root;

    // iterate through string
    for (auto chr = str.cbegin(); chr != str.cend(); ++chr) {
        int i = this->_match(*chr);

        // check character formatting
        if (i < 0 || i >= current->get_capacity()) {
            found = false;
            break;
        }

        // node doesn't exist
        if (current->is_empty_at(i)) {
            found = false;
            break;
        }

        // next node
        current = current->get_node(i);

        // string found in trie
        if (next(chr) == str.cend() && current->get_state() == true) {
            found = true;
        }
    }
    // clean up
    current = nullptr;
    return found;
}

bool Trie::remove(const std::string& str) {
    if (str.empty()) {
        return false;
    }
    // pointer for deletion
    Node* start = nullptr;

    // pointer for iteration
    Node* current = nullptr;
    current = this->_root;

    // safe to delete node
    bool safe = true;

    // resets start pointer to different position
    bool reset = false;

    // index to begin deletion
    int target_index = -1;

    // return value
    bool removed = false;

    // iterate through string
    for (auto chr = str.cbegin(); chr != str.cend(); ++chr) {
        int i = this->_match(*chr);
        // check character formatting
        if (i < 0 || i >= current->get_capacity()) {
            removed = false;
            break;
        }

        // trie doesn't contain the string
        if (current->is_empty_at(i)) {
            removed = false;
            break;
        }

        // set start pointer to the root node
        if (chr == str.cbegin()) {
            // set starting position
            start = current;
            // save target index for deletion
            target_index = i;
        }


        // iterate through trie
        current = current->get_node(i);

        // reset the starting pointer
        if (reset == true) {
            // save index for deletion
            target_index = i;
            // done resetting
            reset = false;
        }

        //  check reset conditions for the start pointer:
        //  1. node has multiple children
        //  2. another string exists within string
        if (current->size() > 1 || (current->get_state() == true && next(chr) != str.cend())) {
            // reset the starting pointer
            reset = true;
            // save parent node
            start = current;
        }


        // finished iteration
        if (next(chr) == str.cend() && current->get_state() == true) {

            // unsafe to delete nodes
            if (!current->is_empty()) {
                // hide string in trie instead
                current->set_state(false);
            }

            // delete nodes starting from start node
            else {
                start->remove_branch(target_index);
            }
            removed = true;
            this->_size -= 1;
            break;
        }
    }

    // clean up
    start = nullptr;
    current = nullptr;

    return removed;
}

/**
* display:
*    prints all the Nodes in the Trie.
*/
void Trie::display() {
    Node* root = nullptr;
    root = this->_root;

    //std::cout << "----- begin -----" << std::endl;

    // begin recursive call
    this->_display(root);

    //std::cout << "----- end -----" << std::endl;

    // clean up
    root = nullptr;
}

/** helper function **/
void Trie::_display(Node* start) {
    /*
    std::cout <<  "key: "  << start->get_key() << ", "
              << "state: " << start->get_state()
              << std::endl;
    */
    for (int i = 0; i < start->get_capacity(); ++i) {
        if (!start->is_empty_at(i)) {
            // recursive call
            _display(start->get_node(i));
        }
    }
}

int Trie::size() {
    return this->_size;
}

/** Exceptions for logging **/
bool Trie::_check_format_and_duplicates(const std::string& str) {

    bool duplicate_error = false;
    bool syntax_error = false;

    if (str.empty()) {
        syntax_error = true;
    }

    else {
        Node* node_ptr = nullptr;
        node_ptr = this->_root;

        bool found = true;

        // iterate through string
        for (auto chr = str.cbegin(); chr != str.cend(); ++chr) {
            // find array index reprsentation
            int i = this->_match(*chr);

            // check character value
            if (i < 0 || i >= node_ptr->get_capacity()) {
                syntax_error = true;
                break;
            }

            // check for duplicates in trie
            if (node_ptr->is_empty_at(i)) {
                // stop iterating through trie
                found = false;
            }

            // iterate through trie
            if (found) {
                node_ptr = node_ptr->get_node(i);
                // duplicate found in trie
                if (next(chr) == str.cend() && node_ptr->get_state() == true) {
                    duplicate_error = true;
                    break;
                }
            }
        }
        // clean up
        node_ptr = nullptr;
    }

    /** duplicate_error:
    *       string already represented in the Trie.
    */
    if (duplicate_error) {
        // show in log
    }

    /** syntax_error:
    *       string incorrectly formatted.
    */
    if (syntax_error) {
        // show in log
    }

    // no errors found
    return duplicate_error == syntax_error;
}


int Trie::_match(const char& chr) {
    // based on LOWERCASE values of the alphabet.
    // only: 'a'...'z'
    return int(chr)-97;
}
