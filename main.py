from google_play_scraper import app
import pandas as pd

def do_stuff(file_path):
	# Grabbing the file data given the file path
	data = pd.read_excel(file_path)

	'''
	Grabbing the column with all the identifiers

	It is the second column and it doesn't have a column name - so we use the default 'Unnamed: 1'
	'''

	identifiers = data['Unnamed: 1']


	# Creating empty array to store the data
	all_data = []

	errored = []
	err_count = 0

	'''
	Loop through all the identifiers and extract the data
	'''

	for identifier in identifiers:
		try:
			result = app(
			    identifier,
			    lang='en', # defaults to 'en'
			    country='us' # defaults to 'us'
			)

			# Storing data related to identifier in dictionary
			data = {
				"identifier" : identifier,
				"genre" : result['genre'],
				"genreId" : result['genreId']
			}

			# Appending data dictionary to array
			all_data.append(data)
		except Exception as err:
			errored.append({
				"identifier" : identifier
			})
			err_count += 1
			print (f'[ERROR] {identifier} - {err}')


	print (f'[FAILED] {err_count} / {len(identifiers)}')
	# Saving data to file! :D

	pd.DataFrame(all_data).to_csv('./data.csv')
	pd.DataFrame(errored).to_csv('./errored.csv')



do_stuff("./Apps1.xlsx")




# result = app(
#     'com.nianticlabs.pokemongo',
#     lang='en', # defaults to 'en'
#     country='us' # defaults to 'us'
# )
