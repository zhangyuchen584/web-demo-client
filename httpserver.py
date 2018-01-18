from BaseHTTPServer import BaseHTTPRequestHandler
import urlparse, json
import cgi
import logging
import grpc
import sentiment_pb2
import sentiment_pb2_grpc


##

import argparse
import requests
import json
#import visdom
import numpy as np

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)


class GetHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        parsed_path = urlparse.urlparse(self.path)
        message = '\n'
        self.send_response(200)
        self.end_headers()
        self.wfile.write(message)
        return

    def do_OPTIONS(self):
        self.send_response(200, 'OK')
        # self.send_header('Content-type', 'application/json')
        self.send_header('Access-Control-Allow-Credentials', 'true')
        self.send_header('Access-Control-Allow-Origin', 'http://localhost:8080')
        self.send_header('Access-Control-Allow-Headers', 'X-CSRF-Token, Content-Type')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS, PUT')

    def do_POST(self):
        ctype, pdict = cgi.parse_header(self.headers['content-type'])
        content_len = int(self.headers.getheader('content-length'))
        post_body = self.rfile.read(content_len)

        # address = '10.218.112.25'
        # port = '12341'

        address = '10.217.129.136'
        port = '12345'


        # ZQ
        text = post_body
        # text = get_text(args.input)
        channel = grpc.insecure_channel('{}:{}'.format(address, port))
        stub = sentiment_pb2_grpc.SentimentServiceStub(channel)
        request = sentiment_pb2.SentimentRequest(text=text)
        response = stub.getAspects(request)
        # print 'response'
        # print response
        sentences = response.sentences
        # print sentences

        datas = {}
        sentence_list = []

        for i, sentence in enumerate(sentences):
            data = {}
            data['text'] = sentence.text
            data['tokenizedText'] = sentence.tokenizedText
            #print sentence.opinions[0]
            #print type(sentence.opinions[0])
            op = []
            for i, opinion in enumerate(sentence.opinions):
                op_dict = {}
                op_dict['target'] = opinion.target
                op_dict['category'] = opinion.category
                op_dict['polarity'] = opinion.polarity
                #op_dict['start'] = opinion.start
                #op_dict['end'] = opinion.end
                op.append(op_dict)
            data['opinions'] = op
            sentence_list.append(data)

        datas['sentences'] = sentence_list
        
        json_data = json.dumps(datas)
        print json_data

        self.send_response(200, 'OK')
        # self.send_header('Content-type', 'application/json')
        self.send_header('Access-Control-Allow-Credentials', 'true')
        self.send_header('Access-Control-Allow-Origin', 'http://localhost:8080')
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(json_data)
        

if __name__ == '__main__':
    from BaseHTTPServer import HTTPServer
    #server = HTTPServer(('10.218.112.25', 22), GetHandler)
    server = HTTPServer(('127.0.0.1', 8080), GetHandler)
    server.serve_forever()
