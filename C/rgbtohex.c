//Format an RGB value (three 1-byte numbers) as a 6-digit hexadecimal string.
#include <stdio.h>
int main(){
    int r,g,b;
    scanf("%d,%d,%d",&r,&g,&b);
    printf("%02x%02x%02x",r,g,b);
    return 0;
}

/**
 * def format_rgb(red, green, blue):
...."""Convert integer RGB to hex RGB string
....
....>>> format_rgb(0, 0, 0)
....'000000'
....>>> format_rgb(255, 0, 0)
....'FF0000'
....>>> format_rgb(0, 255, 0)
....'00FF00'
....>>> format_rgb(0, 0, 255)
....'0000FF'
....>>> format_rgb(255, 255, 255)
....'FFFFFF'
...."""
....return "%02X%02X%02X" % (red, green, blue)
Test solutions:

def _test():
...."""Run tests on functions in module """
....import doctest
....doctest.testmod()
*/