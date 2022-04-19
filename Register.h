#include <string>

class Register {
private:
	std::string login;
	std::string password;
	std::string telegram;
public:
	void verify_registration();
};
