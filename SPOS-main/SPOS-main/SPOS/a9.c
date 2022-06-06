#include <stdlib.h>
#include <stdio.h>
#include <unistd.h>
#include <sys/types.h>
#include<sys/wait.h>

int main (int argc, char *argv[]){
	char * ls_args[3]={"ls","-l",NULL};
	pid_t c_pid ,pid;
	int status ,id;
	c_pid =fork();
	
	if (c_pid==0){
	/* CHILD */
	
	id = getpid();
	printf ("Child id is %d \n", id);
	printf ("Child : executing ls\n");
	
	//execute ls
	
	execvp(ls_args[0],ls_args);
	//only get there if exec failed
	perror("exevc failed");
	
	}else if (c_pid>0){
	/*Parent*/
	if((pid=wait(&status))<0) {
	
	perror("wait");
	_exit(1);
	
	
	}
	id=getpid();
	printf("parent id %d\n",id);
	printf("Parent : finished \n");
	
	}else{
	perror("Fork failed");
	_exit(1);
	
	
	}
return 0;	
}


