#include "TasksForToday.h"
#include <chrono>
#include <ctime>  

void TasksForToday::display() {
    //diplay tasks with todays date
}

std::string TasksForToday::get_current_date() {
    auto start = std::chrono::system_clock::now();
    std::time_t current_time = std::chrono::system_clock::to_time_t(start);
    return std::ctime(&current_time);
}