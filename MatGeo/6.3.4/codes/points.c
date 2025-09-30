#include <stdio.h>

int main() {
  FILE *fp;

  // -------------------
  // Question 6.3.4
  // -------------------


  fp = fopen("points.dat", "w");
  fprintf(fp, "%d,%d,%d\n", 1, 2, 1); // A
  fprintf(fp, "%d,%d,%d\n", 2, -1, -1); // B
  fprintf(fp, "%d,%d,%d\n", 1, -1, 1); // m1
  fprintf(fp, "%d,%d,%d\n", 2, 1, 2); // m2
  fprintf(fp, "%f,%f,%f\n", (float)17/6, (float)1/6, (float)17/6); // c1
  fprintf(fp, "%f,%f,%f\n", (float)26/6, (float)1/6, (float)8/6); // c2
  fclose(fp);
  return 0;
}
