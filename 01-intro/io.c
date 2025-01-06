#include <stdio.h>
#include <unistd.h>
#include <fcntl.h>
#include <assert.h>
#include <sys/types.h>
#include <string.h>

int
main (int argc, char *argv[])
{
  int fd = open("/tmp/file", O_WRONLY | O_CREAT | O_TRUNC, S_IRWXU);
  assert(fd > -1);
  char *s = strdup("hello world\n");
  int l = strlen(s);
  //int rc = write(fd, "hello world\n", 13);
  int rc = write(fd, s, l);
  assert(rc == l);
  close(fd);
  return 0;
}
