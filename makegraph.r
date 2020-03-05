library(readr)
setwd("~/3324-Scouting")
scouting <- read_csv("./match.csv")
attach(scouting)

# Need to store:
# Team Number
# Total Balls (or score)
# Auto Balls (or score)
# Climbing success rate

AutoScore <- c((`Auto Low Hit` * 2) + (`Auto High Outer` * 4) + (`Auto High Inner` * 6))
TeleScore <- c((`Tele High Inner` * 3) + (`Tele High Outer` * 2) + (`Tele Low Hit` * 1))
ClimbScore <- c()
TotalScore <- c(AutoScore + TeleScore)

team <- 3324
# print(args(2))
# print("howdy")
print(args(2))

plot(`TotalScore`[`Team Number`==team], ylim=c(min=0, max=40), xlab = "Match Number", ylab = "Total Power Cells Scored", main = team)
dev.copy(jpeg, "team.jpg")
dev.off()


