#include <stdio.h>
#include <stdlib.h>

//Let us create a data type called node_t
typedef struct node{
    int data;           //can be any datatype, we just want to store some value
    struct node *ptr;   //Pointer to another node. Will be NULL for nothing to point
}node_t;

node_t *head;      //head is the pointer to the first node in the linked list

//O(1) insertion, means adding anode at the beginning
void addNode(int x){
    node_t *temp =(node_t*)malloc(sizeof(node_t));
    node_t *tail =(node_t*)malloc(sizeof(node_t));
    temp->data = x;
    temp->ptr = NULL;
    if (head==NULL){head = temp;}
    else{
        tail = head;
        while(tail->ptr!=NULL){
            
            tail = tail->ptr;
        }
        tail->ptr = temp;
    }
    return ;
}

void print(){
    node_t *temp = (node_t*)malloc(sizeof(node_t));
    temp = head;
    printf("The list is");
    while(temp!=NULL){
        
        printf(" %d",temp->data);
        temp=temp->ptr;
    }
   printf("\n");
   
      
}

//----Reverse using recursion:

void recReverse(node_t* node){
    if(node==NULL){
        head=node;
        return ;
    }
    recReverse(node->ptr);
    node_t* q;
    q = (node_t*)malloc(sizeof(node_t));
    q=node->ptr;       //imagine 4 nodes 100,200,150 and 250, rreturns back to 250 and 250 is next of 150, so it is 150->next, q is 250 now
    q->ptr = node;             //instead 250->next is now what p is that is 150;
    node->ptr = NULL;
}

void reverse(){
    printf("\nWe are in reverse");
    if (head==NULL){
        return ;
    }
    node_t *curr;
    node_t *prev;
    node_t *next;
    curr = (node_t*)malloc(sizeof(node_t)); 
    prev = (node_t*)malloc(sizeof(node_t));
    next = (node_t*)malloc(sizeof(node_t));
    curr = head; prev = NULL; next=head;
    while(next!=NULL){
        next = curr->ptr;
        curr->ptr=prev;
        prev = curr;
        curr = next;
    }
    head = prev;
        
}

int main(){
    head = (node_t*)malloc(sizeof(node_t));
    head = NULL;
    printf("How many numbers?");
    int n,i,x;
    scanf("%d",&n);
    for(i=0;i<n;i++){
        scanf("%d",&x);
        addNode(x);
        print();
    }
    node_t* temp = (node_t*)malloc(sizeof(node_t));
    temp=head;
    recReverse(temp);
    //reverse();      //Reverse the linked list
    print();
    //free(temp);
    return 0;
}

/*
How many numbers?4
23
The list is 23
34
The list is 34 23
56
The list is 56 34 23
109
The list is 109 56 34 23*/