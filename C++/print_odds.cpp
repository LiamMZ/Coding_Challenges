#include <iostream>
using namespace std;
/*
Challenge:
Print all odd numbers up to 99
*/

void print_odds(){
	int i;
	for(i=1;i<100;i+=2){
		cout<<i;
		cout<<" ";

	}
}

int main(){
	print_odds();
	return 0;
}