#!/usr/bin/env/python
#_*_coding:utf-8_*_

from elasticsearch import Elasticsearch


ES = [
	'127.0.0.1:9200',
]

es = Elasticsearch(ES, sniff_on_start=True, sniffer_timeout=60)

board_mappings = {
	"properties": {
		'name': {
			'type': 'text',
			'analyzer': 'ik_max_word',
			'search_analyzer': 'ik_max_word',
			},
		'py_name': {
			'type': 'text',
			'analyzer': 'pinyin',
			'search_analyzer': 'pinyin',
			},
		'introduce': {
			'type': 'text',
			'analyzer': 'ik_max_word',
			'search_analyzer': 'ik_max_word'
		},
		'game_list': {
			'type': 'text',
			'analyzer': 'ik_max_word',
			'search_analyzer': 'ik_max_word',
		},
	},
}

game_mappings = {
	"properties": {
		'name': {
			'type': 'text',
			'analyzer': 'ik_max_word',
			'search_analyzer': 'ik_max_word',
			},
		'en_name': {
			'type': 'text',
			},
		'py_name': {
			'type': 'text',
			'analyzer': 'pinyin',
			'search_analyzer': 'pinyin',
			},
		'introduce': {
			'type': 'text',
			'analyzer': 'ik_max_word',
			'search_analyzer': 'ik_max_word'
		},
		'tag_name': {
			'type': 'text',
			'analyzer': 'ik_max_word',
			'search_analyzer': 'ik_max_word',
		},
	},
}


def insert_index():
	es.indices.delete(index='board', ignore=[400, 404])
	es.indices.create(index='board', ignore=400)
	es.indices.put_mapping(index='board', doc_type='boardinfo', body=board_mappings)

	es.indices.delete(index='game', ignore=[400, 404])
	es.indices.create(index='game', ignore=400)
	es.indices.put_mapping(index='game', doc_type='gameinfo', body=game_mappings)

	pass

def insert_game(id, name, en_name, py_name, introduce, tag_name):
	"""
	新增游戏
	:param id: 游戏id
	:param name: 游戏名
	:param en_name: 游戏英文名
	:param py_name: 游戏名拼音
	:param introduce: 游戏简介
	:param tag_name: 游戏标签
	"""
	data_game = {
		"id": id,
		"name": name,
		"en_name": en_name,
		"py_name": py_name,
		"tag_name": tag_name,
		"introduce": introduce
	}
	res = es.create(index="game", id=id, body=data_game, doc_type="gameinfo")
	print(res)



def insert_board(id, name, py_name, introduce, game_list):
	"""
	新增榜单
	:param id: 榜单id
	:param name: 榜单名
	:param py_name: 榜单拼音名
	:param introduce: 榜单简介
	:param game_list: 榜单游戏名
	"""
	data_board = {
		"id": id,
		"name": name,
		"py_name": py_name,
		"game_list": game_list,
		"introduce": introduce
	}
	res = es.create(index="board", id=id, body=data_board, doc_type="boardinfo")
	print(res)

