int main() {
	char *args[] = {"hi simp", "-p", 0};
	execvp("/bin/bash", args);
}	
