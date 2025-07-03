class User:
    #first name, last name, username, avator_url, profile_info
    def __init__(self, first_name, last_name, username, avatar_url,
                 profile_info):
        self.first_name = first_name
        self.last_name = last_name
        self.avatar_url = avatar_url
        self.username = username
        self.profile_info = profile_info
        self.access = ["Can view profiles", "Update own profile"]

    def get_user_information(self):
        print(f"Username: {self.username}")
        print(f"Name: {self.first_name} {self.last_name}")
        print(f"Information: {self.avatar_url} \n {self.profile_info}")

    def check_access(self, access):
        return self.access.count(access) > 0

new_user = User("Joe", "Smith", "Jsmith01", "www.avatars.com/joesmith",
                "Secretary to president Millard Fillmore")

print(new_user.check_access("Can view profiles"))

class Admin(User):
    def __init__(self, first_name, last_name, username, avatar_url,
                 profile_info):
        super().__init__(first_name, last_name, username, avatar_url,
                         profile_info)
        self.access = ["Can edit Users"]


new_admin = Admin("Joe", "Jones", "JJones02", "www.avatars.com/joesmith",
                "Friend to president Millard Fillmore")

print(new_admin.access)