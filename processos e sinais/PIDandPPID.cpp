#include <stdio.h>
#include <unistd.h>

int main(){
	printf ( "O IDENTIFICADOR DO PROCESSO - PID � : %d \n",(int)getpid() );
	
	//printf(" O IDENTIFICADOR DO PROCESSO PAI - PPID �: %d\n", (int) getppid ());
	
	return 0;
}
