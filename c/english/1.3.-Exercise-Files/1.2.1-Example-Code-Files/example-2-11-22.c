#include <stdio.h>

struct avg_speed{
    int total_distance;
    int time_elapsed;
};

void calc_avg_speed(struct avg_speed speed);

int main()
{
    struct avg_speed speed1;
    struct avg_speed speed2;
    struct avg_speed speed3;

    speed1.time_elapsed = 2;
    speed1.total_distance = 5;
    speed2.time_elapsed =4;
    speed2.total_distance = 20;
    speed3.time_elapsed = 6;
    speed3.total_distance = 45;

    calc_avg_speed(speed1);
    calc_avg_speed(speed2);
    calc_avg_speed(speed3);

    return 0;
}

void calc_avg_speed(struct avg_speed speed)
{
    float avarege = (float) speed.total_distance / speed.time_elapsed;
    printf("At time %d seconds avarege speed was %.2f meters per seconds\n", speed.time_elapsed, avarege);
}
