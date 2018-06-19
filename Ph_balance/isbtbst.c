//Check if  a Binary tree is  Binary Search Tree
#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <limits.h>

typedef struct node{
    int data;
    struct node* left;
    struct node* right;
}node;

bool isBSTutil(node *root, int min, int max){
    if(root==NULL){
        return true;                //This is the base case, implies that the tree is empty or ended
    }
    if((root->data>min) && (root->data<max) && isBSTutil(root->left,min,root->data) && isBSTutil(root->right,root->data,max)){
        return true;
    }
    else return false;
}


/*A function that takes a pointer to the root node of the Binary tree and 
returns true on false based upon it being a BST or not.*/
bool isBST(node *root){
   isBSTutil(root,INT_MIN,INT_MAX);         //Range is between -infinity to +infinity
}

//Let us do an inorder traversal of the Binary tree, if it is soreted then it is a BST else not


int main(){
    
    return 0;
}