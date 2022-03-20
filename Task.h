#include <string>
#include "state.h"

class Task {
	public:
		void set_description(std::string);
		void set_state(state state);
		std::string get_date();
		std::string get_description();
		state get_state();
        int get_id();
	private:
		std::string date;
		std::string description;
		state task_state;
        int id;
};
