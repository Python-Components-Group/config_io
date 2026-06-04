class FieldDoesntExistsError(Exception):
	"""
		Represents a (non-exiting) exception that occurs when an operation is
        performed using an incorrect configuration file with one or more
        required fields missing
	"""
	pass
