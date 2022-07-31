#include <stdio.h>
#define MI_PER_KM 1.609344
#define KM_PER_MI 1/MI_PER_KM
#define FT_PER_MI 5280
#define IN_PER_FT 12

int main(void) {
    double distance, miles, feets, inches;

    printf("Enter distance in kilometers: ");
    scanf("%lf", &distance);

    miles = distance/KM_PER_MI;
    feets = (miles - (int)miles) * FT_PER_MI;
    inches = (feets - (int)feets) * IN_PER_FT;

    printf("%.2lf kilometers equals %d miles, %d feet, and %.2lf inches\n", distance, (int)miles, (int)feets, inches);
}