class InvalidConfigValueError(Exception):
	"""
		Represents an exception (non-exiting) that occurs when
		a value is read from the configuration file that is
		invalid for reasons specified by the raiser of this
		exception
	"""
	pass