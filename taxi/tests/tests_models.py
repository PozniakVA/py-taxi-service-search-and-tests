from django.test import TestCase

from taxi.models import Manufacturer, Driver, Car


class ModelTests(TestCase):
    def test_manufacturer_str(self) -> None:
        name = "BMW"
        country = "Germany"
        manufacturer = Manufacturer.objects.create(name=name, country=country)
        self.assertEqual(str(manufacturer), f"{name} {country}")

    def test_driver_str(self) -> None:
        driver = Driver.objects.create(
            username="ErenJaeger",
            first_name="Eren",
            last_name="Jaeger",
        )
        self.assertEqual(str(driver), f"{driver.username} ({driver.first_name} {driver.last_name})")

    def test_car_str(self) -> None:
        model = "BMW x4"
        manufacturer = Manufacturer.objects.create(name="BMW", country="Germany")
        car = Car.objects.create(
            model=model,
            manufacturer=manufacturer,
        )
        self.assertEqual(str(car), model)
