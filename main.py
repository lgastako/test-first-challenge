class PortedTestsPart1(object):
	def test_that_cells_are_empty_by_default(self):
		sheet = Sheet()
		self.assertEquals("", sheet.get("A1"))
		self.assertEquals("", sheet.get("ZX347"))
