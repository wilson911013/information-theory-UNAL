#include<bits/stdc++.h>
using namespace std;

class Encoder{
public:
    Encoder(){

    }
};

int main (int argc, char *argv[]){
    FILE* fp = fopen("test.pdf", "r");
    if(!fp) {
        std::perror("File opening failed");
        return EXIT_FAILURE;
    }
 
    int c; // note: int, not char, required to handle EOF
    while ((c = std::fgetc(fp)) != EOF) { // standard C I/O file reading loop
       std::putchar(c);
    }
 
    if (std::ferror(fp))
        std::puts("I/O error when reading");
    else if (std::feof(fp))
        std::puts("End of file reached successfully");
 
    std::fclose(fp);
}