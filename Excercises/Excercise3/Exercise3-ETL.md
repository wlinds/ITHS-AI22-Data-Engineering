# Exercise 3 - Handover code (ETL) 

In this exercíse you will get a scenario which unfortunately can happen in industry. 

---
## 0. The scenario

You have been on interview for an internship position at AIvataro AB, and got a very good feeling about the company. The supervisor is an experienced data scientist which has recently got into data engineering. Both you and the company has gotten good impression about each other, and you sign a contract to begin internship there. 

Now you start your internship and your supervisor can't be found anymore, she has apparently changed to another position with higher salary. Unfortunately she was the only data scientist there, so the product owner (PO) is your supervisor now instead. PO is not a technical person, and the other five people where one knows Azure and some other programming languages. They are very happy that you come in with your expertise in data science and data engineering. So you are the data expert here. 

PO shows you the handover that he got and tells you that they can't run the program anymore, but before it worked and it showed a dashboard, now it doesn't work and he doesn't know why. PO knows the value of the dashboard and knows what they want. 

---
## 1. Warmup

PO is tired of not understanding this cruical code, so he wants you to document it and explain the code in detail. Make an explanation on a higher level for PO and the team and one technical explanation for the technical person in the team. It would be nice to see pictures, diagrams or other visualizations to ease the explanation. You can try explain for a friend and see if it is understandable.

---

>**Probing questions**:
>
>I pulled some data from https://random-data-api.com and well, the dashboard works just fine... Kinda. We seem to be missing the entire database though. Any ideas of what happened to it? When was the last time the dashboard worked? 

>**High level explanation**
>
>The dashboard loads users data and supposedly tracks users positions.

>**Technical explanation**
>
>The dashboard loads data previously pulled from an API. The latitude/longtitude is not working.

## 2. Dockerize the app

The technical person wants you to dockerize the app so that it's possible to see the dashboard from localhost. Another requirement is that the data is persisted so we don't lose our user data. Then she can take over and deploy the app. Note that you might need to rewrite some parts of the code. 

---
## 3. Schedule

A non technical person in your team wants to have new users shown in the dashboard and asks you to schedule new set of 5 users every 2 minutes. The technical person says that you can use cron for this.

---
## 4. Further explorations

Now you have finished with the tasks given to you, try to find other things you can do to expand this code and/or explore the data. You are free to explore it further and impress on the PO and others in the team so that they see you and potentially hire you after the internship is finished.






