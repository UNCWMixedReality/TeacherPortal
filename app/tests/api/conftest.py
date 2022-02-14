import pytest
from django.contrib.auth.models import User
from organizations.models import Organization
from users.models import CustomUser, Staff


@pytest.fixture(scope="function")
def test_admin():
    password = "bad-password"

    my_admin = User.objects.create_superuser("TestAdmin", "test@test.com", password)

    return my_admin


@pytest.fixture(scope="function")
def test_organizations():
    org_0 = Organization.objects.create(
        name="St. Mark Catholic School", address="Huntersville, NC"
    )
    org_1 = Organization.objects.create(
        name="Christ The King Catcholic High School", address="Concord, NC"
    )

    org_0.save()
    org_1.save()

    return (org_0, org_1)


@pytest.fixture(scope="function")
def create_staff():
    def _create_staff(org):
        test_user = CustomUser(
            name="Steve Wozniak",
            username="SteveWozniak1234",
            email="wozniaks@uncw.edu",
            password="SuperInsecurePassword",
            phone_number="+1234567890",
        )
        staff = Staff.objects.create(user=test_user, organization=org)

        staff.save()
        return staff

    return _create_staff
