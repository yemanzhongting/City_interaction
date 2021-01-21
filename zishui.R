library(ggplot2)
getwd()
setwd()

Road_Water <- read.csv("~/Road_Water.csv", encoding="UTF-8")

p<-geom_point(Road_Water,aes(x=count,y=POINUM,group=分类,color=POITYPE))
p

ggplot(aes(x=count,y=POINUM),data = Road_Water)+
  geom_point(aes(color=POITYPE,size=roadclass))
  #size=cases
  #scale_fill_gradientn(colors = c("black","yellow","red"),breaks = c(0,17,19),labels = format(c("0","17","19")))+
  xlim(0,quantile(new$green,1))+
  ylim(0,quantile(new$LAI,1)) +
  geom_smooth(method = 'lm',color='red')#+geom_text(aes(label = X1),nudge_x=0,nudge_y=0,check_overlap = TRUE)

  
  
grid.text(stargazer(zfit),0.2,0.4,just = c('left','bottom'))

install.packages('ggtern')

library(tidyverse)
library(ggtern)
library(hrbrthemes)
library(ggtext)

test_plot_pir <- ggtern(data =Road_Water,aes(x=count,y=POINUM,z=roadclass))+
  geom_point(aes(fill=POITYPE,size=2.5))+
  scale_fill_gradientn(colours=c("black","yellow","red"))+
  theme_rgbw(base_family = "Roboto Condensed") +
  labs(x="",y="",
       title = "Example Density/Contour Plot: <span style='color:#D20F26'>GGtern Test</span>",
       subtitle = "processed map charts with <span style='color:#1A73E8'>ggtern()</span>",
       caption = "Visualization by <span style='color:#DD6449'>DataCharm</span>") +
  guides(color = "none", fill = "none", alpha = "none")+
  theme(
    plot.title = element_markdown(hjust = 0.5,vjust = .5,color = "black",
                                  size = 20, margin = margin(t = 1, b = 12)),
    plot.subtitle = element_markdown(hjust = 0,vjust = .5,size=15),
    plot.caption = element_markdown(face = 'bold',size = 12),
  )

test_plot_pir
