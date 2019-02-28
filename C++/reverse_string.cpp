#include <iostream>
using namespace std;

/*
Challenge:
create a function to reverse an inputted string

*/

string reverse_string(string str){
	int length = str.length();
	string ret;
	for(int i = length; i>=0; i--){
		ret = ret + str[i];
	}
	return ret;
}

int main(){
	std::cout<<reverse_string("Hello paul");
	return 0;

}