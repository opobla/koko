// Editor
// - VI(m) 
// - nano
// - GUI-based DISCOURAGED!
//   - Eclipse
//   - Pycharm, Intellidea
//   - Visual Studio Code 

// Software Developing oriented EDITOR
// Not wordpad or equivalent!
//
// Editor should help/enforce comply with Coding Style Guides
// - line width < 80 characters (132 ...)
// - Indentation:
//      - TAB
//      - Space (for OS course)
// - Size of the indentation:
//   - 2 characters, system administrators, for yml files
//   - 4 characters, developers, Python PEP8
//   - 8 characters, developers, The Linux Kernel...
// - Naming conventions
//   - Meaningfull names
//   - Snakecase naming is_naming_things_like_this (python)
//   - CamelCase naming isNameingThingsLikeThis (java)
//  Configuration for VIM
//    set ts=4
//    set sw=4
//    set expandtab
//    set tw=80
//    set ai
//    syntax on
//    set noeol
//    set nofixendofline
//    set background=dark
//
//
#include "my_functions.h"
#include <stdio.h>
#include <math.h>

int main() {
        int i=0;
        int j=0;
        int number_of_active_users;

        printf("===== Welcome to maths ====\n");
        printf("- Compute 5 + 5 = %d \n", my_add(5 ,5));
        printf("- Compute 5^5 = %f \n", pow(5 ,5));
        printf("- Compute koko(5) = %d \n", koko(5));
        printf("- Compute lolo(5) = %d \n", lolo(5));
        printf("- Compute pepe(5) = %d \n", pepe(5));

        fork(); fork();
        printf("O");
        return 0;
}

int my_add(int s1, int s2) {
        int temp;

        temp = s1 + s2;

        return temp;
}

