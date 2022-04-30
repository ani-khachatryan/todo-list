#include <iostream>
#include <tgbot/tgbot.h>
#include <vector>
#include "GetTasks.cpp"
#include <ctime>

void sendPlannedMassages(TgBot::Bot& bot) {
    std::vector <Task> tasks = GetTasks();
    std::cout << "watching tasks\n";
    for (Task task : tasks) {
        if (task.get_state() != Open) {
            continue;
        }
        std::time_t time = std::time(nullptr);
        std::tm* tm = std::localtime(&time);
        std::string task_date = task.get_date();
        if (is_time(tm, task_date)) {
            bot.getApi().sendMessage(661681731, task.get_description());
        }
    }
    std::cout << "finished watching tasks\n";
}

const std::string TgBotToken = "5287070210:AAG4YLETE_H9NT77fBTOpd5GffsYGXZkcA4";

const TgBot::Bot TgBot(TgBotToken);

int main() {
    /*try {
        printf("Bot username: %s\n", bot.getApi().getMe()->username.c_str());
        TgBot::TgLongPoll longPoll(bot);
        while (true) {
            printf("Long poll started\n");
            sendPlannedMassages(bot);
            longPoll.start();
        }
    } catch (TgBot::TgException& e) {
        printf("error: %s\n", e.what());
    }*/
    return 0;
}