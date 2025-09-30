#include <stdio.h>

int main() {
  FILE *fp;

  // -------------------
  // Question 8.2.32
  // -------------------


  fp = fopen("points.dat", "w");
  fprintf(fp, "%d,%d,%d\n", 0, 5, 0); // A
  fprintf(fp, "%d,%d,%d\n", 1, 0, 0); // B
  fprintf(fp, "%d,%d,%d\n", 0, -5, 0); // C
  fprintf(fp, "%d,%d,%d\n", -1, 0, 0); // D
  fclose(fp);
  return 0;
}
