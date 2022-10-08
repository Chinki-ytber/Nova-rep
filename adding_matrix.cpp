/*
QUESTION OF THE DAY!
COMPLETE THE CODE CHALLENGE.

Q) Write a program to take input of two matrix of dimension NxN and MxM and add them if they are of the same dimensions*/



#include <iostream>
using namespace std;

int main(){
    int i,j,m,n,p,q;

    cout<<"enter number of rows for matrix A: ";cin>>m;
    cout<<"enter number of column for matrix A: ";cin>>n;
    int mat1[m][n];

    cout<<"enter number of row for matrix B: ";cin>>p;
    cout<<"enter number of column for matrix B: ";cin>>q;
    int mat2[p][q];
    
        cout<<"Enter element of matrix A: "<<endl;
        for(i=0;i<m;i++){
            for(j=0;j<n;j++){
                cout<<"enter value for ["<<i<<"]["<<j<<"]: ";
                cin>>mat1[i][j];
            }
        }

        cout<<"Enter element of matrix B: "<<endl;
        for(i=0;i<p;i++){
            for(j=0;j<q;j++){
                cout<<"enter value for ["<<i<<"]["<<j<<"]: ";
                cin>>mat2[i][j];
            }
        }
}


// HINTS: you might have to add a loop and addition funtion.
// looking for Basic code.
