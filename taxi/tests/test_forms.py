from django.test import TestCase

from taxi.forms import DriverCreationForm, DriverLicenseUpdateForm


class FormsTests(TestCase):
    def test_driver_creation_form_with_license_number_first_name_last_name_is_valid(self) -> None:
        form_data = {
            "username": "test",
            "password1": "test12test",
            "password2": "test12test",
            "license_number": "AAA45555",
            "first_name": "test",
            "last_name": "cool",
        }
        form = DriverCreationForm(data=form_data)
        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data, form_data)

    def test_driver_license_update_form_license_number_is_valid(self) -> None:
        license_number = "BBB45555"
        form = DriverLicenseUpdateForm(data={"license_number": license_number})
        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data["license_number"], license_number)
