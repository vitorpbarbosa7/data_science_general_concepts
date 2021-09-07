#include <stdio.h>

struct distance_time{
    int total_distance;
    int time_elapsed;
};

int main()
{
    float avarege;
    struct distance_time speed1;
    struct distance_time speed2;
    struct distance_time speed3;

    speed1.time_elapsed = 2;
    speed1.total_distance = 5;
    speed2.time_elapsed =4;
    speed2.total_distance = 20;
    speed3 = 6;
    speed3 = 45;

    avarege = speed1.total_distance / speed1.time_elapsed;
    printf("At time %d seconds avarege speed was %.2f meters per seconds\n", speed1.time_elapsed, avarege);

    avarege = (float) speed2.total_distance / speed2.time_elapsed;
    printf("At time %d seconds avarege speed was %.2f meters per seconds\n", speed2.time_elapsed, avarege);

    avarege = (float) speed3.total_distance / speed3.time_elapsed;
    printf("At time %d seconds avarege speed was %.2f meters per seconds\n", speed3.time_elapsed, avarege);

    return 0;
}
