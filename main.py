from codecs import namereplace_errors
from DS.BinarySearchTree import BinarySearchTree
from DS.LinkedList import LinkedList
from DS.Stack import Stack
from DS.Queue import Queue
from DS.DoublyLinkedList import DoublyLinkedList
from DS.HashTable import HashTable

def find_kth_from_end(ll: LinkedList, k):
    slow = fast = ll.head
    for iter in range(k):
        if fast == None:
            return None
        fast = fast.next
    
    while fast is not None:
        slow = slow.next
        fast = fast.next

    return slow

def item_in_common(list1, list2):
    my_dict = {}
    for item in list1:
        my_dict[item] = True
    for item in list2:
        if item in my_dict:
            return True
        
    return False

def first_non_repeating_char(word):
    letters = {}
    for letter in word:
        letters[letter] = letters.get(letter, 0) + 1

    for letter in word:
        if letters[letter] == 1:
            return letter

def find_duplicates(numbers):
    seen = {}
    duplicates = []
    for number in numbers:
        if number in seen:
            duplicates.append(number)
            continue
        seen[number] = None
    return duplicates

def main():
    print(first_non_repeating_char('gello'))
    
if __name__ == "__main__":
    main()