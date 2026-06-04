from .. import IConfigParser
from .e_parser_ftype import EParserFiletype

from .._private.json_cfgparser import JsonConfigParser



class ConfigParserFactory:
	"""
		Represents a factory for each `IConfigParser`
	"""
	
	
	@classmethod
	def create(
			cls,
			ftype: EParserFiletype
	) -> IConfigParser:
		"""
			Instantiates a new configuration file parser for the specified file type
            
            Parameters
            ----------
                ftype: EParserFiletype
                    An `EParserFiletype` value representing the type of file
					by the requested `IConfigParser` object
            
            Returns
            -------
                IConfigParser
                    An `IConfigParser` object that allows parsing configuration files of the specified file type
		"""
		obj: IConfigParser
		match ftype:
			case EParserFiletype.JSON:
				obj = JsonConfigParser()
			
		return obj
		
		
	##	============================================================
	##						PRIVATE METHODS
	##	============================================================