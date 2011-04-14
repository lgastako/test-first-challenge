import unittest


class Sheet(object):
	def get(self, key):
		return ""


class PortedTestsPart1(unittest.TestCase):
	def test_that_cells_are_empty_by_default(self):
		sheet = Sheet()
		self.assertEquals("", sheet.get("A1"))
		self.assertEquals("", sheet.get("ZX347"))


if __name__ == '__main__':
	unittest.main()