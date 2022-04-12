#include "TaskList.h"
#include <string>

class TasksForToday : public TaskList {
private:
    std::string get_current_date();
public:
    void display() override;
};