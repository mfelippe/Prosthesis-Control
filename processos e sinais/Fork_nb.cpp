#include <stdio.h>
#include <sys/types.h>
#include <unistd.h>

int main(){
	
	pid_t child_pid;
	printf(" O PROGRAMA PRINCIPAL TEM O ID : %d\n",(int) getpid()); // pegando o pid do processo original
	child_pid = fork(); // fazendo um copia do programa em execução
	
	if (child_pid !=0){
		printf("O processo pai tem o id %d\n", (int) getpid()); // mostra o id do processo pai
		printf("O processo filho tem o id %d\n", (int) child_pid); // mostra o id do processo filho
		}else{
			printf("esse é o processo filho e tem o id %d \n", (int) getpid()); // se voce estiver no processo filho só esse id irá aparecer
		}
}	 return 0;

