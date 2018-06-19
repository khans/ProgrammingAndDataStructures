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
    node_t *temp = (node_t*)malloc(sizeof(node_t));
    temp->data = x;
    /*if(head==NULL){         //number of elements is 
        temp->ptr = NULL; 
        head=temp;          //point to this node
    }
    else{
        temp->ptr = head;
        head = temp;
    }*/
    //Simply:
    temp->ptr = head;       //whether head is NUll or empty
    head=temp;
    
  
    //free(temp);
    
   
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

void reverse(){
 
}

void delNode();

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