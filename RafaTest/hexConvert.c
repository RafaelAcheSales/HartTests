#include <string.h>
#include <stdio.h>
char *hex = "ffffffffff0280000082";

int main(int argc, char const *argv[])
{
    int len = strlen(hex);
    for (int i = 0; i < len; i +=2)
    {
        printf("\\x%c%c", hex[i], hex[i+1]);
    }
    
    return 0;
}
