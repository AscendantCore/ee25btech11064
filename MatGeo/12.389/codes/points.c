#include <stdio.h>

int main() {
  FILE *fp;

  // -------------------
  // Question 12.389
  // -------------------


  fp = fopen("points.dat", "w");
  fprintf(fp, "%d,%d,%d,%d\n", 1, 2, 1, 4); // 1
  fprintf(fp, "%d,%d,%d,%d\n", 2, 1, 2, 5); // 2
  fprintf(fp, "%d,%d,%d,%d\n", 1, -1, 1, 1); // 3
  fclose(fp);
  return 0;
}
