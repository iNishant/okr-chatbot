## intent:create_objective
- create okr
- add okr
- new okr
- create objective
- add objective
- new objective

## intent:create_key_result
- create kr
- add kr
- new kr
- create key result
- add key result
- new key result

## intent:list_okrs
- list okrs
- show okrs
- display okrs
- my okrs
- okrs
- list objectives
- show objectives
- display objectives
- my objectives
- objectives

## intent:delete_objective
- remove okr
- delete okr
- delete objective
- remove objective

## intent:affirm
- yes
- indeed
- of course
- that sounds good
- correct

## intent:deny
- no
- never
- I don't think so
- don't like that
- no way
- not really

## intent:new_kr_title
- increase [nps](positive_metric) to [8.5](goal_value)
- increase [nps](positive_metric) from [6](start_value) to [9](goal_value)
- increase [sales growth](positive_metric) from [5%](start_value) to [10%](goal_value)
- decrease [churn](negative_metric) to [2%](goal_value)
- decrease [churn](negative_metric) from [4%](start_value) to [3%](goal_value)
- decrease [CAC](negative_metric) from [100](start_value) to [50](goal_value)

## synonym:increase
- improve
- better
- launch
- reach
- celebrate
- get into
- finalize
- enhance
- maximise
- optimise

## synonym:decrease
- reduce
- cut down
- avoid
- negate
- lessen
- minimise

## lookup:positive_metric
data/lookup_tables/kr_positive_metrics.txt

## lookup:negative_metric
data/lookup_tables/kr_negative_metrics.txt

<!-- TODO: check for INR, dollar symbol in numbers -->
## regex:goal_value 
- [0-9]?[0-9,\.,\%]+

## regex:start_value
- [0-9]?[0-9,\.,\%]+
