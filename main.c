#include <stdio.h>
#include <stdlib.h>
#include <sys/stat.h>

int file_exist (char *filename)
{
  struct stat   buffer;
  return (stat (filename, &buffer) == 0);
}

int main()
{
    if (file_exist ("systm/setup.cfg")) {
        system("python us.py");
    }
    else {
        system("python setup.py");
    }

    return 0;
}
