from typing import Dict, Any
from abc import ABC, abstractmethod



class IConfigParser(ABC):
	"""
		Represents a parser for configuration files written in a specific type and format.
        The category of configuration files that can be read by any IConfigParser consists of configuration files
        that can be represented conceptually as a dictionary indexed by strings.
		
		The type of the configuration file being read is specified by the descendants of this interface.
	"""


	@abstractmethod
	def read_config(self, cfgfile_path: str) -> Dict[str, Any]:
		"""
			Parses the configuration file at the specified path, checking:
                
                - Whether the file extension matches the one required for the type
                - Whether the content is valid for the type specified by the descendants of this interface
                - Whether the configuration file can be represented as a Python dictionary
				
			It then reads the configuration file and returns it as a Python dictionary
            of any-type values
            
            Parameters
            ----------
                cfgfile_path: str
					A string containing the path to the configuration file to be parsed
                    .
            
            Returns
            -------
                Dict[str, Any]
                    A mixed dictionary, indexed by strings, representing the
                    read configuration file.
					
			Raises:
            ------
                ValueError
                    Occurs if:
                    
                        - The provided configuration file path is `None`
                        - The provided configuration file path is an empty string
						
				InvalidConfigFilepathError
                    Occurs if:
                    
                        - The provided configuration file path is syntactically invalid
                        - No file exists at the provided path
                        - The configuration file cannot be opened
			
				WrongConfigFileTypeError
                    Occurs if:
                        
                        - The associated configuration file is not of the type specified by the
                          descendants of this interface (extension)
						- The file's content is invalid for the type specified by the descendants of this interface
  
  
		        WrongConfigFileFormatError
		            Occurs if the configuration file cannot be represented as a Python dictionary
		"""
		pass