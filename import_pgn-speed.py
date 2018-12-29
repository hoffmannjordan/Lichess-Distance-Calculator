import chess
import chess.pgn
import numpy
import pandas as pd



def readpgn(file):
	winners = []
	counter = 0
	pgn = open("/Volumes/Fred/lichess/2018-10/"+file)
	while True:
		game = chess.pgn.read_headers(pgn)
		if game == None:
			break
		if counter % 10000 == 0:
			print(counter)
		white = game.get("White")
		black = game.get("Black")
		res = game.get("Result")
		if res =="1-0":
			winners.append([white,black])
		if res =="0-1":
			winners.append([black,white])
		counter += 1
	return winners
		# print 'here'

if __name__=='__main__':
	df = readpgn('lichess_db_standard_rated_2018-10.pgn')
	print('done')
	print ('Now making DF')
	df = pd.DataFrame(df, columns=list('WL'))
	print ('saving')
	df.to_pickle("/Volumes/Fred/lichess/2018-10-ALL.pkl")