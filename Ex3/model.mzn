int: N_slot;
int: min_time;
int: max_time;
int: max_duration_meeting;

int: duration_meeting;
set of int: SLOTS=1..N_slot;
set of int: DURATION = 0..max_duration_meeting;
set of int: TIME = min_time..max_time;
array[SLOTS] of TIME: array_meeting;
array[SLOTS] of DURATION: array_duration;
var TIME: time_meeting;

include "disjunctive.mzn";
constraint disjunctive(array_meeting++[time_meeting], array_duration++[duration_meeting]);
solve satisfy;


