//
//  project3.cpp
//  
//
//  Created by Nabeel Latifi on 11/6/21.
//Tree with 4 childerent data struct 

#include <stdio.h>
#include<vector>
#include<iostream>
#include<string>
using namespace std;
struct Node{
    string data;
    Node *a;
    Node *b;
    Node *c;
    Node *d;
};
class QuartTree{
private:
    Node *root;
    int count_char_h(Node*,char);
    void insert_h(string, Node*);
    void traverse_h(Node*);
    bool is_tree_full_h(Node *curr);
    vector<int> traverse_h1(Node*);
    int leaf_count_h(Node*);
    string longest_word_h(Node*);

    
public:
    int count_char_x(char);
    void insert(string);
    void construct_tree(vector<string>);
    void traverse_abcdw();
    int leaf_count();
    int count_degree_n_nodes(int);
    string longest_word();
    bool is_tree_full();
    QuartTree(){
        root = NULL;
        
    }
};
bool QuartTree :: is_tree_full_h(Node *curr){
    static int degree_count = 0;
    if(curr != NULL){
        if((curr -> a == NULL) or  (curr -> b == NULL) or (curr -> c == NULL) or (curr -> d == NULL)){
            return false;
        }
        is_tree_full_h(curr -> a);
        is_tree_full_h(curr -> b);
        is_tree_full_h(curr -> c);
        is_tree_full_h(curr -> d);
    }
    return true;
}
bool QuartTree :: is_tree_full(){
    return is_tree_full_h(root);
}
string QuartTree:: longest_word_h(Node *curr){
    static string word;
    static int maxlen = 0;
    if(curr != NULL){
        if(curr -> data.size() >= maxlen){
            maxlen = curr -> data.size();
            word = curr -> data;
        }
        longest_word_h(curr -> a);
        longest_word_h(curr -> b);
        longest_word_h(curr -> c);
        longest_word_h(curr -> d);
    }
    return word;
}
int QuartTree:: count_char_h(Node *curr,char x){
    static int cntChar = 0;
    if(curr != NULL){
        for(int i = 0;i<= curr -> data.size();i++){
            if(x == curr->data[i]){
                cntChar+=1;
            }
            
        }
        count_char_h(curr -> a,x);
        count_char_h(curr -> b,x);
        count_char_h(curr -> c,x);
        count_char_h(curr -> d,x);
    }
    return cntChar;
}
int QuartTree:: count_char_x(char x){
    return count_char_h(root,x);
}
string QuartTree :: longest_word(){
   return longest_word_h(root);
}
void QuartTree::insert_h(string in, Node *leaf){
    if(in.size() == leaf-> data.size()){
        if(leaf -> a != NULL){
            insert_h(in,leaf -> a);
        }
        else{
            leaf -> a = new Node;
            leaf -> a -> data = in;
            leaf -> a -> a = NULL;
            leaf -> a -> b = NULL;
            leaf -> a -> c = NULL;
            leaf -> a -> d = NULL;
        }
    }
    else if((in.size() - leaf -> data.size()) == 1){
        if(leaf-> b != NULL){
            insert_h(in, leaf ->b);
        }else{
            leaf -> b = new Node;
            leaf -> b -> data = in;
            leaf -> b -> a = NULL;
            leaf -> b -> b = NULL;
            leaf -> b -> c = NULL;
            leaf -> b -> d = NULL;
        }
        
    }
    else if((in.size() - leaf -> data.size()) == 2){
        if(leaf -> c != NULL){
            insert_h(in, leaf -> c);
        }else{
            leaf -> c = new Node;
            leaf -> c -> data = in;
            leaf -> c -> a = NULL;
            leaf -> c -> b = NULL;
            leaf -> c -> c = NULL;
            leaf -> c -> d = NULL;
        }
        
    }
    else if((in.size() - leaf -> data.size()) == 3){
        if(leaf -> d != NULL){
            insert_h(in, leaf -> d);
        }
        else{
            leaf -> d = new Node;
            leaf -> d -> data = in;
            leaf -> d -> a = NULL;
            leaf -> d -> b = NULL;
            leaf -> d -> c = NULL;
            leaf -> d -> d = NULL;
        }
    }

}
void QuartTree:: insert(string in){
    if(root!= NULL){
        insert_h(in, root);
    }else{
        root = new Node;
        root -> data = in;
        root -> a = NULL;
        root -> b = NULL;
        root -> c = NULL;
        root -> d = NULL;
    }
    
}
void QuartTree :: construct_tree(vector <string> v){
    for(int i = 0;i<v.size(); i++){
        insert(v[i]);
    }
}
void QuartTree:: traverse_abcdw(){
    traverse_h(root);
}
void QuartTree:: traverse_h(Node *curr){
    if(curr!=NULL){
        traverse_h(curr -> a);
        traverse_h(curr -> b);
        traverse_h(curr -> c);
        traverse_h(curr -> d);
        cout<<curr -> data<< ",";
    }
}
int QuartTree:: leaf_count(){
    return leaf_count_h(root);
}
int QuartTree:: leaf_count_h(Node *curr){
    static int cnt = 0;
    if(curr != NULL){
        if((curr-> a == NULL) and (curr-> b == NULL) and (curr-> c == NULL) and (curr-> d == NULL)){
            cnt+=1;
        }
        leaf_count_h(curr -> a);
        leaf_count_h(curr -> b);
        leaf_count_h(curr -> c);
        leaf_count_h(curr -> d);
    }
    return cnt;
}
int QuartTree:: count_degree_n_nodes(int n){
    vector<int> count = traverse_h1(root);
    return count[n];
}
vector<int> QuartTree::traverse_h1(Node *curr){
    static int n0=0;
    static int n1=0;
    static int n2=0;
    static int n3=0;
    static int n4=0;
    if(curr != NULL){
        if((curr ->a != NULL) and (curr -> b != NULL) and (curr -> c != NULL) and (curr -> d != NULL)){
            n4+=1;
        }
    
        else if((curr->a != NULL) and (curr->b != NULL) and (curr->c != NULL) and (curr->d == NULL)){
            n3+=1;
        }
        else if((curr -> a != NULL) and (curr -> b != NULL) and (curr ->c == NULL) and (curr -> d == NULL)){
            n2 +=1;
        }
        else if((curr -> a != NULL) and (curr -> b == NULL) and (curr -> c == NULL) and (curr-> d == NULL)){
            n1+=1;
     
        }
        else if((curr -> a == NULL) and (curr -> b == NULL) and (curr -> c == NULL) and (curr-> d == NULL)){
            n0+=1;
        }
        traverse_h1(curr -> a);
        traverse_h1(curr -> b);
        traverse_h1(curr -> c);
        traverse_h1(curr -> d);

    }
    vector<int> v = {n0,n1,n2,n3,n4};
    return v;
}

int main(){
//    {"with", "it", "hi", "can", "word", "are", "in", "day","yes", "no", "week", "this", "a", "way", "fun", "that", "it", "are"};
    vector<string> v = {"with", "with","withs","withss","withsss"};
    QuartTree T;
    T.construct_tree(v);
    T.traverse_abcdw();
    cout<<endl;
    cout << T.leaf_count() << endl;
    cout << T.count_degree_n_nodes(1) << endl;
    cout<<endl;
    cout << T.is_tree_full() << endl;
    cout<<endl;
    cout << T.count_char_x('a') << endl;
    cout << T.longest_word() << endl;
    return 0;
}

//g++ -std=c++11 -o project3.out project3.cpp
//if getting errors while running this please use this line to compile the program.

