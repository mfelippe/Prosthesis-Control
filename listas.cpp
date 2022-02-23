#include <iostream>
#include <list>
#include <stdio.h>

using namespace std;

int main(){
	
	list<int> aula; //criando uma lista do tipo inteiro com 
	int tam;
	list<int>::iterator it;
	
	tam =10;
	
	for(int i=0;i<tam; i++){
		
		//push_back insere no final da lista
		aula.push_front(i);
	}
	tam = aula.size(); // size retorna o tamanho da lista
	
	
	// script para inserir o 0 na posição 5
	it=aula.begin();
	advance(it,5);// avançando 5 posições
	aula.insert(it,0); // colocando o zero na posição 5
	
	
	cout << "tamanho da lista " << aula.size() <<"\n\n";
	
	for(int i=0; i<tam ; i++){
		
		cout << aula.front() << "\n";
		aula.pop_front();
	}
	return 0;
}
