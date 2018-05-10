#include<stdio.h>
#include<stdlib.h>

void
secret(){
	printf("%s\n","But this is my secret function");
}

void
input(){
	char buffer[64];
	printf("%s\n","Please enter stuff here! :D");
	gets(buffer);
}

int
main(int argc, char ** argv){
	printf("%x\n",system);
	input();
	return 0;
}
