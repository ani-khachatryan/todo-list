#include "TaskList.h"
#include <string>

class TasksForToday : public TaskList {
public:
    void display() override;
private:
    std::string get_current_date();
};