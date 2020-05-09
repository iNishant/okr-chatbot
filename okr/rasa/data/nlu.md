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
- Grow [MRR](positive_metric) by 15% in Q3 to [$135000](goal_value)
- Reduce [infrastructure costs](negative_metric) from [$2000](start_value) to [$1000](goal_value)
- Improve [engagement](positive_metric) (users that complete a full profile) from [12000](start_value) to [15000](goal_value)
- Improve average [weekly visits](positive_metric) per active user from [1000](start_value) to [200](goal_value)
- Increase [engineering effort](positive_metric) by 100% by EOQ (from [75](start_value) units per week to [150](goal_value) units per week)
- Grow [MRR](positive_metric) 15% in Q3 to [$135000](goal_value)
- Increase [Repurchase Rate](positive_metric) from [50%](start_value) to [80%](goal_value)
- 70% increase in new [trial sign-ups](positive_metric) from organic vs Q2
- Achieving a [conversion rate](positive_metric) of [5%](goal_value) from free to paid users
- Create a new lead generation campaign for iphone 7
- Release a beta version of ios 13
- Complete internal audit (with the help of an external observer)
- Develop [3](goal_value) new [landing pages](positive_metric)
- Recieve ISO 27001 certification
- Develope and launching a new employee training program for l1 engineers
- Conduct a soft skills workshop in 2020
- Conduct [3](goal_value) engineering workshops in 2020
- conduct the first engineering worshop for the year 2020 before June

## intent:new_objectives_title
- grow business
- delight customer base
- improve corporate culture
- launch the new version of the os
- generate marketing leads
- improve customer acquisition
- account based marketing
- improve conversions
- launch newsletter
- improve blog strategy
- increase brand awareness
- strong relationships with gartner
- strong relationships with forrester
- launch customer community
- launch partners/sellers community

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

<!-- TODO: check for INR, dollar symbol in numbers -->
## regex:goal_value 
- [0-9]?[0-9,\.,\%]+

## regex:start_value
- [0-9]?[0-9,\.,\%]+
