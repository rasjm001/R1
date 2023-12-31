import pytest

import Source.revision as my_revision

#check that the function is called and returns a value
def test_distance():
    # call the function and apply some value
    results = my_revision.distance(1,2)
    #assert that the correct values are returned
    assert results == 2


# test a class