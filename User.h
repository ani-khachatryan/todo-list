#include <string>

class User {
private:
	std::string name;
	std::string username;
	std::string telegram;
public:
	void add_task(int task_id);
	void delete_task(int task_id);
	void edit_task(int task_id);	
};
