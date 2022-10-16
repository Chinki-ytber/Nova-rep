
//Complete the code challenge
//use appropriate main method

#include<iostream>
using namespace std;

class shape{
    public:
    virtual void findvol();
};

class cube : public shape{
    public:
    float volume, side;
    
    void findvol(){
        cout<<"Enter a side: ";
        cin>>side;
        volume = side*side*side;
        cout<<"volume: "<<volume<<endl;
    }
    
};

class sphere : public shape{
    public:
    float volume, radius;
    void findvol(){
        cout<<"Enter a radius: ";
        cin>>radius;
        volume  = (4/3)*3.14*radius*radius*radius;
        cout<<"volume: "<<volume<<endl;


    }

};

int main(){
    shape *ptr;
    ptr = new cube;
    ptr->findvol();
    delete ptr;
    cout<<endl;
    ptr=new sphere();
    ptr->findvol();
    delete ptr;
    return 0;
}
