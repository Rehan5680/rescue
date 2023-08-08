Python 3.11.3 (tags/v3.11.3:f3909b8, Apr  4 2023, 23:49:59) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
class Person:
...     def __init__(self, name):
...         self.name = name
...         self.location = None
...     
...     def move_to(self, location):
...         self.location = location
...         print(f"{self.name} moves to {location}")
... 
... class Jail:
...     def __init__(self):
...         self.is_locked = True
...         self.prisoner = None
...     
...     def lock(self):
...         self.is_locked = True
...         print("Jail is locked")
...     
...     def unlock(self):
...         self.is_locked = False
...         print("Jail is unlocked")
...     
...     def place_prisoner(self, person):
...         self.prisoner = person
...         print(f"{person.name} is now in jail")
...     
...     def free_prisoner(self):
...         self.prisoner = None
...         print("Prisoner is freed")
... 
... # Create characters
... rehan = Person("Rehan")
... farah = Person("Farah")
... 
... # Create jail
... jail = Jail()
... 
... # Initial state
... rehan.move_to("the vicinity of the jail")
... 
... # Rehan breaks into the jail
... jail.unlock()
rehan.move_to("the jail")
jail.place_prisoner(farah)
print(f"{rehan.name} breaks into the jail to rescue {farah.name}")

# Rehan and Farah escape
jail.free_prisoner()
rehan.move_to("safety")
farah.move_to("safety")

# Final state
print(f"{rehan.name} and {farah.name} have successfully escaped!")
