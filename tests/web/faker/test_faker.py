class TestFakerFixture:
    """Test Faker Fixture"""

    def test_name_generator(self, faker):
        """Test for generating names using Faker lib"""

        for count in range(10):
            print(faker.name())

    def test_faker_provider_internet(self, faker):
        """Test for generating fake internet addresses using Faker lib"""

        from faker.providers import internet
        faker.add_provider(internet)

        print(faker.ipv4_private())