#include "Task.h"

void Task::set_description(std::string text) {
    description = text;
}

void Task::set_state(State state) {
    task_state = state;
}

std::string Task::get_date() {
    return date;
}

std::string Task::get_description() {
    return description;
}

State Task::get_state() {
    return task_state;
}

int Task::get_id() {
    return id;
}
