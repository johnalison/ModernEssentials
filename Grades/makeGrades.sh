
# Midterm only
#awk '/^#/ {next} {gsub(",","",$1); print "grades[\"" $1 "\"] = ("  $3 "," ")" }' grades.txt 

# Midterm 1 + 2
#awk '/^#/ {next} {gsub(",","",$1); print "grades[\"" $1 "\"] = ("  $3 "," $4 ")" }' grades.txt

# Midterm 1 + 2 + 3
awk '/^#/ {next} {gsub(",","",$1); print "grades[\"" $1 "\"] = ("  $3 "," $4 "," $5 "," $6 "," $7 ")" }' grades.txt



# All
#awk '{gsub(",","",$1); print "grades[\"" $1 "\"] = ("  $3 "," $4 "," $5 "," $6 "," $7 ")" }' grades.txt

