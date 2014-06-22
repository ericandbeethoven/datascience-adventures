# scraping URL example
con <- url("http://www.jhsph.edu",'r')
x <- readLines(con)
head(x)
help(x)
help(url)
# lapply (to apply FN to a list)

# read CSV example
twitter_followers <- read.csv("~/Downloads/twitter_followers.csv")
View(twitter_followers)
twitter_followers$name

# K-means clustering example
set.seed(1234)
par(mar=c(0,0,0,0))
x<-rnorm(12,mean=rep(1:3, each=4), sd=0.2)
y<-rnorm(12,mean=rep(c(1,2,1), each=4), sd=0.2)
plot(x,y, col="green", pch=19, cex=2)
text(x+0.05, y+0.05, labels=as.character(1:12))