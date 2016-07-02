library(foreign)
library(rjson)

filename = "Democracy-Index-2014-English-for-website.sav"
dataset = read.spss(filename, to.data.frame=TRUE)

encode = function(vec) {
  num_responses = length(vec)
  encoded_data = rep(NA, num_responses)
  num_poss_responses = length(levels(vec))
  response_to_num = vector(mode="list", length=num_poss_responses)
  names(response_to_num) = levels(vec)
  max = floor(num_poss_responses / 2)
  min = -max
  for (i in 1:num_poss_responses) {
    if (i == num_poss_responses) {
      response_to_num[[i]] = NA
    } else {
      response_to_num[[i]] = max - i
    }
  }
  for (i in 1:num_responses) {
    encoded_data[i] = response_to_num[vec[i]]
  }
  return(encoded_data)
}

new_dataframe = data.frame(Location=dataset$C1)
new_dataframe$Sex = dataset$Q1c
new_dataframe$Age = dataset$Q2c

new_dataframe$Q1 = unlist(encode(dataset$Q1))
new_dataframe$Q2 = unlist(encode(dataset$Q2))
new_dataframe$Q3 = unlist(encode(dataset$Q3))
new_dataframe$Q4 = unlist(encode(dataset$Q4))
new_dataframe$Q5 = unlist(encode(dataset$Q5))
new_dataframe$Q6 = unlist(encode(dataset$Q6))
new_dataframe$Q7 = unlist(encode(dataset$Q7))
new_dataframe$Q8 = unlist(encode(dataset$Q8))
new_dataframe$Q9_1 = unlist(encode(dataset$Q9_1))
new_dataframe$Q9_2 = unlist(encode(dataset$Q9_2))
new_dataframe$Q9_3 = unlist(encode(dataset$Q9_3))
new_dataframe$Q9_4 = unlist(encode(dataset$Q9_4))
new_dataframe$Q9_5 = unlist(encode(dataset$Q9_5))
new_dataframe$Q9_6 = unlist(encode(dataset$Q9_6))
new_dataframe$Q9_7 = unlist(encode(dataset$Q9_7))
new_dataframe$Q9_8 = unlist(encode(dataset$Q9_8))
new_dataframe$Q9_9 = unlist(encode(dataset$Q9_9))
new_dataframe$Q9_10 = unlist(encode(dataset$Q9_10))
new_dataframe$Q10 = unlist(encode(dataset$Q10))
#new_dataframe$Q15 = dataset$Q15
#new_dataframe$Q16 = dataset$Q16
new_dataframe$Q17 = unlist(encode(dataset$Q17))
new_dataframe$Q18 = unlist(encode(dataset$Q18))
new_dataframe$Q19 = unlist(encode(dataset$Q19))
new_dataframe$Q20 = unlist(encode(dataset$Q20))
new_dataframe$Q21 = unlist(encode(dataset$Q21))
new_dataframe$Q22 = unlist(encode(dataset$Q22))
new_dataframe$Q23 = unlist(encode(dataset$Q23))
new_dataframe$Q27_1 = unlist(encode(dataset$Q27_1))
new_dataframe$Q27_2 = unlist(encode(dataset$Q27_2))

write.csv(new_dataframe, file="../data/idi_data.csv")

