//
// Original Author: Daniel R.
//

#ifndef TRIE_HPP
#define TRIE_HPP

#include <string>
#include "Node.hpp"

/**
 * Trie class:
 *
 * Used as interpretation of the Trie object.
 *
 */
class Trie {
private:
    // Number of strings in Trie.
    int _size;
    // Root node.
    Node* _root = nullptr;
public:
    /**
     * Trie Constructor:
     */
    Trie();

    /**
     * Destructor:
     *     Clean up all memory used.
     */
    ~Trie();

    /**
    * insert:
    *    inserts string representation into the Trie.
    *
    * @param string str
    * @return true: str was inserted into the trie.
    *         false: str was unable to be inserted
    *                ** String is incorrectly formatted.
    *                ** String already existed in Trie.
    */
    bool insert(const std::string& str);

    /**
    * contains:
    *    determines whether the string is stored in the Trie.
    *
    * @param string str
    * @return true: str was in the Trie.
    *         false: str didn't exist in Trie.
    */
    bool contains(const std::string& str);

    /**
    * remove:
    *    removes the string from the representation.
    *
    * @param string key
    * @return true: key was in the Trie and was removed.
    *         false: key didn't exist in Trie.
    */
    bool remove(const std::string& str);

    /**
    * display:
    *    prints all the Nodes in the Trie.
    */
    void display();

    /**
    * size:
    *    returns the number of strings in the Trie.
    *
    * @return int: number of strings in Trie.
    */
    int size();

private:
    /******************************************
    * Helper functions:
    ******************************************/

    /**
    * _match:
    *    Maps char to an array index value.
    *
    * @param char chr
    * @return int: representation of an array index value.
    */
    int _match(const char& chr);

    /**
    * _display:
    *    Parent function: display()
    *    Recursive call to iterate through each node in the Trie and
    *    display their contents.
    *
    * @param Node* start
    */
    void _display(Node* start);

    /******************************************
    * Exceptions:
    ******************************************/

    /**
    * Modify if:
    *   - all inputs are unique.
    *   - all inputs are correctly formatted.
    */
    /**
    * _check_format_and_duplicates:
    *    Evaluates string for formatting and possible duplicates in Trie.
    *
    * @param string str
    * @return true: key was in the Trie and was removed.
    *         false: key didn't exist in Trie.
    */
    bool _check_format_and_duplicates(const std::string& str);
};

#endif //TRIE_HPP
