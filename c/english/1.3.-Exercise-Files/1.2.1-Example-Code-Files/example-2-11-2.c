#include <stdio.h>

struct distance_time{
    int total_distance;
    int time_elapsed;
};

void init_avg_speed(struct distance_time *speed, int time, int distance);
void calc_avg_speed(struct distance_time speed);

int main()
{
    struct distance_time speed1;
    struct distance_time speed2;
    struct distance_time speed3;

    init_avg_speed(&speed1, 2, 5);
    init_avg_speed(&speed2, 4, 20);
    init_avg_speed(&speed3, 6, 45);

    calc_avg_speed(speed1);
    calc_avg_speed(speed2);
    calc_avg_speed(speed3);

    return 0;
}

void init_avg_speed(struct distance_time *speed, int time, int distance)
{
    speed->time_elapsed = time;
    speed->total_distance = distance;
    printf("time elepsed %d sec  total_distance %d meters\n", speed->time_elapsed, speed->total_distance);
}

void calc_avg_speed(struct distance_time speed)
{
    float avarege = (float) speed.total_distance / speed.time_elapsed;
    printf("At time %d seconds avarege speed was %.2f meters per seconds\n", speed.time_elapsed, avarege);
}
