#include "Trie.hpp"
#include <iostream>

int main() {
    /** example: **/
    // create
    Trie* trie = nullptr;
    trie = new Trie();

    /* note: 1=success, 0=failure. */
    /* note: trie.display() needs to be modified first. */

    // insert
    std::cout << "Insert: " << std::endl;
    std::cout <<  "[insert]: " << trie->insert("race") << std::endl;
    std::cout <<  "[insert]: " << trie->insert("rice") << std::endl;
    std::cout <<  "[insert]: " << trie->insert("racecar") << std::endl;
    std::cout <<  "[insert]: " << trie->insert("rack") << std::endl;
    std::cout <<  "[insert]: " << trie->insert("race") << std::endl;  // duplicate, fail
    std::cout <<  "[size]: " << trie->size() << std::endl;

    // contains
    std::cout << "Contains: " << std::endl;
    std::cout <<  "[contains]: " << trie->contains("race") << std::endl;
    std::cout <<  "[contains]: " << trie->contains("rice") << std::endl;
    std::cout <<  "[contains]: " << trie->contains("racecar") << std::endl;
    std::cout <<  "[contains]: " << trie->contains("rack") << std::endl;
    std::cout <<  "[contains]: " << trie->contains("racecars") << std::endl; // doesn't exist

    // remove
    std::cout << "Remove: " << std::endl;
    std::cout <<  "[remove]: " << trie->remove("race") << std::endl;
    std::cout <<  "[remove]: " << trie->remove("rice") << std::endl;
    std::cout <<  "[remove]: " << trie->remove("racecar") << std::endl;
    std::cout <<  "[remove]: " << trie->remove("rack") << std::endl;
    std::cout <<  "[remove]: " << trie->remove("race") << std::endl;  // doesn't exist anymore.
    std::cout <<  "[size]: " << trie->size() << std::endl;

    // clean up
    delete trie;
    trie = nullptr;
    return 0;
}
