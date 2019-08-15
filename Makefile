coverage:
	coverage erase
	coverage run -m django test --settings=menus.tests.settings
	coverage report
	coverage xml