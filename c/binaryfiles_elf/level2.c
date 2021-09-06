#include <stdio.h>
#include <string.h>

int main (){
	char cmd[100], input[10];
	char *prefix = "zsh -c";
	
	strcpy(cmd, prefix);
	scanf("%3s", input);
	strncpy(cmd + strlen(cmd), input, 3);

	puts(cmd);

	system(cmd);

	return 0;
}
