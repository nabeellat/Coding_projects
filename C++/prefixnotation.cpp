//
//  prefixnotation.cpp
//  
//
//  Created by Nabeel Latifi on 10/28/21.
//

#include <stdio.h>
#include<iostream>
#include<stack>
#include<string>
using namespace std;
int prefixeval(string x){
    stack<int> s;
    
}
        
int postfixeval(string x){
    stack<int> s;
    char ch;
    for(int i = 0; i<x.length();i++){
        if(isdigit(x[i])){
            s.push((int)x[i] - 48);
    }

    else{
        int x = s.top();
        s.pop();
        int y = s.top();
        s.pop();
        switch(ch){
            case '+':
                s.push(x+y);
                break;
            case '*':
                s.push(x*y);
                break;
            case '/':
                s.push(y/x);
                break;
            case '-':
                s.push(x-y);
                break;
        }
        }
    }
    int last = s.top();
    s.pop();
    return last;
}
int main(){

            string s = "+9*26";
            cout<<prefixeval(s);
    
}
