awk '{gsub(",","",$1); print "grades[\"" $1 "\"] = ("  $3 ")" }' grades.txt 
