#ifndef _PROCESS_
#define _PROCESS_

#include <stdio.h>
#include <stdlib.h>

typedef struct{
int id;
int at;
int ct;
int wt;
int tat;
int burst;
int rt;
int priority;
}Process;

void process_init(Process *p, int len){

    for(int i=0; i<len; i++){
        p[i].wt = 0;
        p[i].ct = 0;
        p[i].rt = 0;
    }
}

#endif