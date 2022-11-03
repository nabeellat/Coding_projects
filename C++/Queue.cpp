//
//  Queue.cpp
//  
//
//  Created by Nabeel Latifi on 10/27/21.
//

#include <stdio.h>
#include<iostream>
using namespace std;
struct QueueNode{
    int n;
    QueueNode *next;
};
class Queue{
private:
    QueueNode *front;
    QueueNode *rear;
public:
    Queue(){
        front = NULL;
        rear = NULL;
    }
    void push(int value){
        QueueNode *new_node = new QueueNode();
        new_node -> n = value;
        new_node -> next = NULL;
        if(front == NULL){
            front = rear = new_node;
        }
        else{
            rear -> next = new_node;
            rear = new_node;
        }
    }
    void insertAt(int value,int pos){
        QueueNode *curr;
        QueueNode *prev;
        QueueNode *new_node = new QueueNode();
        curr = front;
        int i = 1;
        while(i<pos){
            prev = curr;
            curr = curr -> next;
            i++;
        }
        new_node -> n = value;
        prev -> next = new_node;
        new_node -> next = curr;
    }
    void deleteAt(int pos){
        QueueNode *curr;
        QueueNode *prev;
        int i = 1;
        curr = front;
        
        while(i<pos){
            prev = curr;
            curr = curr -> next;
            i++;
        }
        prev -> next = curr -> next;
        delete curr;
    }
//    void insertAtFront(){
//
//    }
    void show(){
        QueueNode *curr;
        curr = front;
        while(curr != NULL){
            cout<<curr-> n<<endl;
            curr = curr -> next;
        }
        cout<<endl;
    }
    int front_node(){
        int r;
        QueueNode *curr = front;
        if(front != NULL){
            r = curr -> n;
        }else{
            return -1;
        }
        return r;
    }
    int rear_node(){
        int r;
        QueueNode *curr = rear;
        if(rear != NULL){
            r = curr->n;
        }
        else{
            return -1;
        }
        return r;
    }
    int size(){
        int cnt;
        QueueNode *curr = front;
        if(front == NULL){
            return -1;
        }
        cnt = 1;
        while(curr-> next != NULL){
            cnt++;
            curr = curr-> next;
        }
        return cnt;
    }
    bool empty(){
        QueueNode *curr = front;
        if((front == NULL) and (rear == NULL)){
            return 1;
        }
        else{
            return 0;
        }
    }
    int pop(){
        int r;
        QueueNode *curr = front;
        if(front == NULL){
            return -1;
        }
        r = curr->n;
        front = front -> next;
        delete curr;
        return r;
        
    }
    
    
    
};
int main(){
    Queue s;
    s.push(1);
    s.push(2);
    s.push(3);
    s.push(4);
    s.push(5);
    s.show();
    s.insertAt(20,3);
    cout<<endl;
    s.show();
    
    cout<<endl;
    s.deleteAt(3);
    s.show();
    
    return 0;
}
