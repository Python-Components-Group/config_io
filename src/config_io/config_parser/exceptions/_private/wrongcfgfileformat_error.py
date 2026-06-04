class WrongConfigFileFormatError(Exception):
	"""
		Represents a (non-exiting) exception that occurs when an operation
		is performed using a configuration file that cannot be represented
		as a Python dictionary.
	"""
	pass
