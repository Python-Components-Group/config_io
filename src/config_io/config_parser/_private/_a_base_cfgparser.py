from typing import Dict, Any
from abc import abstractmethod
from .. import IConfigParser

# ============ Path Utilities ============ #
from os.path import splitext as path_split_ext
# ======================================== #

from path_validator import PathValidator

from ..exceptions import (
	InvalidConfigFilepathError,
	WrongConfigFileTypeError
)



class _ABaseConfigParser(IConfigParser):
	"""
		Represents a base `IConfigParser`, containing the control logic common to all `IConfigParsers`.
        
        The type of the configuration file being read is specified by the descendants of this abstract class.
        The format of the configuration file being read is specified by the descendants of this abstract class.
	"""
	
	def __init__(self):
		"""
			Creates a new _ABaseConfigReader
		"""
		self._path_val: PathValidator = PathValidator()

	
	def read_config(
			self,
			cfgfile_path: str
	) -> Dict[str, Any]:
		if cfgfile_path is None:
			raise ValueError()
		if cfgfile_path == "":
			raise ValueError()
		
		try:
			self._path_val.assert_path(cfgfile_path)
		except Exception as err:
			raise InvalidConfigFilepathError(err.args[0])
		
		extens: str = self._p__file_extension()
		if extens != "":
			if path_split_ext(cfgfile_path)[1].lower() != f".{extens}":
				raise WrongConfigFileTypeError()
			
		return self._ap__read_spec(cfgfile_path)
	
	
	def _p__file_extension(self) -> str:
		"""
			Returns the required extension for the configuration file.
            Implementing this method is optional if the file type does not require
            a specific extension.
            
            Unless this method is overridden, it returns `""`.
            
            Returns:
            -------
				str
                    A string, in lowercase and without a period, containing the file extension
                    accepted by this `IConfigReader`
		"""
		return ""
	
	
	##	============================================================
	##						ABSTRACT METHODS
	##	============================================================
	
	
	@abstractmethod
	def _ap__read_spec(
			self,
			cfg_path: str
	) -> Dict[str, Any]:
		"""
			Checks the validity of the contents of the associated configuration file against the type specified
			by the descendants of this abstract class, and, if the validation is successful, returns the resulting
			Python dictionary.
            
            The following are guaranteed within this method:
				
				- That the `cfg_path` parameter is not `None`
                - That the `cfg_path` parameter is not an empty string
                - That the file at the `cfg_path` path exists
                - That the `cfg_path` parameter points to a file with the correct extension
			
			Parameters
            ----------
                cfg_path: str
                    A string representing the absolute path containing the configuration file
                    to be associated and read
                    
            Returns
            -------
				Dict[str, Any]
                    A mixed dictionary, indexed by strings, representing the
                    read configuration file.
            
            Raises
            ------
				WrongConfigFileTypeError
                    Occurs if the file’s contents are invalid for the type specified by the subclasses
                    of this abstract class
                    
                WrongConfigFileFormatError
                    Occurs if the configuration file cannot be represented as a Python dictionary
		"""
		pass
	
	
	##	============================================================
	##						PRIVATE METHODS
	##	============================================================