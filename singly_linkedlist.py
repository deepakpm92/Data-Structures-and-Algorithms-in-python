# -*- coding: utf-8 -*-
"""
Created on Sun Nov 10 19:25:09 2019

@author: d.padmanabhan.menon
"""

class Node:
    def __init__(self):
        self.data = None
        self.next = None
        
    def setData(self,data):
        self.data = data
        
    def getData(self):
        return self.data
    
    def setNext(self, n):
        self.next = n
        
    def getNext(self):
        return self.next
    
    def hasNext(self):
        return self.next != None
    
  
    
class LinkedList():
    def __init__(self):
        self.head = None
        self.length = 0

    def listLength(self):
        current = self.head
        count = 0
        
        while current!= None:
            count = count+1
            current  = current.getNext()
        
        return count  
    
    def insertAtEnd(self,data):
        node = Node()
        node.setData = data
        node.setNext = None
        
        current = self.head()
        
        while current.getNext() != None:
            
            current = current.getNext()
        
        current.setNext(node)
        
    
linked_list =  LinkedList()   
node1 = Node()
node1.setData(2)
node1.setNext(None)
linked_list.head = node1
node2 = Node()
node2.setData(3)
node2.setNext(None)
node1.setNext(node2)
print(linked_list.listLength())




    