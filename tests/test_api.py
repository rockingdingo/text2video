# -*- coding: utf-8 -*-
# @Time    : 2024/06/27

import text2video as t2v
import json

def test_arxiv_api():

    input_dict = {"text": "Text to Video"}
    res = t2v.api(input_dict, model=None, api_name="ArxivPaperAPI", start=0, max_results = 3)
    paper_list = json.loads(res["text"])
    print ("###### Text to Image Recent Paper List:")
    for (i, paper_json) in enumerate(paper_list):
        print ("### PAPER %d" % (i+1))
        print (paper_json)

def main():
	test_arxiv_api()

if __name__ == '__main__':
	main()
