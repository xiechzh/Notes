# NOTES
# THIS FILE IS HOW TO SET UP FOR ELASTICRESEARCH
# ELASTICRESEARCH CAN GET DATA FROM DATABASE
# THIS SCRIPT CANNOT RUN, ONLY NOTE

1.Restful基本原理

#MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
#**************************************************************************************************************
#WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW

#*************************  LITZ  *******************************
#****************************************************************

TEMINAL: $ vi config
SCRIPT:
Host prod-credits
HostName data-access.jaxsta.io
User ec2-user
IdentitiesOnly yes
IdentityFile /Users/sophiexie/Downloads/downey.pem
LocalForward 9400 search.jaxsta.io:80

TEMINAL: $ :wq!
TEMINAL: $ ssh prod-credits

LOCALHOST BROWSER:
http://localhost:9400/_plugin/kibana/app/kibana#/dev_tools/console?_g=(filters:!())

QUERY:
GET release/_search
{
  "_source": ["rank", "release_type", "variants.id",
  "title", "id"],
  "size": 4000,
	"query": {
		"bool": {
			"must": [{
				"function_score": {
					"score_mode": "multiply",
					"functions": [{
						"field_value_factor": {
							"factor": 1,
							"field": "rank",
							"modifier": "sqrt",
							"missing": 1
						}
					}]
				}
			}, {
				"nested": {
					"path": "credits",
					"query": {
						"bool": {
							"must": [{
								"match": {
									"credits.entity_id": "41d8cfe1-3bae-44ae-9e7b-18835d31949a"
								}
							}]
						}
					}
				}
			}]
		}
	},
	"sort": [{
		"rank": {
			"order": "desc"
		}
	}]
}

# DOWNLOAD RESULT TO LOCAL
TEMINAL: $ curl -XGET "http://localhost:9400/release/_search" -H 'Content-Type: application/json' -d'{  "_source": ["rank", "release_type", "variants.id",  "title", "id"],  "size": 4000,	"query": {		"bool": {			"must": [{				"function_score": {					"score_mode": "multiply",					"functions": [{						"field_value_factor": {							"factor": 1,							"field": "rank",							"modifier": "sqrt",							"missing": 1						}					}]				}			}, {				"nested": {					"path": "credits",					"query": {						"bool": {							"must": [{								"match": {									"credits.entity_id": "41d8cfe1-3bae-44ae-9e7b-18835d31949a"								}							}]						}					}				}			}]		}	},	"sort": [{		"rank": {			"order": "desc"		}	}]}' >> MichaelJackson_page1.json

# DATA DOWNLOAD TO MichaelJackson_page1.json

#***********************  bilibili  *****************************
#****************************************************************

ES 主流基于Restful框架

# ==== RESTFUL ====
1.和传统的url请求方式不一样
tradition URL：http://localhost:8989/xxx/find?id=21
RestURL: http://localhost:8989/xxx/find/21/name/
2.use HTTP GET POST PUT DELETE

# ==== ES 优点 ====
full text retrieval
1. 效率比数据库查询效率高
2. 搜索结果存在相关度排序
3. 搜索时关键词不区分大小写

# ==== ES 概念 ====
NRT --- near real time
index
type
mapping
document

# ==== ES 更新 ====
# 把原来的删除，重新写入新的数据
POST /dangdang/book/1
{
	"doc":{
		"name": "小白羊的故事"
	}
}
# 在原来数据的基础上更新
POST /dangdang/book/1/_update
# 批量更新
POST /dangdang/book/_bulk
{"index":{"_id": "3"}}
	{"name":"sophie"}
{"index":{}}

# ==== ES 删除 ====
DELETE /dangdang/book/1

# ==== ES 检索 ====
ES官方提供两种检索方式：通过url参数进行搜索 ｜ 通过DSL进行搜索（Domain Specified Language）

# ==== ES DSL检索 返回所有 ====
GET release/_search
{
	"query":{
		"match_all": {}
	},
	"size": 8
}

# ==== ES DSL检索 ====
"_source" : 只返回特定字段
"worldcard": * ?
"ids": 多id查询
"fuzzy": 模糊查询


# ==== ES DSL检索 term基于关键词查询 ====
GET release/_search
{
	"query":{
		"term": {
			"release_type": {
				"value": "Album"
			}
		}
	},
	"size": 8
}
# DSL 对于text的类型进行分词，对于其他的类型都不分词
# ES 使用StandardAnalyzer




