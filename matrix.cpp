// enter a 3x3 matrix and identify highest and lowest elemnt from the matrix

#include<iostream>
using namespace std;


// enter a 3x3 matrix and identify highest and lowest elemnt from the matrix

int main(){
   int i,j,mat[3][3],low,hi;

    for(i=0;i<3;i++){
        for(j=0;j<3;j++){
            cout<<"Enter the value of ["<<i<<"]["<<j<<"]: ";
            cin>>mat[i][j];
        }
    }
    for(i=0;i<3;i++){
        for(j=0;j<3;j++){
            cout<<mat[i][j]<<" ";
        }
        cout<<endl;
    }

}
