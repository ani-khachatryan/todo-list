#include <string>
#include "State.h"

class Task {
	private:
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
