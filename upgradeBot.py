#!/usr/bin/python
# -*- coding: utf-8 -*-
import praw
import time


# Copied this character from a text message from someone with the bug.
# How it appears in text editors is variable.
theBadStr = "I️"
myUserName = 'UpgradeSuggestionBot'


bot = praw.Reddit(user_agent='UpgradeBot v1.3', client_id='zbsXTNm0j0zJ7Q', client_secret='xyKAWUAolx0g_rw3ouYi2-fcNjI', username=myUserName, password='mmiicckk')

subreddits = bot.subreddit('iphone+ipad+apple+ios+applehelp+appletv+applemusic+explainlikeimfive+geek+getnarwhal+lifeprotips+showerthoughts+wtf+gaming+technology+sports+nba+soccer+IAmA+trees+memes+bestof+subredditsimulator+android+iosthemes+iosprogramming+redditmobile+iosbeta+iosgaming+jailbreak')

comments = subreddits.stream.comments()

for comment in comments:
	if theBadStr in comment.body:
		print("\n\n********************")
		print(comment.submission.title)
		print("This guy: {0}".format(comment.author))
		print(comment.body)
		print(comment.submission.shortlink)
		
		alreadySuggested = False
		if (comment.parent().author == myUserName):
			alreadySuggested = True
			print("Already warned above")
		else:
			for reply in comment.replies:
				if reply.author == myUserName:
					alreadySuggested = True
					print("Already warned")
			
		if (not alreadySuggested):
			print("Issuing warning")
			try:
				comment.reply("Hi! I'm the iOS upgrade suggestion bot. It looks like you are using a version of iOS 11. You should upgrade to the latest version to fix a bug that substitutes garbage characters for the letter 'i'.\n\n[See this article at The Verge for more information about the bug.](https://www.theverge.com/2017/11/6/16611756/ios-11-bug-letter-i-a-unicode-symbol)")
			except Exception as e:
				print(e.response.status_code)
				time.sleep(60)
