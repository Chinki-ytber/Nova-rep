// enter a 3x3 matrix and identify highest and lowest element from the matrix

#include<iostream>
using namespace std;

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
   
    low=hi=mat[0][0];
     for(i=0;i<3;i++){
         for(j=0;j<3;j++){
             if(mat[i][j]>hi){
                 hi=mat[i][j];
             }
             else{
                 if(mat[i][j]<low){
                     low=mat[i][j];

                }
            }
         }

        
     }


 cout<<"highest: "<<hi<<" Lowest: "<<low<<endl;

}
