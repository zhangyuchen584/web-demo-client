#! /usr/bin/env python

import sys
import argparse
import codecs
import logging

import grpc

import sentiment_pb2
import sentiment_pb2_grpc

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

def get_text(filename):
    with codecs.open(filename, 'r', encoding='utf-8') as f:
        text = f.read()
    return text

def run(args):
    text = get_text(args.input)
    channel = grpc.insecure_channel('{}:{}'.format(args.address, args.port))
    stub = sentiment_pb2_grpc.SentimentServiceStub(channel)
    request = sentiment_pb2.SentimentRequest(text=text)
    response = stub.getAspects(request)
    sentences = response.sentences

    # request sentence


    for i, sentence in enumerate(sentences):
        # print i
        text = sentence.text
        # logging.info('SENTENCE: {}'.format(text))#print sentence
        print format(text) #sentence
        # tokenized_text = sentence.tokenizedText
        # logging.info('TOKENIZED: {}'.format(tokenized_text))#print token

        opinions = sentence.opinions #opinion
        for opinion in opinions:
            print ' target: {}' .format(opinion.target)
            print ' category: {}' .format(opinion.category)
            print ' polarity: {}' .format(opinion.polarity)
            print '\n'
            # logging.info('\tOPINION: {}, {}, {}, {}, {}'.format(opinion.target, opinion.category, opinion.polarity, opinion.start, opinion.end))
        logging.info('\n')
    return 0

def main():
    parser = argparse.ArgumentParser(description='Run client.',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('input', help='input file')
    parser.add_argument('port', help='port number', type=int)
    parser.add_argument('-a', '--address', help='host address', nargs='?', const='localhost', default='localhost')
    args = parser.parse_args()
    run(args)

if __name__ == '__main__':
    sys.exit(main())
