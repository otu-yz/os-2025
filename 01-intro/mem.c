#include <unistd.h>
#include <stdio.h>
#include <stdlib.h>

// if runing multiple instances of this program,
// try turning off address space randomization.
// To disable address-space randomization:
// echo 0 | sudo tee /proc/sys/kernel/randomize_va_space
// To enable it again:
// echo 2 | sudo tee /proc/sys/kernel/randomize_va_space
// Randomization is a good defense against certain security weaknesses.

int
main(int argc, char *argv[])
{
  int *p = malloc(sizeof(int));
  printf("(%d) address pointed to by p: %p\n", getpid(), p);
  *p = 0;
  while (1) {
    sleep(1);
    *p = *p + 1;
    printf("(%d) p: %d\n", getpid(), *p);
  }
  return 0;
}
