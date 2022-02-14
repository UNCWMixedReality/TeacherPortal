from cgi import test

import pytest
from users.models import CustomUser, Staff

# Create your tests here.


@pytest.mark.django_db
def test_standard_staff_can_only_create_new_staff_in_their_org(
    test_admin, test_organizations, create_user
):
    # org_0, org_1 = test_organizations
    # admin = test_admin

    # assert len(Staff.objects.filter(organization=org_0)) == 0
    # assert len(Staff.)
    pass


@pytest.mark.django_db
def test_admin_staff_can_create_users_in_any_org():
    pass


@pytest.mark.django_db
def test_admin_staff_create_request_without_org_creates_in_admins_org():
    pass
