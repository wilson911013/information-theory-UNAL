#include<bits/stdc++.h>
using namespace std;

int main(){
	double a = 0;
	for(int i = 0 ; i < 10000 ; i++)
		a += sin(i);
	cout<<a<<endl;
}