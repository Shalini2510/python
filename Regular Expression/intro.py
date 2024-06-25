#Regular Expression:  A RegEx, or Regular Expression, is a sequence of characters that forms a search pattern.
                    #RegEx can be used to check if a string contains the specified search pattern.


# import Regex using --> import re

#metacharacters-- characters with a special meaning:
#           []	A set of characters
#           \	Signals a special sequence (can also be used to escape special characters)
#           .	Any character (except newline character)	
#           ^	Starts with	      ex: "^hello"	
#           $	Ends with	  ex: "planet$"	
#           *	Zero or more occurrences	ex: "he.*o"	
#           +	One or more occurrences	   ex:"he.+o"	
#           ?	Zero or one occurrences	     ex:"he.?o"	
#           {}	Exactly the specified number of occurrences	    ex:"he.{2}o"	
#           |	Either or	     ex:"falls|stays"	
#           ()	Capture and group
                
#special sequence

# Character	                              Description	                                                               Example	
#\A	              Returns a match if the specified characters are at the beginning of the string	                   "\AThe"	
#\b	              Returns a match where the specified characters are at the beginning or at the end of a word
#                 (the "r" in the beginning is making sure that the string is being treated as a "raw string")	       r"\bain"

#                                                                                                                      r"ain\b"	

#\B	              Returns a match where the specified characters are present, but NOT at the beginning (or at the end) of a word
#                 (the "r" in the beginning is making sure that the string is being treated as a "raw string")	       r"\Bain"

#                                                                                                                      r"ain\B"	

#\d	              Returns a match where the string contains digits (numbers from 0-9)	                                 "\d"	
#\D	              Returns a match where the string DOES NOT contain digits	                                              "\D"	
#\s	              Returns a match where the string contains a white space character	                                      "\s"