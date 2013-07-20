# Additional manual #
----
svnchecker-fork add some new checkers and some new directive. This manual tells you how to use them.

## New checker: checklog ##
This checker is used to check the commit log style. Here's the example of svnchecker.ini:

	[example-checklog]
	checklog.mode=Keyword
	checklog.KeywordFile=C:\Your Path\Keyword1.txt
	checklog.FailureHandlers=Console

+ `checklog.mode` tells the checklog engine how to check the log. Currently it accepts only one value:`Keyword`
+ `checklog.KeywordFile` tells the checklog engine the full path of the keyword file. 

Here's an example of the keyword file:

	fix bug=^([Ff][Ii][Xx] #[0-9].*)|([Rr][Ee][Ff] #[0-9].*)

The example keyword file tells the checklog engine:

+ If the commit log contains phrase `fix bug`, checklog will use the regular expression `fix bug=^([Ff][Ii][Xx] #[0-9].*)|([Rr][Ee][Ff] #[0-9].*)` to verify the log content. If the log message doesn't match the regular expression, the checker will get failed.