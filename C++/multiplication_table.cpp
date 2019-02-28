#import "iostream"
using namespace std;

/*
challenge:
print a multiplication table up to the value of max
*/

void multiplication_table(int max){
	int i,j,hold;
	for(i = 1; i<max; i++){
		for(j=1; j<max;j++){
			hold = i*j;
			cout<<hold;
			cout<<" ";
		}
		cout<<endl;
	}
}

int main(){
	multiplication_table(13);
	return 0;
}