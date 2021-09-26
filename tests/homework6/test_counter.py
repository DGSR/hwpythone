from homework6.counter import instances_counter


@instances_counter
class User:
    pass


def test_instances_counter():
    res = User.get_created_instances()
    user, _, _ = User(), User(), User()
    assert res == 0
    assert user.get_created_instances() == 3
    assert user.reset_instances_counter() == 3
