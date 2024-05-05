from DS.LinkedList import LinkedList
from DS.Stack import Stack
from DS.Queue import Queue

def main():
    my_queue = Queue(0)
    my_queue.enqueue(1)
    print(my_queue)
    my_queue.enqueue(2)
    print(my_queue)
    my_queue.dequeue()
    print(my_queue)

if __name__ == "__main__":
    main()