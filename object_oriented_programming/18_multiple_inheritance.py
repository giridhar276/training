# 18. Multiple Inheritance
# One child class can inherit from multiple parent classes.

class Father:
    def skills_from_father(self):
        print("Driving")

class Mother:
    def skills_from_mother(self):
        print("Cooking")

class Child(Father, Mother):
    def child_skill(self):
        print("Coding")

c = Child()
c.skills_from_father()
c.skills_from_mother()
c.child_skill()
