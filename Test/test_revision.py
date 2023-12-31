import pytest

import Source.revision as my_revision

#check that the function is called and returns a value
def test_distance():
    # call the function and apply some value
    results = my_revision.distance(1,2)
    #assert that the correct values are returned
    assert results == 2


# test a class

class TestPerson:
    def setup_method(self, method):

        # use this to be able to tell what the linked method is: {method}
        print(f"settting up method, {method}")
        #the parameters are set of the person class- this is then used for all testing ( eg all tests must show that person is called james, 30 and male
        self.Person = my_revision.Person("James", 21, "Male")





    def teardown_method(self, method):
        print(f"tearing down method, {method}")

    def test_one(self):
        # the method that requires testing is selecte- and the return value is tested against the previous set up values
        assert self.Person.method1() == ('My name is ', 'James', ' I am ', 21, ' and a ', 'Male')


    def test_two(self):
        assert True

class TestMe:
    def test_three():
        assert True

