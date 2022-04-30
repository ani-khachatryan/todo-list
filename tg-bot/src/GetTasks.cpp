#include "fiktivTask.cpp"
#include <iostream>

std::vector <Task> GetTasks() {
    std::vector <Task> tasks;
    /*Task task;
    task.set_description("gei");
    task.date = "4 11 22:47 2022";
    task.set_state(Open);
    tasks.push_back(task);*/
    return tasks;
}

bool is_time(std::tm* date, std::string& task_date) {
    return (std::to_string(date->tm_mon + 1) + ' ' +
            std::to_string(date->tm_mday) + ' ' +
            std::to_string(date->tm_hour) + ':' +
            std::to_string(date->tm_min) + ' ' +
            std::to_string(date->tm_year + 1900)) == task_date;
}