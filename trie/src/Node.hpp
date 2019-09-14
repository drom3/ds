//
// Original Author: Daniel R.
//

#ifndef NODE_HPP
#define NODE_HPP

/**
 * Node class:
 *
 * Used for representing Nodes within a Trie.
 */
class Node {
private:
    /** Member variables */
    char _key;
    bool _state;
    int _capacity;
    int _size;


    // array of links other nodes.
    Node** _key_set = nullptr;

    /**
    * Default Constructor:
    *    Set to private to be disabled.
    *    We only allow for a Node to be initialized
    *    with specific starting values.
    */
    Node();

public:
   /**
    * Constructor to set the initial size of the number of keys.
    *    The number of keys is fixed.
    *
    * @param key - identification of the node.
    * @param state - records the progress of the node relative to its insertion.
    *                true: end of progress.
    *                false: in-progress.
    * @param numKeys - number of keys to allocate for.
    */
    Node(const char& key, bool state = false, int numKeys = 26);

    /**
     * Destructor:
     *     Clean up all memory used.
     */
    ~Node();

    /**
    * add:
    *    add node to the location indexed by key in the current nodes key-set.
    *
    * @param char key
    * @return true: new node was added to the current nodes key-set.
    *         false: node was unable to be inserted:
    *                ** Key is incorrect.
    *                ** Key already existed in current nodes key-set.
    */
    void add(int key, Node* node);

    /**
    * remove:
    *    removes all nodes from an index in the current nodes key-set.
    *
    * @param char key
    * @return true: key was in the key-set and all nodes were removed.
    *         false: key didn't exist in key-set.
    */
    bool remove_branch(int key);

    /**
    * size:
    *    amount of child nodes that a node has.
    *
    * @return int: number of child nodes.
    */
    int size();

    /**
    * is_empty:
    *    checks if any links to other nodes exist.
    *
    * @return true: node doesn't have any children.
    *         false: node has children.
    */
    bool is_empty();

    /**
    * is_empty_at:
    *    checks if a link to another node exists by key.
    *
    * @ param int key
    * @return true: node doesn't have a child at key.
    *         false: node has child at key.
    */
    bool is_empty_at(int key);

    /** Getters & Setters **/
    bool get_state();
    void set_state(bool state);
    char get_key();
    int get_capacity();
    Node* get_node(int key);


private:
    /**
    * _match:
    *    converts char to an array index value based on ascii represenation.
    *
    *    based on LOWERCASE values of the alphabet.
    *    only: 'a'...'z'.
    *
    * @param char chr
    * @return int: array index represenation of char.
    */
    int _match(const char& chr);
};

#endif //NODE_HPP
