#!/usr/bin/env/python
#_*_coding:utf-8_*_

import json
from elasticsearch import Elasticsearch

ES = [
	'127.0.0.1:9200',
]

es = Elasticsearch(ES, sniff_on_start=True, sniffer_timeout=60)



def search1_game_name():
	"""
	仅对游戏名进行分页查询
	"""
	query = {
		"query": {
			"match": {"name": "地狱"}
		},
		"_source": ["id", "name"],
		"sort": [
			{"id": "desc"},
		],
		"from": 0,
		"size": 10,
	}
	result = es.search(index="game", body=query)
	print(json.dumps(result, indent=2, ensure_ascii=False))


def search2_game_name():
	"""
	一个关键词，多字段查询
	游戏名，游戏简介一起查询
	"""
	query = {
		"query": {
			"multi_match": {
				"query": "王国",
				"fields": ["name", "introduce"],
			},
		},
		"_source": ["id", "name"],
		"sort": [
			{"id": "desc"},
		],
		"from": 0,
		"size": 10,
	}
	result = es.search(index="game", body=query)
	print(json.dumps(result, indent=2, ensure_ascii=False))


def search3_game_name():
	"""
	多个关键词，允许顺序关键词移位的搜索 slop移动次数
	"""
	query = {
		"query": {
			"multi_match": {
				"query": "王国 地狱",
				"fields": ["name", "introduce"],
				"slop": 1
			},
		},
		"_source": ["id", "name"],
		"from": 0,
		"size": 10,
	}
	result = es.search(index="game", body=query)
	print(json.dumps(result, indent=2, ensure_ascii=False))



def search4_game_name():
	"""
	多条件优先级查询结果
	boost默认是1，数字越小优先级越高
	"""
	query = {
		"query": {
			"bool": {
				"must": [
					{"match": {"name": "王"}}
				],
				"shoule": [
					{"match": {"py_name": {"query": "王", "boost": 2}}},
					{"match": {"introduce": {"query": "王", "boost": 4}}},
					{"match": {"en_name": {"query": "wang", "boost": 3}}},
				]
			}
		},
		"_source": ["id", "name"],
		"from": 0,
		"size": 10,
	}
	result = es.search(index="game", body=query)
	print(json.dumps(result, indent=2, ensure_ascii=False))


search4_game_name()