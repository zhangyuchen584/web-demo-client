import argparse
import requests
import json
#import visdom
import numpy as np



def main():
	#vis = visdom.Visdom()
	parser = argparse.ArgumentParser()
	parser.add_argument("--dataset", dest="dataset", type=str, metavar='<str>', default='Laptop', help="Which dataset")
	parser.add_argument("--mode", dest="mode", type=str, metavar='<str>', default='term', help="Term or Aspect")
	parser.add_argument("--rnn_type", dest="rnn_type", type=str, metavar='<str>', default='HOLOGRAPHIC_memNET', help="Recurrent unit type (lstm|gru|simple) (default=lstm)")
	parser.add_argument("--query", dest="query", type=str, metavar='<str>', default='this app is awesome!', help="Query / test case")
	parser.add_argument("--term", dest="term", type=str, metavar='<str>', default='app', help="Aspect Term")
	parser.add_argument("--port", dest="port", type=int, metavar='<int>', default=5000, help="which port?")

	args = parser.parse_args()

	if(args.port==4000):
		title = 'Holo DyMemNN'
	elif(args.port==5000):
		title = "MemNN"
	elif(args.port==3000):
		title = 'Tensor DyMemNN'

	endpoint = "api/v1.0/predict"
	data={'sentence':'the food is really bad','term':'food'}

	r = requests.post("http://10.218.112.25:{}/{}".format(args.port, endpoint), json=data)
	print('Prediction: {}'.format(json.loads(r.text)['prediction']))





if __name__ == '__main__':
	main()
