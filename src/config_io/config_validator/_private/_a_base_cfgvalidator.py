from typing import Dict, Set, Tuple, Any
from abc import abstractmethod
from .. import IConfigValidator

from ..exceptions import (
	FieldDoesntExistsError,
	ConfigExtraFieldsError
)



class _ABaseConfigValidator(IConfigValidator):
	"""
		Represents a base `IConfigValidator`, containing the validation logic
		common to all `IConfigValidator`s.
        
        The purpose of the validated configuration file is specified by the descendants of this abstract class.
	"""
	
	def __init__(
			self,
			config_dict: Dict[str, Any]
	):
		"""
			Creates a new _ABaseConfigReader by providing it with the Python configuration
			dictionary that will be associated with this validator
            
            Parameters
            ----------
				config_dict: Dict[str, Any]
                    A any-type value dictionary, indexed by strings, representing the
                    configuration file read
			
			Raises
            ------
                ValueError
                    Occurs if:
                    
                        - The provided dictionary is `None`
                        - The provided dictionary is empty
		"""
		if config_dict is None:
			raise ValueError()
		if len(config_dict) == 0:
			raise ValueError()
		
		self._dict: Dict[str, Any] = config_dict
	
	
	def validate_sem(self):
		config_fields: Set[str] = set(self._dict.keys())
		mand_fields, opt_fields = self._ap__fields()
		
		has_all_mands: bool = (
			len(config_fields.intersection(mand_fields)) == len(mand_fields)
		)
		if not has_all_mands:
			raise FieldDoesntExistsError()
		
		if self._p__efields_strict():
			all_fields: Set[str] = mand_fields.union(opt_fields)
			has_extra_fields: bool = config_fields.difference(all_fields) != set()
			if has_extra_fields:
				raise ConfigExtraFieldsError()
		
		self._ap__assert_mandatory(self._dict)
		self._ap__assert_optional(self._dict)
		self._ap__assert_purperrors(self._dict)
		
		
	def _pf__get_dict(self) -> Dict[str, Any]:
		"""
			Returns the Python configuration dictionary
			
			Returns
			-------
				Dict[str, Any]
					A any-type value dictionary, indexed by strings, representing the
					configuration file read
		"""
		return self._dict
	
	
	def _p__efields_strict(self) -> bool:
		"""
			Indicates whether to deny the extra fields or ignore them.
            This is used, for example, in cases where the configuration file does not have
            fixed fields.
            
            Unless this method is overridden, it returns `True`.
			
			Returns
			-------
				bool
					A boolean indicating whether to check the extra fields
		"""
		return True
	
	
	##	============================================================
	##						ABSTRACT METHODS
	##	============================================================
	
	
	@abstractmethod
	def _ap__fields(self) -> Tuple[Set[str], Set[str]]:
		"""
			Returns the required and optional fields (both at the first level of deepness)
            which, respectively, must and may be included in the configuration file
            that is to be validated
            
            Returns
            -------
				Tuple[Set[str], Set[str]]
                    A tuple of sets of strings representing:
                    
                        - [0]: The set of mandatory field names
                        - [1]: The set of optional field names
		"""
		pass
	
	
	@abstractmethod
	def _ap__assert_mandatory(
			self,
			config_read: Dict[str, Any]
	):
		"""
			Checks the validity of the values in the required fields contained in the configuration file that was provided.
            
            If the validation is successful, this operation should be equivalent to a no-op.
            
            The following is guaranteed within this method:
			
				- That all required fields exist (at the first level of the dictionary)
                - That there are no unwanted fields, if required (at the first level of the dictionary)
            
            Parameters
            ----------
                config_read: Dict[str, Any]
					A mixed dictionary, indexed by strings, representing the read configuration file
			
            Raises
            ------
                InvalidConfigValueError
                    Occurs if the semantics of one or more required fields are incorrect
		"""
		pass
	
	
	@abstractmethod
	def _ap__assert_optional(
			self,
			config_read: Dict[str, Any]
	):
		"""
			Check the validity of the values in the optional fields contained in the configuration file
			that was provided.
            
            If the validation is successful, this operation should be equivalent to a no-op.
			
			The following is guaranteed within this method:
            
                - That all required fields exist and are semantically correct
                - That there are no unwanted fields, if required (at the first level of the dictionary)
                
            Parameters
            ----------
				config_read: Dict[str, Any]
                    A varied dictionary, indexed by strings, representing the read configuration file
                    
        
            Raises
            ------
				ConfigExtraFieldsError
                    Occurs if the configuration file contains fields not expected by the scope
                    specified by the descendants of this abstract class
            
                InvalidConfigValueError
                    Occurs if the semantics of one or more optional fields are incorrect
		"""
		pass
	
	
	@abstractmethod
	def _ap__assert_purperrors(
			self,
			config_read: Dict[str, Any]
	):
		"""
			Check for any errors related to the purpose specified by the subclasses of this abstract class.
            
            If validation is successful, this operation must be equivalent to a no-op.
			
			The following is guaranteed within this method:
            
                - That all required fields exist and are semantically correct
                - That any optional fields that exist are semantically correct

			Parameters
			----------
				config_read: Dict[str, Any]
                    A mixed dictionary, indexed by strings, representing the read configuration file
			
			Raises
            ------
                InvalidConfigValueError
                    Occurs if the semantics of one or more fields are correct but there is
                    a specific error declared by the descendants of this abstract class
		"""
		pass
	
	
	##	============================================================
	##						PRIVATE METHODS
	##	============================================================