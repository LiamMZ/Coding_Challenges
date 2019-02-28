#include <iostream>
#include <fstream>
using namespace std;
/*
Challenge:
sum the values from each line of a file

format of input:
'int
int
int
int....'
*/

int sum_from_file(string filename){
	string line;
	ifstream myfile(filename);
	int val = 0;
  if (myfile.is_open())
  {
    while ( getline (myfile,line) )
    {
    	cout<<line<<endl;
      val = val + stoi(line);
  }
    myfile.close();
  }
  return val;
}

int main(){
	cout<<sum_from_file("numbers.txt");
	return 0;
}