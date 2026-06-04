from typing import Dict, Any
from ._a_base_cfgparser import _ABaseConfigParser

# ============== JSON Utilities ============== #
from json import (
	JSONDecoder, JSONDecodeError
)
# ============================================ #

from ..exceptions import (
	WrongConfigFileTypeError,
	WrongConfigFileFormatError,
)



class JsonConfigParser(_ABaseConfigParser):
	"""
		Represents an `IConfigParser` for JSON configuration files.
        
        Each JSON configuration file read consists, at the root, of a dictionary
        indexed by strings
	"""
	
	def __init__(self):
		"""
			Creates a new JsonConfigParser
		"""
		super().__init__()
		
		self._json_dec: JSONDecoder = JSONDecoder()
	
	
	def _p__file_extension(self) -> str:
		return "json"
	
	
	def _ap__read_spec(self, cfg_path: str) -> Dict[str, Any]:
		json_content: Any
		with open(cfg_path, "r") as fconf:
			try:
				json_content = self._json_dec.decode(fconf.read())
			except JSONDecodeError:
				raise WrongConfigFileTypeError("The provided file is not a valid JSON file")
			
		if not isinstance(json_content, dict):
			raise WrongConfigFileFormatError("The JSON file does not have a dictionary as its root")
		
		return json_content
	
	
	##	============================================================
	##						ABSTRACT METHODS
	##	============================================================
	