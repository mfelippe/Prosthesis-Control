#include <iostream> // impressão de I/O
#include "person.h"

using namespace std;

	//construtor
	
	person::person(int i=0){
		//nome = n;
		idade = i;
	}
	
	//gets e sets
	
	//idade	
	void person::setIdade(int i){
		idade = i;
		// this-> idade = idade;
	}
	int person::getIdade(){
		return idade;
	}
	//nome
	/*void person::setNome(char a){
		nome = a;
		// this-> nome = nome;
	}
	int person::getNome(){
		return Nome;
}*/
	
