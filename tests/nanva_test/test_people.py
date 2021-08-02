import logging
import unittest

from nanva.people import People


class TestPeople(unittest.TestCase):
    logger = logging.getLogger(__name__)
    logging.basicConfig(format='%(asctime)s %(module)s %(levelname)s: %(message)s',
                        datefmt='%m/%d/%Y %I:%M:%S %p', level=logging.INFO)

    def test_people(self):
        name = "good_man"
        mail = "good_man@nice.lab"
        p = People(name, mail)
        self.logger.info("sbc", p)
        self.assertEqual(name, p.name, f"People's name should be {name}")


if __name__ == '__main__':
    unittest.main()
