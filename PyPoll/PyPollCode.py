import os
import csv

createfilepath =  os.path.join('analysis', 'PyPollAnalysis.txt')
election_data_csv = os.path.join("Resources", "election_data.csv")
with open(election_data_csv, newline='') as csv_file:

	reader = csv.reader(csv_file)
	next(reader)

	vote_count = 0
	canidates = {}

	#makes dictionary keys from column 3.
	#counts votes for each key.
	for row in reader:
		vote_count += 1
		if row[2] in canidates.keys():
			canidates[row[2]] = canidates[row[2]] + 1
		else:
			canidates[row[2]] = 1

	#puts keys and values into lists
	canidate = []
	canidate_votes = []
	for key, value in canidates.items():
		canidate.append(key)
		canidate_votes.append(value)

	#finds vote percentage
	vote_percent = []
	for i in canidate_votes:
		vote_percent.append(round(i/vote_count*100, 3))

	#Merges lists into tuples
	canidate_summary = list(zip(canidate, canidate_votes, vote_percent))


	#finds highest count of votes to find winner
	winner = max(canidates, key=canidates.get)

	print("Election Results")
	print("------------------------")
	print(f"Total Votes:", vote_count)
	print("------------------------")

	for data in canidate_summary:
		print(data[0] + ": " + str(data[2]) + '%  (' + str(data[1]) + ')\n')
 

	print("------------------------")
	print("Winner:", winner)
	print("------------------------")

	with open(createfilepath, "w") as f:
		f.write("Election Results\n")
		f.write("------------------------\n")
		f.write(f"Total Votes:")
		f.write(str(vote_count))
		f.write("\n")
		f.write("------------------------\n")

		for data in canidate_summary:
			f.write(data[0] + ": " + str(data[2]) + '%  (' + str(data[1]) + ')\n')
 

		f.write("------------------------\n")
		f.write("Winner:")
		f.write(str(winner))
		f.write("\n")
		f.write("------------------------\n")