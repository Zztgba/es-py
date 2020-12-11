## Elasticsearch 查询

### 字段类型 keyword 与 text

| 字段类型 | 是否分词 |
|  :----  | :----  |
| keyword | 不拆分 |
| text  | 拆分 |


### 简单查询 term、match、match_phrase、query_string、multi_match、prefix、range


|  查询方式  |  对查询词是否拆分  | keyword | text | 其他特性 |
|  :----  | :----  | :--- | :--- | :--- |
| term | 不会分词 | 不拆分+不拆分 => 完全匹配 | 不拆分+拆分 => 输入匹配text分词后的结果 |
| match | 会分词 | 拆分+不拆分 => 完全匹配 | 拆分+拆分 => 匹配任意一个分词即可 |
| match_phrase | 会分词 | 拆分+不拆分 => 完全匹配 | 拆分+拆分 => 所有分词按顺序匹配成功 |
| query_string | 同match查询一样 |
| multi_match | 同match查询一样 | - | - | 查询多个字段 |
| prefix | 不拆分 | 不拆分+不拆分 => 前缀完全一致 | 不拆分+拆分 => 前缀查询词符合任何一个分词的前缀 | 查询前缀匹配不支持查询词进行分词（gt大于，gte大于等于，lt小于，lte小于等于） |
| range | 范围查询 |  |  | 对查询字段进行范围过滤 |

### bool组合查询 must、 must_not、 should、 filter


|  组合查询关系  |  用途  |
|  :----  | :----  |
| must | 类似SQL中的 and， 必须包含其中的条件 |
| must_not | 类似SQL中的 not， 必须不包含其中的条件 |
| should | 满足其中条件增加查询分数，不影响查询结果 |
| filter | 与must类似，但不影响查询结果分数 |

