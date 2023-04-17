awk '{gsub(",","",$1); print "grades[\"" $1 "\"] = ("  $3 "," $4 "," $5")" }' grades.txt 
