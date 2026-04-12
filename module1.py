# This module will cover component level of question for practising the SOLID Principles. 
# Single Responsibility Principle (SRP)

class UserValidator:
    def is_valid(self, username):
        if len(username)<3:
            raise ValueError("username too short")
        

class UserRepository:
    def __init__(self, db):
        self.db = db

    def addition(self, username):
        self.db.append(username)
    
    def get_user(self, username):
        return username if username in self.db else None

class UserService:
    def __init__(self, repo, validator):
        self.repo = repo
        self.validator = validator

    def register_service(self, username):
        self.validator.is_valid(username)

        if self.repo.get_user(username):
            raise ValueError("username already exist")
        
        else:
            self.repo.addition(username)
            print(f"user data saved for - {username}")
        

if __name__ == "__main__":
    repo = UserRepository(db=[])
    validator = UserValidator()
    # initilize service once bcz if it was passed in loop then it will calling repo and validator multiple times
    # Input data like username should be passed to the service method, not stored in the service itself. 
    # This keeps the service stateless and reusable
    # please remember to work on nameing methods don't use addition , instead use add_user which are industry level
    service = UserService(repo, validator)

    for i in range(3):
        username = input(str("please enter your username : "))
        try:
            service.register_service(username)
        except ValueError as e:
            print(e)

