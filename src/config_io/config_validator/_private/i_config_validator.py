from abc import ABC, abstractmethod



class IConfigValidator(ABC):
	"""
		Represents a validator for configuration files related to a specific purpose,
        represented as a Python dictionary, with any-type values, indexed by strings.
        
        The purpose of the validated configuration file is specified by the descendants of this interface.
	"""
	
	
	@abstractmethod
	def validate_sem(self):
		"""
			Performs semantic validation of the associated Python dictionary representing the configuration file
        
            Raises
            ------
				FieldDoesntExistsError
                    Occurs if the represented configuration file is missing one or more required fields
            
                ConfigExtraFieldsError
                    Occurs if the configuration file contains fields not expected
                    by the scope specified by the descendants of this interface

				InvalidConfigValueError
                    Occurs if:
					
						- The semantics of one or more required fields are incorrect
                        - The semantics of one or more optional fields are incorrect
                        - The semantics of one or more fields are correct but a specific error exists
                          declared by the descendants of this interface
		"""
		pass