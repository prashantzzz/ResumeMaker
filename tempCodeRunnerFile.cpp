#include <iostream>
using namespace std;
void f(int n){
    if(!n)return;
    cout<<"name "<<n<<endl;
    f(--n);
    cout<<"name "<<n<<endl;
}
int main(){
    f(5);
}