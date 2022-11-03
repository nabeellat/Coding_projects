//
//  stack.cpp
//  
//
//  Created by Nabeel Latifi on 10/27/21.
//stack object

#include <stdio.h>
#include<iostream>
using namespace std;
struct StackNode{
    int n;
    StackNode *previous;
};
class stack{
private:
    StackNode *top;
public:
    stack(){
        top = NULL;
    }
    void push(int value){
        StackNode *new_node = new StackNode();
        new_node -> n = value;
        new_node -> previous = top;
        top = new_node;
        
    }
    void show(){
        StackNode *curr = top;
        while(curr != NULL){
            cout<<curr -> n << "||"<<curr->previous<<endl;
            curr = curr -> previous;
        }
        
    }
    int count(){
        int cnt;
        StackNode *curr;
        curr = top;
        if(top == NULL){
            return 0;
        }
        else{
            cnt = 1;
        }
        while(curr-> previous != NULL){
            curr = curr -> previous;
            cnt++;
        }
        return cnt;
    }
    int pop(){
        int r;
        StackNode *curr;//cant ha
        curr = top;
        if(top == NULL){
            return -1;
        }
        r = curr -> n;
        top = top -> previous;
        delete curr;
        return r;
    }
    void insertAt(int value,int pos){
        StackNode *curr;
        StackNode *prev;
        StackNode *new_node = new StackNode();
        curr = top;
        int i = 1;
        while(i<pos){
            prev = curr;
            curr = curr -> previous;
            i++;
        }
        new_node -> n = value;
        
        prev -> previous = new_node;
        new_node-> previous = curr;
        
    }
    void deleteAt(int pos){
        StackNode *curr;
        StackNode *prev;
        curr = top;
        int i = 1;
        while(i<pos){
            prev = curr;
            curr = curr -> previous;
            i++;
        }
        prev -> previous = curr -> previous;
        delete curr;
    }
};
int main(){
    stack s;
    s.push(1);
    s.push(2);
    s.push(8);
    s.show();
//    cout<<s.pop()<<endl;
//    cout<<endl;
//    cout<<s.count()<<endl;
    s.insertAt(4,2);
    s.deleteAt(2);
    s.show();
    return 0;
}
