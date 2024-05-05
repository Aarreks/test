# Alex Giang
# Professor Abolghasemi
# CIS 502
# 11 March 2024

# Week 8, Exercise

# This file is intended to demonstrate beginning knowledge in implementing
# a singleton design pattern.

import threading


class Singleton:
    __instance = None

    def __init__(self):
        # Only create the instance if it hasn't been created yet:
        if not Singleton.__instance:
            print("Instance created.")  # essentially, pass. Do not raise an error.
            Singleton.__instance = self
        else:
            # If the user tries to create another instance, raise an error.

            print()
            raise RuntimeError("This class, a singleton, already has an instance.\n"
                               "Please use Singleton.get_instance() to retrieve it.")

    # This method provides a global access point to the Singleton shared instance.
    @staticmethod
    def get_instance():
        # Using threading.Lock to allow only one attempt
        # to modify the shared instance at a time.
        with threading.Lock():
            try:
                # Run the constructor, which will attempt to construct
                # and store a new instance as the shared instance
                # or raise an error
                Singleton()
            except RuntimeError:
                # A second method call to __init__ through get_instance
                # should not have an error printed, but a second
                # call to __init__ should.
                pass
        return Singleton.__instance

    def store_data(self, **kwargs):
        # iterate through all **kwargs to store
        # items in shared instance __dict__
        for key, val in kwargs.items():
            setattr(self, key, val)


def main():
    print("This method will attempt to instantiate Singleton three times.")

    instance_a = Singleton()
    print("Instantiated Singleton without a try block without error.")
    print("Asserting that pointer to constructor return"
          "equals the class shared instance...")
    assert instance_a == Singleton.get_instance()
    print("Assertion passed!")
    try:
        instance_b = Singleton()
    except RuntimeError as e:
        print("Tried to call constructor of Singleton again, "
              "got error message:\n", e)
        print("We yield to message instructions below by using get_instance.")
        instance_b = Singleton.get_instance()
    finally:
        instance_c = Singleton.get_instance()

    print("Printing the id and full __str__ of each of the three pointers:")
    print(id(instance_a), instance_a)
    print(id(instance_b), instance_b)
    print(id(instance_c), instance_c)

    print("Storing data through first pointer...")
    # Change the keyword arguments!
    instance_a.store_data(sleepy=True, giving_up=False)
    print("Retriving data through second and third pointer:")
    print('instance_b.sleepy is', instance_b.sleepy,
          'instance_c.giving_up is', instance_c.giving_up)


if __name__ == "__main__":
    main()
