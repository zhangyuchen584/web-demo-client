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
	# parser.add_argument("--rnn_type", dest="rnn_type", type=str, metavar='<str>', default='HOLOGRAPHIC_memNET', help="Recurrent unit type (lstm|gru|simple) (default=lstm)")
	# parser.add_argument("--query", dest="query", type=str, metavar='<str>', default='this app is awesome!', help="Query / test case")
	# parser.add_argument("--term", dest="term", type=str, metavar='<str>', default='app', help="Aspect Term")
	parser.add_argument("--port", dest="port", type=int, metavar='<int>', default=5000, help="which port?")

	args = parser.parse_args()

	if(args.port==4000):
		title = 'Holo DyMemNN'
	elif(args.port==5000):
		title = "MemNN"
	elif(args.port==3000):
		title = 'Tensor DyMemNN'

	# endpoint = "api/v1.0/predict"
	# data={'sentence':args.query,'term':args.term}
	data={'sentence':'the food is good','term':'food'}

	# r = requests.post("http://10.218.112.25:{}/{}".format(args.port, endpoint), json=data)
	r = requests.post("http://10.218.112.25:{}/api/v1.0/predict".format(args.port), json=data)
	print('Prediction: {}'.format(json.loads(r.text)['prediction']))
	# print(r.text)


if __name__ == '__main__':
	main()







# from BaseHTTPServer import BaseHTTPRequestHandler
# import urlparse, json
# import cgi
# import logging
# import grpc
# import sentiment_pb2
# import sentiment_pb2_grpc

# logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)


# class GetHandler(BaseHTTPRequestHandler):

#     def do_GET(self):
#         parsed_path = urlparse.urlparse(self.path)
#         message = '\n'
#         self.send_response(200)
#         self.end_headers()
#         self.wfile.write(message)
#         return

#     def do_OPTIONS(self):
#         self.send_response(200, 'OK')
#         # self.send_header('Content-type', 'application/json')
#         self.send_header('Access-Control-Allow-Credentials', 'true')
#         self.send_header('Access-Control-Allow-Origin', 'http://localhost:8080')
#         self.send_header('Access-Control-Allow-Headers', 'X-CSRF-Token, Content-Type')
#         self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS, PUT')

#     def do_POST(self):
#         ctype, pdict = cgi.parse_header(self.headers['content-type'])
#         content_len = int(self.headers.getheader('content-length'))
#         post_body = self.rfile.read(content_len)

#         address = '10.218.112.25'
#         port = '12341'
#         text = post_body
#         # text = get_text(args.input)
#         channel = grpc.insecure_channel('{}:{}'.format(address, port))
#         stub = sentiment_pb2_grpc.SentimentServiceStub(channel)
#         request = sentiment_pb2.SentimentRequest(text=text)
#         response = stub.getAspects(request)
#         sentences = response.sentences

#         '''
#         for i, sentence in enumerate(sentences):
#             text = sentence.text
#             print format(text) #sentence

#             opinions = sentence.opinions #opinion
#             for opinion in opinions:
#                 print ' target: {}' .format(opinion.target)
#                 print ' category: {}' .format(opinion.category)
#                 print ' polarity: {}' .format(opinion.polarity)
#                 print '\n'
#         '''
#         datas = {}
#         sentence_list = []

#         for i, sentence in enumerate(sentences):
#             data = {}
#             data['text'] = sentence.text
#             data['tokenizedText'] = sentence.tokenizedText
#             #print sentence.opinions[0]
#             #print type(sentence.opinions[0])
#             op = []
#             for i, opinion in enumerate(sentence.opinions):
#                 op_dict = {}
#                 op_dict['target'] = opinion.target
#                 op_dict['category'] = opinion.category
#                 op_dict['polarity'] = opinion.polarity
#                 #op_dict['start'] = opinion.start
#                 #op_dict['end'] = opinion.end
#                 op.append(op_dict)
#             data['opinions'] = op
#             sentence_list.append(data)

#         datas['sentences'] = sentence_list
#         print datas
#         json_data = json.dumps(datas)
#         print type(json_data)
#         #json_data = '{"sentences": "test"}'

#         self.send_response(200, 'OK')
#         # self.send_header('Content-type', 'application/json')
#         self.send_header('Access-Control-Allow-Credentials', 'true')
#         self.send_header('Access-Control-Allow-Origin', 'http://localhost:8080')
#         self.send_header('Content-type', 'application/json')
#         self.end_headers()
#         self.wfile.write(json_data)
#         print 

# if __name__ == '__main__':
#     from BaseHTTPServer import HTTPServer
#     #server = HTTPServer(('10.218.112.25', 22), GetHandler)
#     server = HTTPServer(('127.0.0.1', 8080), GetHandler)
#     server.serve_forever()
