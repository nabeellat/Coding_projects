//
//  LinkedList.cpp
//  
//
//  Created by Nabeel Latifi on 10/26/21.
//
#include <stdio.h>
#include<iostream>
using namespace std;

struct Node{
    int n;
    Node *previous;
};
class LinkedList{
private:
    Node *head;
public:
    LinkedList(){
        head = NULL;
    }
    void insert_node(int value){
        Node *new_node = new Node();
        if(new_node != NULL){
            new_node -> n = value;
            new_node -> previous = head;
            head = new_node;
        }
        else{
            head = new_node;
        }

        
    }
    int pop(){
        int r;
        Node *temp = head;
        if(head == NULL){
            return -1;
        }
        r = temp -> n;
        head = head -> previous;
        delete temp;
        return r;
    }
    void show(){
        Node *curr = new Node();
        curr = head;
        while(curr != NULL){
            cout<<"[" <<curr ->n<<"||"<<curr-> previous<<"]"<<endl;
            curr = curr -> previous;
        }
        
    }
};

int main(){
    LinkedList L;
    L.insert_node(1);
    L.insert_node(2);
    L.show();
    cout<<L.pop()<<endl;
    L.show();
    return 0;
}
