#include <stdio.h>

struct avg_speed{
    int total_distance;
    int time_elapsed;
};

void init_avg_speed(struct avg_speed *speed, int time, int distance);
void calc_avg_speed(struct avg_speed speed);

int main()
{
    struct avg_speed speed1;
    struct avg_speed speed2;
    struct avg_speed speed3;

    init_avg_speed(&speed1, 2, 5);
    init_avg_speed(&speed2, 4, 20);
    init_avg_speed(&speed3, 6, 45);

    calc_avg_speed(speed1);
    calc_avg_speed(speed2);
    calc_avg_speed(speed3);

    return 0;
}

void init_avg_speed(struct avg_speed *speed, int time, int distance)
{
    speed->time_elapsed = time;
    speed->total_distance = distance;
    printf("time elepsed %d sec  total_distance %d meters\n", speed->time_elapsed, speed->total_distance);
}

void calc_avg_speed(struct avg_speed speed)
{
    float avarege = (float) speed.total_distance / speed.time_elapsed;
    printf("At time %d seconds avarege speed was %.2f meters per seconds\n", speed.time_elapsed, avarege);
}
