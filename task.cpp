#include "task.h"

void Task::set_description(std::string text) {
    description = text;
}

void Task::set_state(state state) {
    task_state = state;
}

std::string Task::get_date() {
    return date;
}

std::string Task::get_description() {
    return description;
}
		
state Task::get_state() {
    return task_state;
}