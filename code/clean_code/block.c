#include <stdio.h>

int main() {
    int foo = 17;
    if (foo == 17) {
        printf("foo is 17\n");
    }
    if (foo == 42)
        printf("foo is 42\n");
        printf("foo is 42\n");  // not in the block
    
    return 0;
}
