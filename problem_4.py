## START : GROUP DEFINITION FROM ASSIGNMENT
class Group(object):
    def __init__(self, _name):
        self.name = _name
        self.groups = []
        self.users = []

    def add_group(self, group):
        self.groups.append(group)

    def add_user(self, user):
        self.users.append(user)

    def get_groups(self):
        return self.groups

    def get_users(self):
        return self.users

    def get_name(self):
        return self.name


parent = Group("parent")
child = Group("child")
sub_child = Group("subchild")

sub_child_user = "sub_child_user"
sub_child.add_user(sub_child_user)

child.add_group(sub_child)
parent.add_group(child)
## END : GROUP DEFINITION FROM ASSIGNMENT

## START MY WORK
def is_user_in_group(user: str, group: Group) -> bool:
    """
    Return True if user is in the group, False otherwise.

    Args:
      user(str): user name/id
      group(class:Group): group to check user membership against
    """
    if user in group.get_users():
        return True
    for sub_group in group.get_groups():
        user_exists = is_user_in_group(user, sub_group)
        if user_exists:
            return True
    return False

## END MY WORK

# Testing validity of function
# print(is_user_in_group("a", parent))