#include <string>
#include "../../State.h"

class Task {
	public:
		std::string date;
		std::string description;
		State task_state;
        int id;
	public:
		void set_description(std::string);
		void set_state(State state);
		std::string get_date();
		std::string get_description();
		State get_state();
        int get_id();
};

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
