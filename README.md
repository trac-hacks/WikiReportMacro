#WikiReportMacro

Wiki macro inserts the Trac report into the wiki page.

    [[WikiReport(<id>,<key1>=<value1>, <keyN>=<valueN>, ...)]]

This macro accepts a comma-separated list of keyed parameters, in the form "key=value" and "id".

* "id" -- then report id of the Trac
* "key" -- then report parameter 
* "value" -- then value of report parameter

It supports dynamic variables.
Example:

    [[WikiReport(1)]]
    [[WikiReport(11,PARENT=0)]]
    [[WikiReport($ID,PARENT=$PARENT)]]
