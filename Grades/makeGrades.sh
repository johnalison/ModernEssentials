awk '{gsub(",","",$1); print "grades[\"" $1 "\"] = ("  $3 "," $4 "," $5 "," $6 "," $7 ")" }' grades.txt 
