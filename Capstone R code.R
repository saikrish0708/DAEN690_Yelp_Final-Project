#JSON TO CSV
library(jsonlite)
library(tibble)
#Business Dataset
yelp<-fromJSON("//datacloud.gmu.edu/scratch/DAEN-690 Project data-Krish//yelp_dataset/yelp_dataset~/dataset/business.json")
yelp <- stream_in(file("//datacloud.gmu.edu/scratch/DAEN-690 Project data-Krish//yelp_dataset/yelp_dataset~/dataset/business.json"))
head(yelp, 10)
yelp<-flatten(yelp)
head(yelp, 10)
yelp<-as_data_frame(yelp)
write.table(yelp, file="yelp",sep=",",row.names=F)
write.csv(yelp, "yelp.csv")
summary(yelp)
#Review Dataset
yelp1<-fromJSON("//datacloud.gmu.edu/scratch/DAEN-690 Project data-Krish//yelp_dataset/yelp_dataset~/dataset/review.json")
yelp1 <- stream_in(file("//datacloud.gmu.edu/scratch/DAEN-690 Project data-Krish//yelp_dataset/yelp_dataset~/dataset/review.json"))
head(yelp1, 10)
str(yelp1)
yelp1<-flatten(yelp1)
str(yelp1)
yelp1<-as_data_frame(yelp1)
yelp1
write.table(yelp1, file="yelp1",sep=",",row.names=F)
write.csv(yelp1, "yelp1.csv")
summary(yelp1)

#inner join two datasets
library(dplyr)
attach(yelp)
attach(yelp1)
yelp = merge( yelp, yelp1, by=business_id)

# tidy text
library(janeaustenr)
library(tidytext)
library(tidyr)
library(ggplot2)
library(qdap)
library(magrittr)
tidy = yelp%>%
  unnest_tokens(word,text)

# Removing Stop Words
data("stop_words")
tidy <- tidy %>% 
  anti_join(stop_words)

#Sentiment Lexicon
bingsentiment<- tidy %>%
  inner_join(get_sentiments("bing"))
nrcsentiment <- tidy %>%
  inner_join(get_sentiments("nrc"))

#Sentiment Count
bingsentiment %>%
  sentiment_counts <- count(business_id, sentiment)
nrcsentiment %>%
  sentiment_counts <- count(business_id, sentiment)

# Positive Percent
posbing = bingsentiment %>%
  group_by(business_id) %>%
  mutate(total = sum(n),
         percent = n / total) %>%
  filter(sentiment == "positive") %>%
  arrange(desc(percent))

# Negative percent
negbing = bingsentiment %>%
  group_by(business_id) %>%
  mutate(total = sum(n),
         percent = n / total) %>%
  filter(sentiment == "negative") %>%
  arrange(desc(percent))

# Visualizations
#Barplot for Bing
ggplot( bingsentiment, aes(x = sentiment, y = n)+ labs(title = "newplot")+
          geom_bar(stat = "identity") +
          theme_gdocs())
#Barplot for NRC
ggplot( nrcsentiment, aes(x = sentiment, y = n)+ labs(title = "newplot")+
          geom_bar(stat = "identity") +
          theme_gdocs())

#Wordcloud
cor <- Corpus(yelp)
cor <- Corpus(VectorSource(b1$text))
inspect((cor))
cor <- tm_map(cor, stripWhitespace)
cor <- tm_map(cor, tolower)
cor <- tm_map(cor, removeWords, stopwords('english'))
cor <- tm_map(cor, stemDocument)
inspect(cor)
cor <- tm_map(cor, removeNumbers)
cor <- tm_map(cor, removePunctuation)
wordcloud(lords, scale=c(5,0.5), max.words=150, random.order=FALSE, rot.per=0.35, use.r.layout=FALSE, colors=brewer.pal(8, 'Dark1'))

# Term Document Matrix
tdm <- TermDocumentMatrix( cor, 
                           control = list(
                             weighting = weightTfIdf,
                             removePunctuation = TRUE, 
                             stopwords = stopwords(kind = "en")
                           )
)

# Polarity density plot
pol = polarity(yelp$text)
ggplot(pol$all, aes(x = polarity, y = ..density..)) +
  theme_gdocs() + 
  geom_histogram(binwidth = 0.20, fill = "55", colour = "grey60") +
  geom_density(size = 0.80)

# Comparision of poistive and negative words
comparison.cloud( tdm, 
                  max.words = 35, 
                  colors = c("darkblue", "darkgreen")
)